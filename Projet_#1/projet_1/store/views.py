from django.shortcuts import render
from django.http import HttpResponse
from .models import CONTRACTS

# Create your views here.

def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def contracts(request):
    contracts = ["<li>{}</li>".format(contract['name']) for contract in CONTRACTS]
    message = """<ul>{}</ul>""".format("\n".join(contracts))
    return HttpResponse(message)