from django.contrib import admin
from django.urls import path, include

from cashflow.views import index, show_income, show_expenses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cashflow.urls')),
    path('incomes/', show_income, name='incomes'),  # Додайте відповідну функцію представлення incomes_view
    path('expenses/', show_expenses, name='expenses')  # Додайте відповідну функцію представлення expenses_view
]
