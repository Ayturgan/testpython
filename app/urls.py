from django.urls import path
from . import views

urlpatterns = [
    path('notifications-test/', views.notifications_test, name='notifications_test'),
]
