from django.db import models

# Create your models here.
class Category(models.Model):
    """Model für eine Kategorie. Jedes Model muss von models.Model erben."""

    class Meta:
        # Meta-Informationen über das Model
        verbose_name_plural = "Kategorien"
        verbose_name = "Kategorie"

    created_at = models.DateTimeField(auto_now_add=True)  # Zeitstempel bei Anlegen setzen

    # immer, wenn Datensatz geändert wird, wird updated_at auf den Zeitstempel gesetzt
    updated_at = models.DateTimeField(auto_now=True) 

    name = models.CharField(max_length=100)  # mandatory, VARCHAR 100
    # null=True => darf in der DB NULL sein
    # blank=True => darf im Formular leer sein
    sub_title = models.CharField(max_length=100, null=True, blank=True)

    # mehrzeiliges Eingabefeld
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        """String Repräsentation einer Python Classe. Die Kategorie soll
        mit ihrem Namen ausgegeben werden."""
        return self.name


class Event(models.Model):

    class MinGroup(models.IntegerChoices):
        """Select-Box in der Adminoberfläche"""
        SMALL = 2
        MEDIUM = 5
        BIG = 10

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    min_group = models.IntegerField(choices=MinGroup.choices)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
     

    def __str__(self) -> str:
        return self.name

