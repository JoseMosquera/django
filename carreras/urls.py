from django.urls import path
from . import views
from .views import EditCarrera, CarreraDelete, EditPosicion, EditEntreno, EntrenoDelete

urlpatterns = [
    #Path de carrera
    path('', views.carreras, name="carreras"),
    path('editcarrera/<int:pk>', EditCarrera.as_view(), name="editcarrera"),
    path('addcarrera/', views.addCarrera, name='addcarrera'),
    path('deletecarrera/<int:pk>/', CarreraDelete.as_view(), name='deletecarrera'),

    #Path de posicion
    path('posicionesuser/', views.posicionesUser, name="posicionesuser"),
    path('apuntarse/<int:carrera_id>/', views.addPosicion, name='apuntarse'),
    path('posiciones/', views.posiciones, name='posiciones'),
    path('posicion/<int:pk>/', EditPosicion.as_view(), name='posicion'),

    #Path de entreno
    path('entrenos/', views.entrenos, name="entrenos"),
    path('entrenosuser/', views.entrenosUser, name="entrenosUser"),
    path('entrenos/addentreno', views.addEntreno, name="addentreno"),
    path('editentreno/<int:pk>', EditEntreno.as_view(), name="editentreno"),
    path('deleteentreno/<int:pk>/', EntrenoDelete.as_view(), name='entrenodelete'),
]