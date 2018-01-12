from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^menu/$', views.MenuCard.as_view()),
    url(r'^menu/(?P<pk>[0-9]+)/$', views.MenuUpdate.as_view()),
    url(r'^offer/$', views.offers),
    url(r'^booking/$', views.booking_list),
    url(r'^login/$', views.login),
    url(r'^feedback/$', views.Feedbacks.as_view()),
    # url(r'^customer/list$', views.CustomerList.as_view()),
    # url(r'^customer/new$', views.NewCustomer.as_view()),
    # url(r'^customer/(?P<pk>[0-9]+)/orders/$', views.CustomerOrderList.as_view()),
]
