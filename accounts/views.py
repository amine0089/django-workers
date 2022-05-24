from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from accounts.models import User, Private, Entity, Account, Client
from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.http import JsonResponse
 
import json
import secrets
import traceback


# Create your views here.
def register(request):
    """
    Creeate an function for registering an user in databas
    :param request:
    :return:
    """

    context = {}
    try:
        if request.method == 'POST':
            username = request.POST.get('user_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone_number = request.POST.get('phone')
            menu1 = request.POST.get('menu1')
            ssn = request.POST.get('ssn')

            if User.objects.filter(username=username).exists():
                context['msg'] = 'Sorry, this username already exists'
                return render(request, 'accounts/base/register.html', context)

            if User.objects.filter(email=email).exists():
                context['msg'] = 'Sorry, this email already exists'
                return render(request, 'accounts/base/register.html', context)

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.is_active = False
            user_obj.save()

            if menu1 == 'Private_Investor':
                legal_name = request.POST.get('legal_name')
                address = request.POST.get('address')
                region = request.POST.get('region')
                zipcode = int(request.POST.get('zipcode'))
                country = request.POST.get('e_country')
                city = request.POST.get('city')

                user = Private.objects.create(
                    user=user_obj,
                    legal_name=legal_name,
                    address=address,
                    region=region,
                    zip=zipcode,
                    country=country,
                    city=city
                )

            elif menu1 == 'Investing_via_entity':
                legal_name = request.POST.get('legal_investing')
                address = request.POST.get('entity_adress')
                region = request.POST.get('entity_region')
                zipcode = int(request.POST.get('entity_zip_Code'))
                countary = request.POST.get('entity_country')
                city = request.POST.get('entity_city')
                entity_type = request.POST.get('entity_type')

                user = Entity.objects.create(
                    user=user_obj,
                    legal_name=legal_name,
                    address=address,
                    region=region,
                    zip=zipcode,
                    country=countary,
                    city=city,
                    type=entity_type
                )

            account_type = request.POST.get('account_type')
            account_number = int(request.POST.get('account_number'))

            swiftcode = request.POST.get('swiftcode')
            financial_account = request.POST.get('financial_account')
            notes = request.POST.get('notes')

            if Account.objects.filter(account_number=account_number).exists():
                context['msg'] = 'Account number must be unique, this account number already exists'
                return render(request, 'accounts/base/register.html', context)

            Account.objects.create(
                type=account_type,
                account_number=account_number,
                owner=user
            )

            user.swift_code = swiftcode
            user.bank_name = financial_account
            if ssn:
                user.SSN = ssn
            user.notes = notes
            user.phone_number = phone_number

            token = secrets.token_hex(20)
            user.token = token
            user.save()

            # Send activation email
            site_url = get_current_site(request)
            subject = 'Activate Your Account'
            message = "cc"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            html_message = render_to_string('accounts/email/verified.html',
                                            {'username': user_obj.username, 'email': email,
                                             'token': token, 'site_url': site_url})
            send_mail(subject, message, f'Solomartel Holdings<{email_from}', recipient_list, html_message=html_message,
                      fail_silently=False)

            messages.success(request,
                             'Thank you for your registration! Your account has been successfully created. An email has been sent to you with detailed instructions on how to activate it')
            return redirect('accounts:register')

        return render(request, 'accounts/base/register.html')
    except:
        traceback.print_exc()
        messages.error(request, 'Something went wrong, please try again later')
        return render(request, 'accounts/base/register.html', context)


def activate_account(request):
    try:
        token = request.GET.get('token')
        email = request.GET.get('email')
        try:
            user = User.objects.get(email=email)

            client = Client.objects.get(user=user)
            # print("user_info", user_info)
            # user_saved_token = user_info[0].token
            # print(user_saved_token)
            if client.token == token:
                client.user.is_active = True
                client.user.save()
                messages.success(request, 'You have successfully confirmed your account, Please Login Here')

                return redirect(reverse('accounts:login'))
            else:
                messages.error(request, 'Invalid Token, please try again')
                return redirect(reverse('accounts:login'))
        except User.DoesNotExist:
            messages.error(request, "Invalid email address, please try again")
            return redirect(reverse('accounts:login'))
        except Client.DoesNotExist:
            messages.error(request, "You are not client in our website, please try again")
            return redirect(reverse('accounts:login'))
        except Exception as e:
            messages.error(request, str(e))
            return redirect(reverse('accounts:login'))
    except:
        messages.error(request, "Something went wrong, please try again")
        return redirect(reverse('accounts:login'))


def login(request):
    """
    Make a function for login an user account
    :param
    request:
    :return:
    """
    context = {}
    if not request.user.is_authenticated:
        try:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                if User.objects.filter(username = username).exists() or User.objects.filter(email = username).exists():
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        if user.is_active:
                            login_user(request, user)
                            return redirect(reverse('base:home'))
                        else:
                            context['msg'] = 'Sorry, you have not confirmed your account, check your mail'
                            return render(request, 'accounts/base/login.html', context)
                    else:
                        context['msg'] = 'Incorrect Password. Please introduce correct password or check instructions below'
                        return render(request, 'accounts/base/login.html', context)
                else:
                    context['msg'] = 'This user does not exists. Please try login with an existing User.'
                    return render(request, 'accounts/base/login.html', context)                    

            return render(request, 'accounts/base/login.html', context)
        except:
            traceback.print_exc()
#            context['msg'] = 'Something went wrong, Please try again later'
            return render(request, 'accounts/base/login.html', context)
    else:
        return redirect(reverse('base:home'))


def logout(request):
    logout_user(request)
    return redirect(reverse('base:home'))


def forgot_password(request):
    """
    call a function when user will lost his password
    :param request:
    :return:
    """
    context = {}

    try:
        if request.method == 'POST':
            site_url = get_current_site(request)
            site_url = str(site_url)
            email = request.POST.get('email')

            try:
                user = User.objects.get(email=email)
                subject = "Solomartel: Forgotten password"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                message = ''
                html_message = render_to_string('accounts/email/forget_email.html',
                                                {'user_info': user, 'email': email
                                                    , 'site_url': site_url})
                send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                          html_message=html_message, fail_silently=False)
                context['msg'] = "You will receive an email with the instructions to reset you password."
                context['success'] = True

            except User.DoesNotExist:
                context[
                    'msg'] = 'No user account registered with provided information. Please check your details and try again'
        return render(request, 'accounts/base/forgot.html', context)

    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong, please try again later'
        return render(request, 'accounts/base/forgot.html', context)


def reset_password(request):
    context = {}
    try:
        email = request.GET.get('q')
        user = User.objects.get(email=email)
        if request.method == 'POST':
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect(reverse('accounts:login'))

        context['success'] = True
        context['email'] = email
        return render(request, 'accounts/base/reset_password.html', context)
    except User.DoesNotExist:
        context['msg'] = 'Unrecognize email user'
        return render(request, 'accounts/base/reset_password.html', context)
    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong, Please try again later'
        return render(request, 'accounts/base/reset_password.html', context)


def home_mail_sending(request):
    try:
        context = {}
        if request.method == 'POST':
            site_url = get_current_site(request)
            site_url = str(site_url)
            email = request.POST.get('EMAIL')
            subject = "Solomartel: Please Confirm Subscription"
            message = ""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            msg_html = render_to_string('email/promtion_email.html',
                                        {'email': email, 'site_url': site_url})
            send_mail(subject, message, f'Solomartel Holdings<{email_from}>', recipient_list,
                      html_message=msg_html, fail_silently=False, )

        return render(request, 'email/promtion_email.html', context)

    except:
        context = {}
        traceback.print_exc()
        context['msg'] = 'Something went wrong, Please try again later'
        return render(request, 'email/promtion_email.html', context)


@login_required
def user_profile(request):
    try:
        client = Client.objects.get(user_id=request.user.id)
        context = {'user_obj': client}
        return render(request, 'accounts/base/user_profile.html', context)
    except:
        traceback.print_exc()
        return render(request, 'accounts/base/user_profile.html')


@login_required
def update_personal_data(request):
    context = {}
    try:
        if request.method == 'POST':
            hidden_value = request.user.id
            user_obj = User.objects.get(id=hidden_value)
            legal_name = request.POST.get('legal_name')
            user_name = request.POST.get('user_name')
            ssn = request.POST.get('ssn')
            mobile = request.POST.get('mobile')
            user_check = User.objects.filter(username=user_name).exclude(username=user_obj.username)
            if user_check:
                context['status'] = 'fail'
                context['msg'] = 'Sorry, Username is already exists'
                return HttpResponse(json.dumps(context))

            User.objects.filter(id=hidden_value).update(username=user_name)

            client = Client.objects.get(user=user_obj)
            client.legal_name = legal_name
            client.ABA_number = ssn
            client.phone_number = mobile
            client.save()

            # client_obj = Client.objects.get(user=user_obj)
            context['status'] = 'success'
            context['msg'] = 'Your Profile is Updated Successfully'
            return HttpResponse(json.dumps(context))
    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong, Please try again or contact us later'
        context['status'] = 'fail'
        return HttpResponse(json.dumps(context))


@login_required
def update_address_data(request):
    context = {}
    try:
        if request.method == 'POST':
            hidden_value = request.user.id
            user_obj = User.objects.get(id=hidden_value)
            address = request.POST.get('address')
            city = request.POST.get('city')
            region = request.POST.get('region')
            zipcode = request.POST.get('zipcode')

            client = Client.objects.get(user=user_obj)
            client.address = address
            client.city = city
            client.region = region
            client.zip = zipcode
            client.save()

            context['status'] = 'success'
            context['msg'] = 'Your Profile is Updated Successfully'
            return HttpResponse(json.dumps(context))
    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong, Please try again or contact us later'
        context['status'] = 'fail'
        return HttpResponse(json.dumps(context))


@login_required
def update_bank_data(request):
    context = {}
    try:
        if request.method == 'POST':
            hidden_value = request.user.id

            user_obj = User.objects.get(id=hidden_value)
            titlefield = request.POST.get('titlefield')
            acc_number = request.POST.get('acc_number')
            swift_code = request.POST.get('swift_code')
            financial = request.POST.get('financial')

            client = Client.objects.get(user=user_obj)
            client.bank_name = financial
            client.swift_code = swift_code
            client.account_type = titlefield
            client.my_accounts.all()[0].account_number = acc_number
            client.save()
            client.my_accounts.all()[0].save()

            context['status'] = 'success'
            context['msg'] = 'Your Profile is Updated Successfully'
            return HttpResponse(json.dumps(context))
    except:
        traceback.print_exc()
        context['msg'] = 'Something went wrong, Please try again or contact us later'
        context['status'] = 'fail'
        return HttpResponse(json.dumps(context))


@login_required
def change_password(request):
    context = {}
    try:
        user_id = request.user.id

        old_password = request.POST['old_psw']
        new_password = request.POST['nw_psw']
        user_obj = User.objects.get(id=user_id)
        old_password_is_matched = user_obj.check_password(f'{old_password}')
        new_password_different = user_obj.check_password(f'{new_password}')
        if old_password_is_matched:
            if not new_password_different:
                user_obj.set_password(new_password)
                user_obj.save()
                logout_user(request)
                context['status'] = 'success'
                messages.success(request, 'Success! Your Password has been changed!,Please login here')
            else:
                context['msg'] = 'Your new password must be different!'
                context['status'] = 'fail'
        else:
            context['status'] = 'fail'
            context['msg'] = 'The old password you have entered is incorrect!'

        return HttpResponse(json.dumps(context))
    except:
        context['msg'] = 'Something went wrong'
        context['status'] = 'fail'
        return HttpResponse(json.dumps(context))

def check_user_name(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        user_name = request.GET.get("user_name", None)
        # check for the nick name in the database.
        if User.objects.filter(username = user_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)

def check_email_user(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        email_user = request.GET.get("email_user", None)
        # check for the nick name in the database.
        if User.objects.filter(email = email_user).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)