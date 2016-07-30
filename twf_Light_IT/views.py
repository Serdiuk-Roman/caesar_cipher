from django.http import HttpResponse

def first_page(request):
    return HttpResponse('<h1><a href="/dw/">dw</a> або <a href="/lit/">lit</a></h1>')
