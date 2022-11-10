
from django import forms


class FormularioPersonas(forms.Form):
    ##CREANDO ATRIBUTO PARA CARGAR EL SELECTOR
    
    OPCIONES=(
        (1,'Cocinero'),
        (2,'Ayudante'),
        (3,'Mesero'),
        (4, 'Administrador')
    )
    
    
    
    ##DENTRO DE LA CLASE CADA ATRIBUTO SERA UN INPUT 
    nombre= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=50
    )
    
    apellido= forms.CharField(
           widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=200
        
    )
    
    foto = forms.CharField(
           widget=forms.TextInput(
            attrs={'class':'form-control mb-3'}),
        required= True,     
    )
    
    
    Cargo = forms.ChoiceField(
           widget=forms.Select(
            attrs={'class':'form-control mb-3'}),
        required= True,
        choices= OPCIONES
    )
    
    
    
    
    Salario = forms.CharField(
        widget= forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=50
        
        
    )
    
    Contacto = forms.CharField(
        widget= forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=50
        
        
    )