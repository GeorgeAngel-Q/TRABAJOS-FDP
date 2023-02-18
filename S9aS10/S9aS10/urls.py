"""S9aS10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from primer_grupo.views import home1,home2,home3
from primer_grupo.views import ejercicio_1,ejercicio_2,ejercicio_3,ejercicio_4,ejercicio_5
from primer_grupo.views import ejercicio_6,ejercicio_7,ejercicio_8,ejercicio_9,ejercicio_10
from primer_grupo.views import ejercicio_11,ejercicio_12,ejercicio_13,ejercicio_14,ejercicio_15
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home1, name="home"),
    path('home/', home1, name="home"),
    path('home2/', home2, name="home2"),
    path('home3/', home3, name="home3"),
    path('ejercicio1/', ejercicio_1),  path('ejercicio2/', ejercicio_2),
    path('ejercicio3/', ejercicio_3),  path('ejercicio4/', ejercicio_4),
    path('ejercicio5/', ejercicio_5),  path('ejercicio6/', ejercicio_6),
    path('ejercicio7/', ejercicio_7),  path('ejercicio8/', ejercicio_8),
    path('ejercicio9/', ejercicio_9),  path('ejercicio10/', ejercicio_10),
    path('ejercicio11/', ejercicio_11),path('ejercicio12/', ejercicio_12),
    path('ejercicio13/', ejercicio_13),path('ejercicio14/', ejercicio_14),
    path('ejercicio15/', ejercicio_15),
]
