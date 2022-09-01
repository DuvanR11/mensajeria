from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.forms import Costumerform
from .models import Costumer
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

# =======================FRONTEND=============================

# Funcion para ir a la pagina principal (frontend)
def home(request):
    return render(request, 'home.html')

def send_message(request):
    if request.method == "POST":
        form = Costumerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado')
            return HttpResponseRedirect('/admin')
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = Costumerform()
    return render(request, 'home.html', {'form': form})

# =======================BACKEND=============================
 
# Funcion de login
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

# Funcion para retornar pagina de inbox
def inbox(request):
    return render(request, 'inbox.html')
