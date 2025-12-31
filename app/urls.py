"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
from paciente.views import Pacienteviewset
from profissionais.views import ProfissionalViewset
from consultas.views import ConsultaViewset

router = DefaultRouter()
router.register(r'paciente',Pacienteviewset)
router.register(r'consulta', ConsultaViewset)
router.register(r'profissionais', ProfissionalViewset)

urlpatterns = [
    path('', admin.site.urls),
    path('app/', include(router.urls)),
    path('app/token/', TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('app/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
