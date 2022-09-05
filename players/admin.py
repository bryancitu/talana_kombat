from django.contrib import admin
from .models import Power, Player

# Register your models here.
class PowersInline(admin.StackedInline):
    model = Power
    extra = 4

class PlayerAdmin(admin.ModelAdmin):
    """Personalization of Player Admin"""

    list_display = ['id', 'username', 'full_name', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['username']
    inlines = [PowersInline]

admin.site.register(Player, PlayerAdmin)
admin.site.register(Power)
