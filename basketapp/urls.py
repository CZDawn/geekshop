import basketapp.views as basketapp
from django.urls import path

app_name = 'basketapp'

urlpatterns = [
    path(r'^$', basketapp.basket, name='view'),
    path(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    path(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),
    path(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.basket_edit, name='edit'),
]
