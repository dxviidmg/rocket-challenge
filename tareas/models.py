from django.db import models
from django.utils import timezone
import datetime 

class Tarea(models.Model):
	status_choices = (
		("pendiente","pendiente"),
		("completado","completado")
	)

	descripcion = models.CharField(max_length=50)
	creacion = models.DateTimeField(default=timezone.now)
	duracion = models.IntegerField()
	tiempo = models.IntegerField(null=True, blank=True)
	status = models.CharField(max_length=20, default="pendiente", choices=status_choices)

	def __str__(self):
		return '{} creada el {}'.format(self.descripcion, self.creacion)

	def save(self, *args, **kwargs):
		if self.status == "completado":

			ahora = datetime.datetime.now(timezone.utc)
			tdelta = ahora - self.creacion
			minutos = tdelta.seconds/60
			self.tiempo = minutos
		super(Tarea, self).save(*args, **kwargs)