from django.urls import path

from user import views

urlpatterns = [
    path('', views.user_signup, name="user_create"),
    path('emailvalidation', views.email_validation, name="email_validation"),
    path('verify/<int:pk>/<str:token>/', views.verify_email, name='verify_email'),
]