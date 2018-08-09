from django.conf.urls import url

from products import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^(?P<cat_slug>[\w.@+-]+)/$', views.category, name="category"),

]