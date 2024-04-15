from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('user/<int:user_id>', show_user, name='user')

]