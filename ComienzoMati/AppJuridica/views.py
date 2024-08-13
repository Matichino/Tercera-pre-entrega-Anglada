from django.shortcuts import render
from AppJuridica.models import Cliente
from AppJuridica.forms import ClienteFormulario

def inicio(request):
    return render (request, "AppJuridica/index.html")

def ServiciosJuridicos (request):
    return render ( request, "AppJuridica/Servicios Juridicos.html")

def ServiciosCiberseguridad(request):
    return render ( request,"AppJuridica/Vista Servicios Ciberseguridad.html")

def Precios(request):
    return render ( request,"AppJuridica/Precios.html")

def SobreNosotros(request):
    return render ( request,"AppJuridica/Sobre Nosotros.html")


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuariocreado = Cliente(
                usuario=informacion["usuario"],
                numero_de_caso=informacion["numero_de_caso"]
            )
            usuariocreado.save()
            return render(request, "AppJuridica/index.html")
    else:
        mi_formulario = ClienteFormulario()

    return render(request, "AppJuridica/form-con-api.html", {"mi_formulario": mi_formulario})