from django.db import models

class Tarea(models.Model):
	descripcion = models.CharField(max_length=50)
	duracion_estimada = models.IntegerField()
	tiempo = models.IntegerField()
	status = models.CharField(max_length=20, default="pendiente")