from django.urls import path

from time_wizard import views

urlpatterns = [
    path('load-holidays', views.load_holidays, name='ajax-load-holidays'),
]
