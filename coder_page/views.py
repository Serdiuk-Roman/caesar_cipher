import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

def coder(request):
    return render(request, 'coder_page/base.html', {})

def caesar_cipher(request):
    if request.method == "POST":
        
        objs = json.loads(request.body.decode("utf-8"))
        text = objs.get('text')
        step = int(objs.get('step'))
        
        result = ""
        advice = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        counter_list = []
        
        #text analysis Caesar cipher
        for i in text:
            if i.isalpha():
                if i.isupper():
                    numb_ascii = ord("A") + (((ord(i)-ord("A"))+step)%26)
                    result = result + chr(numb_ascii)
                else:
                    numb_ascii = ord("a") + (((ord(i)-ord("a"))+step)%26)
                    result = result + chr(numb_ascii)
            else:
                result = result + i
        
        #search most used letter
        for k in alphabet:
            counter = text.count(k) + text.count(k.upper())
            counter_list.append(counter)
        x = counter_list.index(max(counter_list))
        
        #step define
        if ord("a") + x > ord("e"):
            advice_step = ord("a") + x - ord("e")
        else:
            advice_step = 26 + x + ord("a")  - ord("e")
        
        advice = str(advice_step)

        data = {"cipher_text": result, "advice": advice, "counter_list": counter_list}

        return JsonResponse(data)
