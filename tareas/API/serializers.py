from rest_framework import serializers
from ..models import *

class TareaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Tarea
		fields = ['pk','descripcion', 'duracion', 'tiempo', 'status']

	def validate_status(self, value):
		"""
		Check that the start is before the stop.
		"""
#		if data['status'] != "completado":
		if 'completado' in value:
			raise serializers.ValidationError("Tarea completada")
		return value