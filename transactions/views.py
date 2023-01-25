from django.shortcuts import render
from rest_framework import generics

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionRetrieveView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer