from django.db import models

# No se requiere un modelo para esta versión.
# Si se almacenara un historial, podría existir un modelo como:
#
# class Conversion(models.Model):
#     numero_binario = models.CharField(max_length=255)
#     tipo_conversion = models.CharField(max_length=20)
#     resultado = models.CharField(max_length=255)
#     creado_en = models.DateTimeField(auto_now_add=True)
