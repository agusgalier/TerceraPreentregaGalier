from django.shortcuts import render, redirect
from inicio.forms import CrearFutbolistaFormulario, BuscarFutbolista, CrearBasquetbolistaFormulario, BuscarBasquetbolista, CrearTenistaFormulario,BuscarTenista
from inicio.models import Futbolista, Basquetbolista, Tenista

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_futbolista(request):
    messages=''
    if request.method =='POST':
        formulario=CrearFutbolistaFormulario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            futbolista=Futbolista(nombre=info['nombre'],edad=info['edad'],posicion=info['posicion'])
            futbolista.save()
            # mensaje=f'Se creo el futbolista {futbolista.nombre}'
            messages=messages.success(request, 'El jugador se ha creado exitosamente.')
            return redirect('inicio:lista_futbolistas')
        else:
            # return render(request, 'inicio/crear_futbolista.html',{'formulario':formulario})
            return render(request, 'inicio/crear_futbolista.html',{'formulario':formulario})
    formulario=CrearFutbolistaFormulario()
    return render(request, 'inicio/crear_futbolista.html',{'formulario':formulario,'mensaje':messages})

def lista_futbolistas(request):
   formulario=BuscarFutbolista(request.GET)
   if formulario.is_valid():
       nombre_futbolista=formulario.cleaned_data['nombre']
       lista_futbolistas=Futbolista.objects.filter(nombre__icontains=nombre_futbolista)
   else:
       print('No es valido')
   formulario=BuscarFutbolista()    
   return render(request, 'inicio/lista_futbolistas.html',{'formulario':formulario,'futbolistas':lista_futbolistas}) 

def crear_basquetbolista(request):
    mensaje=''
    if request.method =='POST':
        formulario=CrearBasquetbolistaFormulario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            basquetbolista=Basquetbolista(nombre=info['nombre'],edad=info['edad'],posicion=info['posicion'])
            basquetbolista.save()
            mensaje=f'Se creo el basquetbolista {basquetbolista.nombre}'
            return redirect('inicio:lista_basquetbolistas')
        else:
            return render(request, 'inicio/crear_basquetbolista.html',{'formulario':formulario})
    formulario=CrearBasquetbolistaFormulario()
    return render(request, 'inicio/crear_basquetbolista.html',{'formulario':formulario,'mensaje':mensaje})

def lista_basquetbolistas(request):
   formulario=BuscarBasquetbolista(request.GET)
   if formulario.is_valid():
       nombre_basquetbolista=formulario.cleaned_data['nombre']
       lista_basquetbolistas=Basquetbolista.objects.filter(nombre__icontains=nombre_basquetbolista)
   else:
       print('No es valido')
   formulario=BuscarBasquetbolista()    
   return render(request, 'inicio/lista_basquetbolistas.html',{'formulario':formulario,'basquetbolistas':lista_basquetbolistas})
 
def crear_tenista(request):
    mensaje=''
    if request.method =='POST':
        formulario=CrearTenistaFormulario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            tenista=Tenista(nombre=info['nombre'],edad=info['edad'],ranking=info['ranking'])
            tenista.save()
            mensaje=f'Se creo el tenista {tenista.nombre}'
            return redirect('inicio:lista_tenistas')
        else:
            return render(request, 'inicio/crear_tenista.html',{'formulario':formulario})
    formulario=CrearTenistaFormulario()
    return render(request, 'inicio/crear_tenista.html',{'formulario':formulario,'mensaje':mensaje})

def lista_tenistas(request):
   formulario=BuscarTenista(request.GET)
   if formulario.is_valid():
       nombre_tenista=formulario.cleaned_data['nombre']
       lista_tenistas=Tenista.objects.filter(nombre__icontains=nombre_tenista)
   else:
       print('No es valido')
   formulario=BuscarBasquetbolista()    
   return render(request, 'inicio/lista_tenistas.html',{'formulario':formulario,'tenistas':lista_tenistas}) 
