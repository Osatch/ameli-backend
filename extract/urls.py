from django.urls import path
from .views import lancer_script

urlpatterns = [
   
    path('launch/', lancer_script),
]
