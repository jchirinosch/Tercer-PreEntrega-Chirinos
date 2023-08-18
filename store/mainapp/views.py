from django.shortcuts import render
from django.http import HttpResponse
#from .models import Guitarra, Bajo, Percusion, Sucursal
from .models import *
from .forms import *

def home(request):
    return render(request, 'mainapp/base.html')

def guitarras(request):
    contexto = {'guitarras': Guitarra.objects.all(), 'titulo':'Listado de Guitarras' }
    return render(request, 'mainapp/guitarras.html', contexto)

def bajos(request):
    contexto = {'bajos': Bajo.objects.all(), 'titulo':'Listado de Bajos' }
    return render(request, 'mainapp/bajos.html', contexto)

def percusion(request):
    contexto = {'percusion': Percusion.objects.all(), 'titulo':'Listado de Percusión' }
    return render(request, 'mainapp/percusion.html', contexto)

def sucursales(request):
    contexto = {'sucursales': Sucursal.objects.all(), 'titulo':'Listado de nuestras sucursales' }
    return render(request, 'mainapp/sucursales.html', contexto)

###### Forms

def guitarrasform(request):
    if request.method == 'POST':
        guitarra = Guitarra(marca=request.POST['marca'],
                            modelo=request.POST['modelo'],
                            origen=request.POST['origen'],
                            precio=request.POST['modelo'])
        guitarra.save()
        return HttpResponse('Se agrego el producto al listado de forma exitosa.')
    return render(request, 'mainapp/guitarrasForm.html')

def bajosform(request):
    if request.method == 'POST':
        bajos = bajos(marca=request.POST['marca'],
                      modelo=request.POST['modelo'],
                      origen=request.POST['origen'],
                      precio=request.POST['modelo'])
        bajos.save()
        return HttpResponse('Se agrego el producto al listado de forma exitosa.')
    return render(request, 'mainapp/bajosForm.html')

def percusionform(request):
    if request.method == 'POST':
        percusion = Percusion(marca=request.POST['marca'],
                            modelo=request.POST['modelo'],
                            origen=request.POST['origen'],
                            precio=request.POST['modelo'])
        percusion.save()
        return HttpResponse('Se agrego el producto al listado de forma exitosa.')
    return render(request, 'mainapp/percusionForm.html')


def buscarSucursal(request):
    return render(request, "mainapp/buscarSucursal.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        sucursales = Sucursal.objects.filter(nombre__icontains=patron)
        contexto = {'sucursales': sucursales} 
        return render(request, "mainapp/sucursales.html", contexto)
