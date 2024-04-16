from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'cashflow/index.html')

def show_user(request, user_id):
    user=User.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'cashflow/user.html', context)

def show_income(request, user_id, amount=55):
    income=Income.objects.filter(user=user_id).order_by('date')
    return render(request,'cashflow/incomes.html',{'amount':amount})




def show_expenses(request):
    return HttpResponse('Витрати')

