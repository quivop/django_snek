from django.shortcuts import render
from django.http import HttpResponse

# My first view~

def index(request):
	return HttpResponse("Hello, wold. You're at the fic index.")
