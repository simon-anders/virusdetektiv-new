from django.shortcuts import render, redirect
from django import forms
from .models import *

def index(request):
    return render(request, 'index.html')

def token(request):
    if request.method != "POST":
        raise Exception("URL only for POST request.")
    token_code = request.POST["token"]
    token = Token.objects.filter(code=token_code).first()
    if token is None:
        return render(request, 'message.html', {'msg': "Ungültiger Bestell-Code"})
    if token.used:
        return render(request, 'message.html', {'msg': "Bestell-Code bereits entwertet."})

    request.session['token_code'] = token_code
    return redirect( order )

# AgeGroups = [
#     ("adult", "Erwachsene(r) (min. 18 Jahre)"),
#     ("adolescent", "Jugendliche(r) (12-17 Jahre)" ),
#     ("child", "Kind (7-11 Jahre)"),
#     ("too_young", "Kleinkind (unter 7 Jahre)") ]
#
# class OrderFormLine(forms.Form):
#     name = forms.CharField()
#     agegroup = forms.ChoiceField(choices=AgeGroups)
#     phone = forms.CharField()

def order(request):
    if request.method == "POST":
        pass
    return render(request, 'order.html', {'range':range(3)})
