from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'rud/(?P<pk>[-\d]+)$', views.TareasRUD.as_view(), name="tarea-rud"),
	url(r'search/$', views.TareasList.as_view(), name="tareas-search"),
	url(r'list/completadas/$', views.TareasCompletadasList.as_view(), name="tarea-list-comp"),
	url(r'list/pendientes/$', views.TareasPendientesList.as_view(), name="tarea-list-pend"),	
	url(r'list/$', views.TareasList.as_view(), name="tarea-list-all"),

]

#urlpatterns = format_suffix_patterns



#from django.conf.urls import url, include
#from . import views

#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('vacantes',
#	views.VacantesViewSet)


#urlpatterns = [
#	url(r'^', include(router.urls))
#]