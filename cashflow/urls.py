from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('user/<int:user_id>', show_user, name='user'),
    path('incomes/', show_income, name='incomes'),
    path('expenses/', show_expenses, name='expenses')
]