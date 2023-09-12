from django.contrib import admin

# Register your models here.
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'power', 'cost')  # Muestra estos campos en la lista de registros
    list_filter = ('id', 'name', 'power', 'cost')  # Agrega un filtro
    search_fields = ('id', 'name', 'power', 'cost')


admin.site.register(Card, CardAdmin)
