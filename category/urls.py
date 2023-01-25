from django.urls import path
from rest_framework import routers
from .views import CategoryListView, CategoryRetrieveView

urlpatterns = [
    path(r'categories/', CategoryListView.as_view()),
    path(r'categories/<int:pk>/', CategoryRetrieveView.as_view()),

]
