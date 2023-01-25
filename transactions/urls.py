from django.urls import path


from transactions.views import TransactionListCreateView, TransactionRetrieveView

urlpatterns = [
    path(r'transactions/', TransactionListCreateView.as_view()),
    path(r'transactions/<int:pk>/', TransactionRetrieveView.as_view())
]