from django.urls import path
from . import views

urlpatterns = [
    #Path de carrera
    path('', views.carreras, name="carreras"),
    # path('editcarrera/<int:foro_id>/', views.editcarrera, name="editcarrera"),
    # path('addcarrera/', views.carreraAdd, name='addcarrera'),
    # path('editpost/<int:pk>', editPost.as_view(), name='editpost'),

    #Path de entreno
    path('entrenos/', views.entrenos, name="entrenos"),
]