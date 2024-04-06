from django.urls import path
from AppLibreria.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("autor/", crear_autor, name="AutoresCrear"), #CRUD
    path("clientes/", crear_cliente, name="ClientesCrear"),#CRUD
    path("subgeneros/", crear_subgenero, name="SubgeneroCrear"),#CRUD
    path("buscar_cliente/", buscar_cliente, name="Buscar_cliente"),
    path("buscar_subgenero/", buscar_subgenero, name="Buscar_subgenero"),
    path("buscar_autor/", buscar_autor, name="Buscar_autor"),
    path ("about/", acerca_de_mi, name="Acerca de mi"),
    
    
    path("leerClientes/", leerClientes, name="ClientesLeer"), #CRUD
    path("eliminarCliente/<clienteNombre>/", eliminarCliente, name="ClienteEliminar"), #CRUD
    path("editarCliente/<clienteNombre>/", editarCliente, name="ClienteEditar"), #CRUD

    path("leerSubgeneros/", leerSubgeneros, name="SubgenerosLeer"), #CRUD
    path("eliminarSubgenero/<subgeneroNombre>/", eliminarSubgenero, name="SubgeneroEliminar"), #CRUD
    path("editarSubgenero/<subgeneroNombre>/", editarSubgenero, name="SubgenerosEditar"), #CRUD
    
    path("leerAutor/", leerAutor, name="AutoresLeer"), #CRUD
    path("eliminarAutor/<autorNombre>/", eliminarAutor, name="AutoresEliminar"), #CRUD
    path("editarAutor/<autorNombre>/", editarAutor, name="AutoresEditar"), #CRUD

    path("login/", IniciarSesion, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("avatar/", agregar_avatar, name="Agregar Avatar"),

    path("", inicio, name="Home"),
    ]