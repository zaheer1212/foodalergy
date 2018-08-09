from django.shortcuts import render

from products.models import Product, Category, Featured
from userprofile.models import Profile
from django.contrib.auth.models import User

def category(request, cat_slug):

    category = Category.objects.get(categorySlug=cat_slug)
    productss = Product.objects.filter(productCategory=category).order_by('productName')
    if request.user.is_active:
        favourite = []
        favorites = Featured.objects.filter(username=request.session['username'])
        for fv in favorites:
            favourite.append(int(fv.product_id))
        products = []
        for p in productss:
            products.append(p)
        context = {'products': products, 'category': category, 'favourites': favourite}
        return render(request, 'category.html', context)
    else:
        products = []
        for p in productss:
            products.append(p)

        context = {'products': products, 'category': category}
        return render(request, 'category.html', context)
    # try:
        # ua = Profile.objects.get(user=request.user)

        # for p in products:
        #     p.ok = True
        #     for pa in p.productAllergies.all():
        #         if pa in ua.userAllergies.all():
        #             p.ok = False
        #
        # p2 = products.filter(ok=True)
        # print('=========== IN TRY ================')
        # context = {'products': p2, 'category': category}
    #
    # except:
    #     print('=========== IN EXcept ================')
    #     context = {'products': products, 'category': category}

    # context = { 'products':products, 'category':category }


