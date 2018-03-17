from ..models import Tarea
from .serializers import TareaSerializer 
from rest_framework import generics

class TareasPendientesList(generics.ListCreateAPIView):
	queryset = Tarea.objects.filter(status="pendiente")
	serializer_class = TareaSerializer

class TareasCompletadasList(generics.ListCreateAPIView):
	queryset = Tarea.objects.filter(status="completado")
	serializer_class = TareaSerializer


class TareasList(generics.ListCreateAPIView):
	queryset = Tarea.objects.all()
	serializer_class = TareaSerializer

	def get_queryset(self):
		qs = Tarea.objects.all()
		query = self.request.GET.get("q")

		if query is not None:
			qs = qs.filter(descripcion__icontains=query)
		return qs	

class TareasRUD(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = TareaSerializer

	def get_queryset(self):
		return Tarea.objects.all()