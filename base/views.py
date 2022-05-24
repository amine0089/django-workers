from django.urls import resolve
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from base.models import Testimonial, Investment, PropertyPicture, Remark, Client_Investment, PromoCode, Distribution, Pastproject,Pastprojectpicture,PastprojectPromotionalDocument
from accounts.models import Client
from django.db.models import Sum

import decimal
import traceback


def must_be_opened(view):
    def wrapper(*args, **kwargs):
        try:
            if isinstance(list(kwargs.values())[0], str):
                fund = Investment.objects.get(name=list(kwargs.values())[0])
                if not fund.closed:
                    return view(*args, **kwargs)
                else:
                    client = Client.objects.get(user=args[0].user)
                    transaction = Client_Investment.objects.filter(client=client, investment=fund)[0]
                    if transaction.approved and transaction.status == 'Complete':
                        context = {'investment_record': fund}
                        tot_client_investment = Client_Investment.objects.filter(client=client, investment=fund, approved=True).aggregate(Sum('invested_amount'))
#                        percentage_invested = ((transaction.invested_amount['invested_amount__sum'] * 100) / fund.invested_amount) * (1-fund.SoloMartel_ownership/100)
                        percentage_invested = (tot_client_investment['invested_amount__sum']* 100 / fund.invested_amount) * (1-fund.SoloMartel_ownership/100)
                        context['client_investment'] = transaction
                        context['percentage_invested'] = percentage_invested
                        context['tot_client_investment'] = tot_client_investment
                        distributions = Distribution.objects.filter(investment=fund).order_by('distribution_date')
                        new_distributions = Distribution.objects.filter(investment=fund).annotate(client_amount = Sum("distributed_amount") * percentage_invested/100).order_by('-distribution_date')
                        context['distributions'] = distributions
                        context['new_distributions'] = new_distributions
                        return render(args[0], 'investments/view_investment.html', context)
                    else:
                        messages.error(args[0], 'This fund is already closed')
                        return redirect(reverse('base:investments'))
            elif isinstance(list(kwargs.values())[0], int):
                transaction = Client_Investment.objects.get(id=list(kwargs.values())[0])
                if not transaction.investment.closed:
                    return view(*args, **kwargs)
                else:
                    messages.error(args[0], 'This fund is already closed')
                    return redirect(reverse('base:investments'))
        except Investment.DoesNotExist:
            messages.error(args[0], 'Invalid fund key: This fund doesn\'t exist')
            return redirect(reverse('base:investments'))
        except Client_Investment.DoesNotExist:
            messages.error(args[0], 'This fund is already closed or doesn\'t exist!')
            return redirect(reverse('base:investments'))

    return wrapper


# Create your views here.

def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'base/home.html', {'testimonials': testimonials})


def contact(request):
    if request.method == 'POST':
        subject=request.POST['first_name']
        email=request.POST['email']
        message=request.POST['message'] 
        
        send_mail(
            subject + " the is my email " + email,
            message,
            settings.EMAIL_HOST_USER,
            ['info@solomartel.com'],
            fail_silently = False
        )
    return render(request,'base/contacts.html',{})


def faq(request):
    return render(request, 'base/faq.html')


def about(request):
    return render(request, 'base/about-us.html')


def investments(request):
    context = {}
    invests = Investment.objects.exclude(closed = True)
    context['investments'] = invests
    pastprojects = Pastproject.objects.all()
    context['pastprojects'] = pastprojects
    if pastprojects.count() == 0:
        context['msg2'] = "At the moment we have no current past projects. Please come back later."
    if invests.count() == 0:
        context['msg1'] = "At the moment we have no Investments availables. Please come back later."

    return render(request, 'investments/investments.html', context)


def question_through_email(request):
    try:
        if request.method == 'POST':
            site_url = get_current_site(request)
            email = request.POST.get('email')
            user_query = request.POST.get('query')

            subject = "You've received messages from {}".format(email)
            message = ""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@solomartel.com']
            msg_html = render_to_string('email/question_email.html',
                                        {'your_query': user_query, 'email': email, 'site_url': site_url})
            send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                      html_message=msg_html, fail_silently=False, )

            messages.success(request, 'Your question has been sent successfully')
        return redirect(reverse('base:investment', kwargs={'name': request.session['investment']}))

    except Exception as e:
        traceback.print_exc()
        messages.error(request, str(e))
        return redirect(reverse('base:investment', kwargs={'name': request.session['investment']}))

@login_required
@must_be_opened
def investment(request, name):
    context = {}
    try:
        investment_record = Investment.objects.get(name=name)
        context['investment_record'] = investment_record
        request.session['investment'] = name
        if request.user.is_authenticated:
            client = Client.objects.get(user=request.user)
            client_investment = Client_Investment.objects.filter(client=client, investment=investment_record,
                                                              approved=True)
            if not client_investment:
                return render(request, 'investments/detail_investment.html', context)
            for inv in client_investment:
                tot_amount = inv.invested_amount
            percentage_invested = (tot_amount * 100) / investment_record.invested_amount
            context['client_investment'] = client_investment
            context['percentage_invested'] = percentage_invested
            # with_profile_pic = investment_record.my_images.all()[0]

            distributions = Distribution.objects.filter(investment=investment_record).order_by('distribution_date')
            context['distributions'] = distributions
            return render(request, 'investments/detail_investment.html', context)
        return render(request, 'investments/detail_investment.html', context)
    except Investment.DoesNotExist:
        context['msg'] = 'Something went wrong, Please try again later'
        return render(request, 'investments/detail_investment.html', context)
    except Client_Investment.DoesNotExist:
        traceback.print_exc()
        return render(request, 'investments/detail_investment.html', context)
    except Client.DoesNotExist:
        return render(request, 'investments/detail_investment.html', context)


def past_projects(request):
    context = {}
    pastprojects = Pastproject.objects.all()
    context['pastprojects'] = pastprojects
    try:
        return render(request, 'base/past_projects.html', context)
    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong,Please try again later'
        return render(request, 'base/past_projects.html', context)

def past_project(request, name):
    context = {}
    try:
        investment_record = Pastproject.objects.get(name=name)
        context['investment_record'] = investment_record
        request.session['investment'] = name
        return render(request, 'investments/detail_past_projects.html', context)
    except Pastproject.DoesNotExist:
        context['msg'] = 'Something went wrong, Please try again later'
        return render(request, 'investments/detail_past_projects.html', context)


@must_be_opened
@login_required
def investment_form(request, invest):
    context = {}
    try:
        investment_record = Investment.objects.get(name=invest)
        context['investment_record'] = investment_record
        try:
            client = Client.objects.get(user=request.user)
            client_investment = Client_Investment.objects.filter(client=client, investment=investment_record)
            
            for i in client_investment:

                if not i.payment_token and i.status == 'Not achieved':
                    return redirect(reverse('base:choose_payment', kwargs={'invest': i.id}))
                if not (i.approved and i.status == 'Complete'):
                    messages.error(request, 'You already have an investment in this fund waiting to be approved.')
                    return redirect('base:investments')
        except Client_Investment.DoesNotExist:
            pass

        if request.method == 'POST':
            investmentamount = request.POST.get('investmentamount')
            promocode = request.POST.get('promocode')
            check_offer = Client_Investment.objects.filter(investment=investment_record, client=client)
#            if check_offer:
#                context['msg'] = 'Sorry, You already offer for this investment'
#                return render(request, 'investments/invest_form.html', context) 

            client_investment = Client_Investment.objects.create(
                investment=investment_record, invested_amount=decimal.Decimal(investmentamount),
                client=client, status='Not achieved')

            # investment_record.invested_amount += decimal.Decimal(investmentamount)
            # investment_record.save()

            if promocode:
                try:
                    promo_object = PromoCode.objects.get(code=promocode)
                    client_investment.promocode = promo_object
                    client_investment.save()
                except PromoCode.DoesNotExist:
                    context['msg'] = 'Invalid Promo code'
                    return render(request, 'investments/invest_form.html', context)
                except:
                    traceback.print_exc()
            context[
                'success_msg'] = 'Thank you for your registration ! Your offer has been successfully created,Enter your details to Compelete payment process'
            return redirect(reverse('base:choose_payment', kwargs={'invest': client_investment.id}))
        # context['get_id_of_investoment'] = invest
        return render(request, 'investments/invest_form.html', context)
    except Investment.DoesNotExist:
        context['msg'] = 'Unrecognized investment'
        return render(request, 'investments/invest_form.html', context)
    except:
        traceback.print_exc()
        context['msg'] = 'An error has ocurred. Please try again later'
        return render(request, 'investments/invest_form.html', context)


@must_be_opened
@login_required
def choose_payment(request, invest):
    context = {}
    try:
        context['id_offer_obj'] = invest
        return render(request, 'investments/payment_way.html', context)
    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong,Please try again later'
        return render(request, 'investments/payment_way.html')


@login_required
def my_transactions(request):
    context = {}
    try:
        # request_user = request.user.id
        client = Client.objects.get(user=request.user)
        transactions = Client_Investment.objects.filter(client=client)
        context['all_transactions'] = transactions
        return render(request, 'investments/my_transactions.html', context)
    except:
        traceback.print_exc()
        return render(request, 'investments/my_transactions.html')


@login_required
def my_investments(request):
    try:
        request_user = request.user.id
        client = Client.objects.get(user=request.user)
        investments = Client_Investment.objects.filter(client=client, done=True, approved=True, investment__closed=False)
        investments_closed = Client_Investment.objects.filter(client=client, done=True, approved=True, investment__closed=True).values(
            'investment__name',
            'investment__net_returns',
            'investment__gross_returns',
            'investment__market_value',
            'investment__my_images__image').annotate(tot_amount=Sum('invested_amount'))

#Clean the investment_closed QuerySet and only obtain one register for Investment
        inv=""

        inv_list_closed=list(investments_closed)
        for i,investment_instance in enumerate(inv_list_closed):
            if investment_instance['investment__name']==inv:
                del inv_list_closed[i]
            else:
                inv=investment_instance['investment__name']
                im=investment_instance['investment__my_images__image']




        #investments = Client_Investment.objects.filter(client=client, done=True, approved=True).values('investment__name').annotate(Sum('invested_amount'))
        context = {'transactions': investments, 'investments_closed' : inv_list_closed,'media_url': settings.MEDIA_URL}
        return render(request, 'investments/my_investments.html', context)
    except:
        traceback.print_exc()
        return render(request, 'investments/my_investments.html')


@login_required
def delete_investment(request, id):
    try:
        transaction_to_delete = Client_Investment.objects.get(id=id)
        transaction_to_delete.delete()
        messages.success(request, 'Your offer has been successfully deleted')
    except Client_Investment.DoesNotExist:
        traceback.print_exc()

    return redirect(reverse('base:my_transactions'))
