from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from userprofile.forms import SignUpForm, UpDateForm
from products.models import Allergy
import sqlite3
from products.models import Featured
from products.models import *
import json
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import EmailMessage
import datetime
from datetime import timedelta

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verify_user = User.objects.filter(username=username)
        verify_email = User.objects.filter(email=email)
        if verify_user:
            return render(request, 'signup.html', {'error': 'UserName Already Exists..'})
        elif verify_email:
            return render(request, 'signup.html', {'error': 'Email Already Exists..'})
        else:
            user = User(username=username, email=email, password=password)
            user.save()
            return redirect('/login_user/')
    else:
        return render(request, 'signup.html')


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password) | \
               User.objects.filter(email=username, password=password)
        if user:
            for us in user:
                if us.is_active:
                    request.session['username'] = us.username
                    login(request, us)
                    return HttpResponseRedirect('/')
        else:
            msg = 'Username or Password is wrong.'
            context = {'error': msg}
            return render(request, 'login.html', context)

    return render(request, 'login.html', )


def logout_view(request):
    logout(request)
    del request.session['username']
    return redirect('home')


def update(request):
    if request.method == 'POST':
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if password != '' and first_name != '' and last_name != '':
            query = User.objects.filter(username=request.session['username']).update(password=password,
                                                                                     first_name=first_name,
                                                                                     last_name=last_name)
            return redirect('/')
    else:
        # defaults = {
        #             'username': request.user.username,
        #             'email': request.user.email,
        #         }
        # if request.user.profile.userAllergies:
        #     defaults['allergies'] = [t.pk for t in request.user.profile.userAllergies.all()]
        #     print (defaults)
        # form = UpDateForm(defaults, instance=request.user)
        return render(request, 'update.html', )


def update_forgot_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        if password != '':
            query = User.objects.filter(email=email).update(password=password)
            return JsonResponse({'status': 'pass', 'message': 'Password Update'})
    else:
        return JsonResponse({'status': 'Fail', 'message': 'Some Error Occured'})


def update_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        if password != '':
            query = User.objects.filter(username=request.session['username']).update(password=password)
            return redirect('/')
    else:
        return render(request, 'password.html', )


def forgot_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        if password != '':
            query = User.objects.filter(username=request.session['username']).update(password=password)
            return redirect('/')
    else:
        return render(request, 'forgot_password.html', )


def featured(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        check_favorite = Featured.objects.filter(username=request.session['username'], product_id=product_id)
        if check_favorite:
            return JsonResponse({'success': True, 'message': 'Product Already in Your Favorite List'})
        else:
            feature = Featured(product_id=product_id, username=request.session['username'])
            feature.save()
            return JsonResponse({'success': True, 'message': 'Product Added Successfully..'})


def favorite_products(request):
    products = []
    if request.session['username'] != '':
        favourite = []
        favorites = Featured.objects.filter(username=request.session['username'])
        for fv in favorites:
            favourite.append(int(fv.product_id))
    favroties = Featured.objects.filter(username=request.session['username'])
    for item in favroties:
        productss = Product.objects.filter(productId=item.product_id)
        for p in productss:
            products.append(p)
    context = {'products': products, 'favourites': favourite}
    return render(request, 'favorite_items.html', context)


def remove_favorite(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        remove_favorites = Featured.objects.filter(username=request.session['username'], product_id=product_id)
        remove_favorites.delete()
        return JsonResponse({'success': True, 'message': 'Product Deleted Successfully..'})


def home(request):
    from django.core.paginator import Paginator
    if request.method == 'GET':
        category = Category.objects.all()
        all_products = Product.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(all_products, 25)  # Show 25 contacts per page
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        if request.user.is_authenticated:
            favourite = []
            favorites = Featured.objects.filter(username=request.session['username'])
            for fv in favorites:
                favourite.append(int(fv.product_id))
            context = {'products': products, 'favourites': favourite}
        else:
            context = {'products': products, }

        # page = request.GET.get('page')
        #
        # products = paginator.get_page(page)

        return render(request, 'home.html', context)


def search(request):
    if request.method == 'GET':
        if request.GET['search_option'] == 'category':
            category = Category.objects.filter(categoryName__contains=request.GET['search_value'])
            product = Product.objects.filter(productCategory=category).order_by('productName')
        if request.GET['search_option'] == 'product':
            product = Product.objects.filter(productName__contains=request.GET['search_value'])
            print('=================')
            print(product)
            print('=================')
        if request.GET['search_option'] == 'allergy':
            alergy = Allergy.objects.filter(allergyName=request.GET['search_value'])[0]
            product = Product.objects.filter(productAllergies=alergy.allergyId)
        products = []
        for p in product:
            products.append(p)
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 25)  # Show 25 contacts per page
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'products': products}
    return render(request, 'search.html', context)


def verify_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        verify_email = User.objects.filter(email=email)
        if verify_email:
            import random
            num = random.randint(0, 99999)
            number = str(num)
            add_code = VerificationCode(email=email, code=number, used=False)
            add_code.save()
            send_email = EmailMessage('Reset Password Code', "Here is your code for password reset "
                                                             "please enter this code in within 5 minutes"+number,
                                 to=['wdeveloper12@gmail.com'])
            send_email.send()
            return JsonResponse({'status': 'pass', 'message': 'Code Sent on Email: ' + email})
        else:
            return JsonResponse({'status': 'Fail', 'message': 'Wrong Email User does not Exist'})


def confirm_code(request):
    if request.method == 'POST':
        email = request.POST['email']
        code = request.POST['code']
        verify_code = VerificationCode.objects.filter(email=email, code=code, used=False)
        current_time = datetime.datetime.now()
        if verify_code:
            for v in verify_code:
                time = v.created_at + timedelta(minutes=5)
                verify_time = time.time().strftime("%I:%M")
                if current_time.time().strftime("%I:%M") >= verify_time:
                    update_token = VerificationCode.objects.filter(code=code).update(used=True)
                    return JsonResponse({'status': 'Fail', 'message': 'Token Expired'})
                else:
                    update_token = VerificationCode.objects.filter(code=code).update(used=True)
                    return JsonResponse({'status': 'pass', 'message': 'Token Verified'})
        else:
            return JsonResponse({'status': 'Fail', 'message': 'Token is not right'})