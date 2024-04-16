from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import User


# Create your views here.
@csrf_exempt
def create_account(request):
    if request.method == 'POST':
        data = request.body
        # user = User.objects.create_user(email=request.body., name=data['name'],
        #                                 password=data['password'], username=data['username'])
        return HttpResponse(request.body)
