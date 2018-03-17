from rest_framework import serializers
from ..models import *

class TareaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Tarea
		fields = ['pk','descripcion', 'duracion', 'tiempo', 'status']

	def validate(self, data):
		"""
		Check that the start is before the stop.
		"""
		if data['status'] == "completado":
			raise serializers.ValidationError("Tarea completada")
		return data