from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'cashflow/index.html')

def show_user(request, user_id):
    user=User.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'cashflow/user.html', context)