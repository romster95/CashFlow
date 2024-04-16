from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'cashflow/index.html')

def show_user(request, user_id):
    user=User.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'cashflow/user.html', context)

def show_income(request):
    return HttpResponse('Надходження')

def show_expenses(request):
    return HttpResponse('Витрати')

