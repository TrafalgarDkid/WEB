from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('Planes', views.planes, name='planes'),
    path('Nosotros', views.nosotros, name='nosotros'),
    path('Contacto', views.contacto, name='contacto'),
    path('Sesion', views.sesion, name='sesion'),
    path('Registrarse', views.registrarse, name='registrarse'),
    path('Carrito/<str:pk>', views.carrito, name='carrito'),
    path('AgregarPLan', views.formPlanes, name='agregarPlan'),
    path('CrudPlanes', views.crudPlanes, name='crudPlanes'),
    path('ModificarPlan/<str:pk>', views.modificarPlan, name='modificaPlan'),
    path('EliminarPlan/<str:pk>', views.eliminarPlan, name='eliminarPlan'),
]