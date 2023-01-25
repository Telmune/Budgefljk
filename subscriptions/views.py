from django.shortcuts import render
from rest_framework import generics

from subscriptions.models import Subscription
from subscriptions.serializer import SubscriptionSerializer


class SubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriprionListView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
