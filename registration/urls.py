from django.urls import path
from .views import SingUpView, PerfilUpdate, EmailUpdate

urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('perfil/', PerfilUpdate.as_view(), name='perfil'),
    path('perfil/email/', EmailUpdate.as_view(), name='perfil_email'),
]