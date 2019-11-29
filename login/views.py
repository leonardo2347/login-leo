from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def login_list(request):
    if request.method == 'POST':
     
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.add_message(request, messages.INFO, 'Seja bem vindo!')
            return redirect('/login/home/')
          
        else:
            # Return an 'invalid login' error message.
            messages.add_message(request, messages.ERROR, 'Login faciled! ID de e-mail ou senha inválida!')
            return render (request, 'login.html')
    else:
        return render(request,'login.html')


