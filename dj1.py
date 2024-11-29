from django.db import models
from django.apps import apps

# Przykładowy model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

# Pobranie modelu z rejestru aplikacji
model = apps.get_model('myapp', 'Book')

# Wyświetlenie pól modelu
for field in model._meta.get_fields():
    print(f"Field name: {field.name}, Field type: {field.get_internal_type()}")
