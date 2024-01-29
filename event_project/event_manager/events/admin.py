from django.contrib import admin
from .models import Category, Event 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "sub_title"]  # liste von Feldern in der Übersicht


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    @admin.action(description="Mache aktive")
    def make_active(self, _, queryset):
        # queryset => Objekte, die für die Aktion ausgewählt wurden (per checkbox)
        # setze alle Einträge im Queryset auf is_active = True
        queryset.update(is_active=True)

    def make_inactive(self, _, queryset):
        queryset.update(is_active=False)
    
    # Registreieren der Aktionen
    actions = ["make_active", "make_inactive"]

    # Anzeige in der Übersicht
    list_display = ["name", "category", "min_group"]

    # generiert eine Suchbox (erscheint in admin)
    search_fields = ["name", "description"]
    list_filter = ["category"]