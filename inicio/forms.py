from django import forms

class CrearFutbolistaFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    posicion=forms.CharField(max_length=20)
    
class BuscarFutbolista(forms.Form):
    nombre=forms.CharField(max_length=30, required=False)
    
class CrearBasquetbolistaFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    posicion=forms.CharField(max_length=20)
    
class BuscarBasquetbolista(forms.Form):
    nombre=forms.CharField(max_length=30, required=False)

class CrearTenistaFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    ranking=forms.CharField(max_length=20)
    
class BuscarTenista(forms.Form):
    nombre=forms.CharField(max_length=30, required=False)
        
    