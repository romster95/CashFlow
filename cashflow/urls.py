from django.urls import path

from .views import *

urlpatterns = [
    path('<int:user_id>', index, name='home'),
]