from django.urls import path
from AppJuridica import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('Servicios Juridicos/', views.ServiciosJuridicos, name= "Servicios Juridicos"),
    path('Servicios Ciberseguridad/', views.ServiciosCiberseguridad, name= "Servicios Ciberseguridad"),
    path('Precios/', views.Precios, name= "Precios"),
    path('Sobre Nosotros/', views.SobreNosotros, name= "Sobre Nosotros")
    
]

Formularios = [
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),

]

urlpatterns += Formularios