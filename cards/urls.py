from django.urls import path
from .views import BankCardRetrieveView, BankCardListView, GoalRetrieveView, GoalListView

urlpatterns = [
    path(r'bankcard/', BankCardListView.as_view()),
    path(r'bankcard/<int:pk>/', BankCardRetrieveView.as_view()),
    path(r'goal/', GoalListView.as_view()),
    path(r'goal/<int:pk/',GoalRetrieveView.as_view())
]
