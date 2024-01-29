from django.db import models

# Create your models here.
class Category(models.Model):
    """Model für eine Kategorie. Jedes Model muss von models.Model erben."""
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


