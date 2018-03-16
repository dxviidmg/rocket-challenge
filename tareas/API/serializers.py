from rest_framework import serializers
from ..models import *

class TareaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tarea
		fields = ['pk','descripcion', 'duracion', 'tiempo', 'status']