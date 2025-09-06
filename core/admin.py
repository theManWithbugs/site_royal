from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models

# Adiciona o campo telefone ao User como atributo extra
User.add_to_class('telefone', models.CharField(max_length=20, unique=True, blank=False))

# Personaliza o admin para mostrar o campo telefone
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações extras', {'fields': ('telefone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações extras', {'fields': ('telefone',)}),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)