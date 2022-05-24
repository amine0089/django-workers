from django.conf import settings
from accounts.models import User
from accounts.models import Client
from django.contrib import messages
from base.views import must_be_opened
from django.contrib.auth import logout
from django.core.mail import send_mail
from base.models import Client_Investment
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site

import stripe
import secrets
import traceback
import decimal

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
@login_required
def checkout(request):
    context = {'key': settings.STRIPE_PUBLISHABLE_KEY}
    return render(request, 'payment_template.html', context)


# May be protected by some decorators
# Must include robust error handling
# Create transaction for all actions required in db after charge's payment.

@must_be_opened
@login_required
def charge(request, invest):
    id_offer_obj = invest
    obj_invest = Client_Investment.objects.get(id=id_offer_obj)

    context = {}
    if request.method == 'POST':
        # retrieve associated customer, and make charge
        try:
            creditcardnumber = request.POST.get('creditcardnumber')
            exp_month = request.POST.get('month_year')
            month_year = exp_month.split('/')
            exp_month = month_year[0]

            # print("\n" * 3)
            # print("month_year is ------->", month_year)

            cardcode = request.POST.get('cardcode')
            amount = request.POST.get('amount_entered')
            # print(amount)
            exp_year = month_year[1]
            token = stripe.Token.create(
                card={
                    "number": str(creditcardnumber).replace(' ', ''),
                    "exp_month": int(exp_month),
                    "exp_year": int(exp_year) + 2000,
                    "cvc": str(cardcode)
                },
            )
            charge = stripe.Charge.create(
                amount=int(eval(amount)) * 100,
                currency='usd',
                description=f'{obj_invest.client.user.username} pay for {obj_invest.investment.name}',
                source=token
            )
            if charge['paid']:
                # letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
                # payment_token = ''.join(random.choice(letters) for _ in range(10))
                payment_token = secrets.token_hex(64)
                obj_invest.payment_token = payment_token
                obj_invest.done = True
                obj_invest.save()

                site_url = get_current_site(request)
                site_url = str(site_url)
                # user_id = request.user.id
                email = request.user.email
                client = Client.objects.get(user=request.user)
                subject = 'Request For Approval'
                message = ""
                userr = User.objects.get(username=request.user)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['info@solomartel.com']
                html_message = render_to_string('payment/approval.html',
                                                {'client_obj': client, 'email': email, 'payment_token':
                                                    payment_token, 'transaction': obj_invest,
                                                 'site_url': site_url, 'userr' : userr})
                send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                          html_message=html_message, fail_silently=False)
                # client.payment_done = True,
                # client.token = payment_token
                # client.save()

                return redirect(reverse('payment:thankyou'))
        except stripe.error.CardError as e:
            traceback.print_exc()
            context = {
                'status': e.http_status,
                'error': e.error.type,
                'code': e.error.code,
                'param': e.error.param,
                'message': e.error.message,
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj
            }
            return render(request, 'payment/credit_card.html', context)
        except stripe.error.RateLimitError:
            traceback.print_exc()
            context = {
                'error': 'RatelimitError',
                'message': 'Too many requests made to the API too quickly',
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj
            }
            return render(request, 'payment/credit_card.html', context)
        except stripe.error.InvalidRequestError:
            traceback.print_exc()
            context = {
                'error': 'InvalidRequestError',
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj,
                'message': 'Invalid parameters were supplied to Stripe\'s API'
            }
            return render(request, 'payment/credit_card.html', context)
        except stripe.error.AuthenticationError:
            traceback.print_exc()
            context = {
                'error': 'AuthenticationError',
                'message': 'Authentication with Stripe\'s API failed',
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj
            }
            return render(request, 'payment/credit_card.html', context)
        except stripe.error.APIConnectionError:
            traceback.print_exc()
            context = {
                'error': 'APIConnectionError',
                'message': 'Network communication with Stripe failed',
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj
            }
            return render(request, 'payment/credit_card.html', context)
        except Exception as e:
            traceback.print_exc()
            context = {
                'error': 'StripeError',
                'message': 'Something went wrong, check your email',
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj
            }
            return render(request, 'payment/credit_card.html', context)
        except Exception:
            traceback.print_exc()
            context = {
                'error': 'Exception',
                'message': 'An error occured',
                'obj_invest': obj_invest,
                'id_offer_obj': id_offer_obj
            }
            return render(request, 'payment/credit_card.html', context)

    id_offer_obj = invest
    obj_invest = Client_Investment.objects.get(id=id_offer_obj)
    context['obj_invest'] = obj_invest
    context['id_offer_obj'] = id_offer_obj
    return render(request, 'payment/credit_card.html', context)

@must_be_opened
@login_required
def banktransfer(request, invest):
    id_offer_obj = invest
    obj_invest = Client_Investment.objects.get(id=id_offer_obj)

    context = {}
#    if request.method == 'POST':
        # retrieve associated customer, and make charge
    try:
            payment_token = secrets.token_hex(64)
            obj_invest.payment_token = payment_token
            obj_invest.done = True
            obj_invest.save()

            site_url = get_current_site(request)
            site_url = str(site_url)
            # user_id = request.user.id
            email = request.user.email
            userr = User.objects.get(username=request.user)
            client = Client.objects.get(user=request.user)
            subject = 'Request For Approval'
            message = ""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['info@solomartel.com']
            html_message = render_to_string('payment/approval.html',
                                            {'client_obj': client, 'email': email, 'payment_token':
                                                payment_token, 'transaction': obj_invest,
                                                'site_url': site_url, 'userr' : userr})
            send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                        html_message=html_message, fail_silently=False)

            return redirect(reverse('payment:thankyou'))
    except Exception:
        traceback.print_exc()
        context = {
            'error': 'Exception',
            'message': 'An error occured',
            'obj_invest': obj_invest,
            'id_offer_obj': id_offer_obj
        }
        return render(request, 'payment/direct_bank.html', context)

    id_offer_obj = invest
    obj_invest = Client_Investment.objects.get(id=id_offer_obj)
    context['obj_invest'] = obj_invest
    context['id_offer_obj'] = id_offer_obj
    return render(request, 'payment/direct_bank.html', context)


def thankyou(request):
    return render(request, 'payment/thankyou.html')


#@login_required
def confirm_transaction(request):
    try:
        token = request.GET.get('token')
#       email = request.GET.get('email')
        email = settings.EMAIL_HOST_USER
        invest = int(request.GET.get('invest'))
        try:
            email_Check = User.objects.get(email=email)

            # user_info = Client.objects.filter(user=email_Check)
            offer_obj = Client_Investment.objects.get(id=invest)

            if offer_obj.payment_token == token:

                try : 
                    client_offer = Client_Investment.objects.get(id=invest, status = "Not achieved")
                    client_offer.approved = True
                    client_offer.status = 'Complete'
                    client_offer.investment.invested_amount += decimal.Decimal(client_offer.invested_amount)
                    client_offer.investment.save()
                    client_offer.save()

                    messages.success(request, "The transaction has been successfully approved.")

                    # messages.success(request, 'You have successfully Approve this request, You can Check Here')

                    # First mail for user

                    email = client_offer.client.user.email
                    client = client_offer.client
                    subject = 'Approval accepted'
                    message = ""
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [client_offer.client.user.email]
                    html_message = render_to_string('payment/approved_notification.html', {'transaction': client_offer})

                    mail_1 = send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                            html_message=html_message, fail_silently=False)
                    
                    if mail_1 == 0:
                        messages.error(request, "An error has occurred trying to contact the customer. Please check if customer e-mail is correct.")
                        return redirect(reverse('accounts:login'))


                    # Second mail for the admin
                    site_url = get_current_site(request)
                    subject = f'Update on fund: {client_offer.investment.name}'
                    message = ""
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['info@solomartel.com']

                    percentage_reached = (client_offer.investment.invested_amount * 100) / client_offer.investment.amount_needed
                    amount_left = client_offer.investment.amount_needed - client_offer.investment.invested_amount
                    if 25 <= percentage_reached < 30:
                        html_message = render_to_string('payment/update_fund.html',
                                                        {'transaction': client_offer, 'amount_left': amount_left,
                                                        'needed_percentage': percentage_reached, 'site_url': site_url,
                                                        'reached': 25})
                        send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                                html_message=html_message, fail_silently=False)
                    elif 50 <= percentage_reached < 55:
                        html_message = render_to_string('payment/update_fund.html',
                                                        {'transaction': client_offer, 'amount_left': amount_left,
                                                        'needed_percentage': percentage_reached, 'site_url': site_url,
                                                        'reached': 50})
                        send_mail(subject, message, f'Solomartel Holdings<{email_from}', recipient_list,
                                html_message=html_message, fail_silently=False)
                    elif 75 <= percentage_reached < 80:
                        html_message = render_to_string('payment/update_fund.html',
                                                        {'transaction': client_offer, 'amount_left': amount_left,
                                                        'needed_percentage': percentage_reached, 'site_url': site_url,
                                                        'reached': 75})
                        send_mail(subject, message, f'Solomartel Holdings<{email_from}', recipient_list,
                                html_message=html_message, fail_silently=False)
                    elif 95 <= percentage_reached <=100:
                        html_message = render_to_string('payment/update_fund.html',
                                                        {'transaction': client_offer, 'amount_left': amount_left,
                                                        'needed_percentage': percentage_reached, 'site_url': site_url,
                                                        'reached': 95})
                        send_mail(subject, message, f'Solomartel Holdings<{email_from}', recipient_list,
                                html_message=html_message, fail_silently=False)
                
                    return redirect(reverse('accounts:login'))

                except Client_Investment.DoesNotExist:
                    traceback.print_exc()
                    messages.error(request, "An error as occurred. Transaction has not been approved.")
                    return redirect(reverse('accounts:login'))
            else:
                messages.error(request, 'Invalid Payment Token,please try again')
                return redirect(reverse('accounts:login'))
        except User.DoesNotExist:
            traceback.print_exc()
            messages.error(request, "Invalid Informations, please try again")
            return redirect(reverse('accounts:login'))
    except:
        traceback.print_exc()
#        messages.error(request, "Unknown error, please try again thank you.")
        return redirect(reverse('accounts:login'))


def direct_bank(request, tid):
    transaction = Client_Investment.objects.select_related('investment').get(id=tid)
    investment = transaction.investment
    return render(request, 'payment/direct_bank.html', {'investment': investment, 'tid': tid, 'transaction': transaction})
