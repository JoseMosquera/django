from django.urls import path
from .views import SingUpView, PerfilUpdate

urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('perfil/', PerfilUpdate.as_view(), name='perfil'),
]