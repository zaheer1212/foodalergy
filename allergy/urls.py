"""allergy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

admin.site.site_header = settings.ADMIN_SITE_HEADER

from userprofile import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html')),
    # url(r'^termsandconditions/$', TemplateView.as_view(template_name='legal.html')),
    # url(r'^$', blogviews.home, name='home'),
    # url(r'^blog/(?P<entry_slug>[\w.@+-]+)/$', blogviews.entrydetail, name='entrydetail'),
    # url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^all_products/$', views.all_products, name='all_products'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^category/', include('products.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login_user/$', views.login_user, name='login'),
    url(r'^update/$', views.update, name='update'),
    url(r'^update_password/$', views.update_password, name='update_password'),
    url(r'^update_forgot_password/$', views.update_forgot_password, name='update_forgot_password'),
    url(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
    url(r'^verify_email/$', views.verify_email, name='verify_email'),
    url(r'^confirm_code/$', views.confirm_code, name='confirm_code'),
    url(r'^featured/$', views.featured, name='featured'),
    url(r'^favorite_products/$', views.favorite_products, name='favorite_products'),
    url(r'^remove_favorite/$', views.remove_favorite, name='remove_favorite'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^search/$', views.search, name='search'),
    url(r'^accounts/', include('django.contrib.auth.urls'))

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
