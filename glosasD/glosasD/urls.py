"""
URL configuration for glosasD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from glosasAPIDJ import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Glosas for less documentation
    path('api/glosas/', views.get_all_glosas, name='GetAllGlosas'),
    path('api/glosas/less_doc/<int:glosa_id>/', views.get_one_glosa_less_doc, name='GetOneGlosa'),
    path('api/glosas/create/', views.create_glosa, name='CreateGlosa'),
    path('api/glosas/less_doc/update/<int:glosa_id>/', views.update_glosa_less_doc, name='UpdateGlosa'),
    path('api/glosas/less_doc/delete/<int:glosa_id>/', views.delete_glosa_less_doc, name='DeleteGlosa'),
]
