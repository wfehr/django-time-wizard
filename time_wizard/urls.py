from django.conf.urls import url

from time_wizard import views

urlpatterns = [
    url(r'^load-holidays', views.load_holidays, name='ajax-load-holidays'),
    url(r'^load-provinces', views.load_provinces, name='ajax-load-provinces'),
]
