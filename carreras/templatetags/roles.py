from django import template
from django.contrib.auth.models import Group
from carreras.models import Carrera

register = template.Library()

@register.filter()
def rol(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False