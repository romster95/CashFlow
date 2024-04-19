from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request, user_id):
    user = User.objects.get(pk=user_id)
    income = Income.objects.filter(user=user_id).order_by('-date')
    context = {
        'user': user,
        'incomes': income
    }
    return render(request, 'cashflow/index.html', context)
