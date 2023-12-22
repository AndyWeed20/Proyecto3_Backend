from seminario_app import views
from django.contrib import admin
from django.urls import path
from seminario_app.views import (
    IndexView,
    InscritoListView,
    InscritoCreateView,
    InstitucionCreateView,
    AutorAPI,
    InscritoListAPIView,
    institucion_list_api,
    inscrito_detalle,
    institucion_detalle,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'), 
    path('inscritos_ui/', InscritoListView.as_view(), name='inscrito_list_ui'),
    path('inscritos/', InscritoCreateView.as_view(), name='inscrito_create'),
    path('instituciones/', InstitucionCreateView.as_view(), name='institucion_create'),
    path('api/inscritos/', InscritoListAPIView.as_view(), name='api_inscrito_list'),
    path('api/instituciones/', institucion_list_api, name='api_institucion_list'),
    path('api/inscritos/<int:id>/', views.inscrito_detalle, name='inscrito_detalle'),
    path('api/instituciones/<int:id>/', views.institucion_detalle, name='institucion_detalle'), 
    path('api/autor/', AutorAPI.as_view(), name='api_autor'),
]



