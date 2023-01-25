from django.shortcuts import render
from rest_framework import generics

from cards.models import BankCard, Goal
from cards.serializer import BankCardSerializer, GoalSerializer


class BankCardRetrieveView (generics.RetrieveAPIView):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer

class BankCardListView (generics.ListCreateAPIView):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer

class GoalRetrieveView (generics.RetrieveAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalListView (generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

