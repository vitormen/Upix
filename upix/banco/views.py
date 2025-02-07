from django.shortcuts import render
from .models import ContaBancaria

# Create your views here.
def index(req):

    return render(req, 'index.html')

def cadastro_conta(req):

    return render(req, 'cadastro-conta.html')

def cadastro_pix(req):

    return render(req, 'cadastro-pix.html')

def listagem(req):
    
    return render(req, 'listagem.html')

