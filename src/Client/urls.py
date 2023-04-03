from django.contrib import admin
from django.urls import path
from .views import Formulaire
urlpatterns = [
    path('', Formulaire, name='main-page'),
    path('admin/', admin.site.urls),
]
