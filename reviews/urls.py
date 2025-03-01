from django.urls import path

from . import views

urlpatterns = [
   path('', views.ReviewView.as_view()),
   path('thank_you', views.ThankYouView.as_view()),
   path('list', views.ReviewListView.as_view()),
   path('favorite', views.ReviewFavorite.as_view()),
   path('list/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
  ]