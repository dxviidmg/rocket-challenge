from ..models import Tarea
from .serializers import TareaSerializer 
from rest_framework import generics

class TareasList(generics.ListCreateAPIView):
	queryset = Tarea.objects.all()
	serializer_class = TareaSerializer

class TareasRUD(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = TareaSerializer

	def get_queryset(self):
		return Tarea.objects.all()