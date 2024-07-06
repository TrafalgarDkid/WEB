from django.shortcuts import render
from .models import Plan, Usuario
# Create your views here.
def menu(request):
    context = {}
    return render(request,"pages/menu.html", context)

def planes(request):
    planes = Plan.objects.all()
    context = {
        'planes' : planes
    }
    return render(request,"pages/planes.html", context)

def nosotros(request):
    context = {}
    return render(request,"pages/nosotros.html", context)

def contacto(request):
    context = {}
    return render(request,"pages/contacto.html", context)

def sesion(request):
    context = {}
    return render(request,"pages/sesion.html", context)

def registrarse(request):

    if request.method != "POST":
        context = {}
        return render(request,"pages/registrarse.html", context)        

    else:

        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        contrasena = request.POST.get('contrasena')
        

        obj = Usuario.objects.create(

            email = email,
            nombre = nombre,
            apellido = apellido,
            contrasena = contrasena,
            
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request,"pages/registrarse.html", context)



    

def carrito(request,pk):
    plan = Plan.objects.get(id_plan = pk)
    context = {
        'plan' : plan
    }
    return render(request,"pages/carrito.html", context)

def formPlanes(request):

    if request.method != "POST":
        context = {}
        return render(request, "pages/formPlan.html", context)        

    else:

        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        descripcion2 = request.POST.get('descripcion2')
        precio = request.POST.get('precio')
        duracion = request.POST.get('duracion')
        incluye = request.POST.get('incluye')
        imagen = request.POST.get('incluye')
        

        obj = Plan.objects.create(

            titulo = titulo,
            descripcion = descripcion,
            descripcion2 = descripcion2,
            precio = precio,
            duracion = duracion,
            incluye = incluye,
            imagen = imagen,
            

        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/formPlan.html", context)
    
def crudPlanes(request):
    planes = Plan.objects.all()
    context = {
        'planes' : planes
    }
    return render(request,"pages/crudPlanes.html", context)

def modificarPlan(request, pk):

    plan = Plan.objects.get(id_plan = pk)
    context = {
        'plan' : plan
    }
    return render(request, "pages/modificarPlan.html", context)

def eliminarPlan(request, pk):
    try:
        plan = Plan.objects.get(id_plan = pk)
        plan.delete()
        planes = Plan.objects.all()
        context = {
            'mensaje' : "Plan eliminado",
            'planes': planes, 
        }
        return render(request, "pages/crudPlanes.html", context)

    except:
        planes = Plan.objects.all()
        context = {
            'mensaje' : "Error al eliminar plan",
            'planes': planes, 
        }
        
        return render(request, "pages/crudPlanes.html", context)