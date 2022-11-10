from django.shortcuts import render
from web.formularios.formularioPersonas import FormularioPersonas

###IMPORTAR EL FORMULARIO A RENDERIZAR
from web.formularios.formularioPlatos import FormularioPlatos

from web.models import Platos
from web.models import Empleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def VistaPlatos(request):
    formulario = FormularioPlatos()
    datosParaTemplate = {
        'formularioRegistro': formulario,
        'bandera':False                   
                         }
    
    #PREGUNTAMOS SI EXSITE ALGUNA PETICION DE TIPO POST
    if request.method =='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario = FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato = datosDelFormulario.cleaned_data
            #creamos un modelo de tipo plato
            platoNuevo= Platos(
                nombre =datosPlato["nombrePlato"],
                descripcion =datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio= datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
                
            )
            #Intentamos llevar el objeto platoNuevo a LA BD
            try:
                    platoNuevo.save()
                    datosParaTemplate["bandera"] = True
                    print("EXITO GUARDANDO LOS DATOS")
                    
                
            except Exception as error:  
                    datosParaTemplate["bandera"] = False
                    print("error", error)        
    
    return render(request,'platos.html',datosParaTemplate)

def Personal(request):
    formulario = FormularioPersonas()
    datosParaTemplate = {
        'formularioPersonas': formulario
    }
    
    #PREGUNTAMOS SI EXSITE ALGUNA PETICION DE TIPO POST
    if request.method =='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario = FormularioPersonas(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPersona = datosDelFormulario.cleaned_data
            #creamos un modelo de tipo ersonao
            personaNueva= Empleados(
                nombre =datosPersona["nombre"],
                apellido =datosPersona["apellido"],
                foto=datosPersona["foto"],
                cargo= datosPersona["cargo"],
                salario=datosPersona["salario"],
                contacto=datosPersona["contacto"]
                
            )
            #Intentamos llevar el objeto platoNuevo a LA BD
            try:
                    personaNueva.save()
                    datosParaTemplate["bandera"] = True
                    print("EXITO GUARDANDO LOS DATOS")
                    
                
            except Exception as error:  
                    datosParaTemplate["bandera"] = False
                    print("error", error)        
    
    
    
    
    
    return render(request,'personal.html',datosParaTemplate)