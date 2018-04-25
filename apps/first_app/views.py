from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from models import User, UserManager
import bcrypt
from .models import *
  # the index function is called when root is visited
def index(request):
  return render(request, 'first_app/index.html')

def register(request):
  errors = User.objects.nameValidator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
      request.session['first_name'] = request.POST['first_name']
      request.session['last_name'] = request.POST['last_name']
      request.session['email'] = request.POST['email']
      return redirect('/')
  else:
    pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pwhash)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    return redirect('/success')

def login(request):
  errors = User.objects.loginValidator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/')
  else:
    request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
    request.session['last_name'] = User.objects.get(email=request.POST['email']).last_name
    return redirect('/success')
  

def success(request):
  return render(request, 'first_app/success.html')
