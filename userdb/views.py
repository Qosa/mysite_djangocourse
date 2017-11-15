from django.shortcuts import render
from django.http import HttpResponse
from userdb.models import Users
from . import forms
from userdb.forms import FormModel
from django.core import validators

# Create your views here.
# ---------------->     TUTAJ OKRESLAMY CO BEDZIE WIDOCZNE NA STRONIE(W TYM PLIKU)      <---------------
def index(request): # W URLS.PY podajemy NAZWE FUNKCJI
    return HttpResponse("<h1 style='color:blue;font-family:arial;'>Welcome to Users page!</h1>")
def users(request):
    users_list = Users.objects.order_by('name')
    users_dict = {'users_records':users_list}
    return render(request, 'userdb/users.html',context=users_dict) #ZDEFINIOWANIE JAKA TRESC BEDZIE WIDOCZNA NA DANEJ TEMPLATCE
def form_name_view(request):
    form = FormModel()
    if request.method == 'POST': #aby pobrac dane obiektu trzeba sprawdzic metode (czy jest POST) oraz zwalidowac formularz - inaczej wystapi blad braku atrybutu !!!
        form = FormModel(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, 'userdb/form_name.html',{'form':form})



# 1. ZDEFINIOWANIE MODELU, TRESCI BADZ FORMULARZA (models, forms)
# 2. UTWORZENIE ODPOWIEDNIEJ FUNKCJI W PLIKU VIEWS.PY (OKRESLENIE TEMPLATKI ORAZ ZAWARTOSCI)
# 3. OKRESLENIE ADRESU POD JAKIM BEDZIE WIDOCZNA STRONA W PLIKU URLS.PY
# WALIDACJA FORMULARZY ROWNIEZ NASTEPUJE W PLIKU VIEWS