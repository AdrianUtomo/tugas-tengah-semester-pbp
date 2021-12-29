from django.core import serializers

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

from beranda.models import Feedback
from .models import Feedback2
from .forms_login2 import CreateUserForm
import json


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def daftar(request):
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(json.loads(request.body))
#         form.cleaned_data['username'] = request.POST.get('username')
#         form.cleaned_data['email'] = request.POST.get('email')
#         form.cleaned_data['password1'] = request.POST.get('password1')
#         form.cleaned_data['password2'] = request.POST.get('password2')
        
        if form.is_valid():
            form.save()
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Sign Up!"
            }, status=200)
        else :
          return JsonResponse({
              "request" : form.errors,
              "status": False,
              "message": "Failed to Sign Up"
            }, status=401)
    else :
      return JsonResponse({
              "status": False,
              "message": "Failed to Sign Up"
            }, status=401)

def logoutFlutter(request) :
    logout(request.body)
    return JsonResponse({
              "status": True,
              "message": "Succes Logout"
            }, status=200)


@csrf_exempt

def json_fb(request) :
    data = serializers.serialize('json', Feedback.objects.all())
    return HttpResponse(data, content_type="application/json")
