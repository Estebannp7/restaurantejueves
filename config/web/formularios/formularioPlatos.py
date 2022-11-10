## LOS FORMULARIOS DE DJANGO SON CLASE 

from django import forms


class FormularioPlatos(forms.Form):
    ##CREANDO ATRIBUTO PARA CARGAR EL SELECTOR
    
    OPCIONES=(
        (1,'Entrada'),
        (2,'Plato fuerte'),
        (3,'Postre')
    )
    
    
    
    ##DENTRO DE LA CLASE CADA ATRIBUTO SERA UN INPUT 
    nombrePlato= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=20
    )
    
    descripcionPlato= forms.CharField(
           widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=50
        
    )
    
    fotoPlato = forms.CharField(
           widget=forms.TextInput(
            attrs={'class':'form-control mb-3'}),
        required= True,     
    )
    
    
    precioPlato = forms.CharField(
           widget=forms.NumberInput(
            attrs={'class':'form-control mb-3'}),
        required= True,
    )
    
    
    
    
    tipoPlato= forms.ChoiceField(
        widget= forms.Select(attrs={'class':'form-control mb-3'}),
        required= True,
        choices= OPCIONES
        
        
    )