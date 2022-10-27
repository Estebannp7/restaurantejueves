from django import forms


class FormularioPlatos(forms.Form):
    ##CREANDO ATRIBUTO PARA CARGAR EL SELECTOR
    
    OPCIONES=(
        (1,'Mesero'),
        (2,'Cocinero'),
        (3,'Cajero')
    )
    
    
    
    ##DENTRO DE LA CLASE CADA ATRIBUTO SERA UN INPUT 
    nombrePersonal= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=5
    )
    
    descripcionPlato= forms.CharField(
           widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required= True,
        max_length=20
        
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