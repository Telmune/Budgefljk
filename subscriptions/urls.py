from django.urls import path
from rest_framework import routers

from .models import Subscription

urlpatterns = [
    path(r'subscriptions/', Subscription.as_view()),
    path(r'subscriprions/<int:pk>/', Subscription.as_view()),

]
