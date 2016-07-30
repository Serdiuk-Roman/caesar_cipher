from django.http import HttpResponse

def first_page(request):
    return HttpResponse('<p><a href="/dw/">dw</a> або <a href="/lit/">lit</a></p>')
