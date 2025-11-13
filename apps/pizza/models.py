from django.db import models

class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizzas'
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
