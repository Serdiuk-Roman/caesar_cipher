from django.shortcuts import render

def coder(request):
    return render(request, 'coder_page/base.html', {})
