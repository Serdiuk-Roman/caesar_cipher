from django.shortcuts import render
from django.http import HttpResponse

def coder(request):
    return HttpResponse('<h1><a href="/dw/">dw</a> або <a href="/lit/">lit</a></h1>')

def first_page(request):
    return render(request, 'fp/base.html', {})