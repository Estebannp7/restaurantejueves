from django.shortcuts import render,redirect
from web.formularios.formularioPersonas import FormularioPersonas

###IMPORTAR EL FORMULARIO A RENDERIZAR
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos

from web.models import Platos
from web.models import Empleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):
    
    platosConsultados = Platos.objects.all()
    
    formulario = FormularioEdicionPlatos()
    diccionarioEnvio={
        'platos':platosConsultados,
        'formulario': formulario
    }
    
    return render(request,'menuPlatos.html',diccionarioEnvio)


def EditarPlato(request,id):
    #recibir los datos del formulario y editar mi plato
     if request.method =='POST':
        datosDelFormulario = FormularioEdicionPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato = datosDelFormulario.cleaned_data
            try:
                    Platos.objects.filter(pk=id).update(precio=datosPlato["precioplato"])
                    print("EXITO GUARDANDO LOS DATOS")
                    
                
            except Exception as error:  
                  
                    print("error", error)       
            return redirect('menu') 


def MenuPersonas(request):
    
    personasConsultados = Empleados.objects.all()
    
    diccionarioEnvio={
        'empleados':personasConsultados
    }
    
    return render(request,'menuEmpleados.html',diccionarioEnvio)


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
    datosParaTemplate1 = {
        'formularioPersonas': formulario,
        'bandera': False
    }
    
    #PREGUNTAMOS SI EXSITE ALGUNA PETICION DE TIPO POST
    if request.method =='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario1 = FormularioPersonas(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario1.is_valid():
            #capturamos la data
            datosPersona = datosDelFormulario1.cleaned_data
            #creamos un modelo de tipo ersonao
            personaNueva= Empleados(
                nombres =datosPersona["nombre"],
                apellidos =datosPersona["apellido"],
                foto=datosPersona["foto"],
                cargo= datosPersona["cargo"],
                salario=datosPersona["salario"],
                contacto=datosPersona["contacto"]
                
            )
            #Intentamos llevar el objeto platoNuevo a LA BD
            try:
                    personaNueva.save()
                    datosParaTemplate1["bandera"] = True
                    print("EXITO GUARDANDO LOS DATOS")
                    
                
            except Exception as error:  
                    datosParaTemplate1["bandera"] = False
                    print("error", error)        
    
    
    
    
    
    return render(request,'personal.html',datosParaTemplate1)