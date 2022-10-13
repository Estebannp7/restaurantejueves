from django.shortcuts import render

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

