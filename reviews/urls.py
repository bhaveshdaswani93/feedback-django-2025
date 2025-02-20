from django.urls import path

from . import views

urlpatterns = [
   path('', views.reviews),
   path('thank_you', views.thank_you)
  ]