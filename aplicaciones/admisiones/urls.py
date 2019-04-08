from django.urls import path, include
from aplicaciones.admisiones.views import RegiatroAdmision, Crear_pdf_prospecto, PreregistroList, PreregistroEdit, \
preregristroDelete
app_name = 'admisiones'
urlpatterns = [
    path('registro-admisiones/', RegiatroAdmision.as_view(), name='registro'),
    path('registro-list/', PreregistroList.as_view(), name='registro_list'),
    path('registro-edit/<int:pk>', PreregistroEdit.as_view(), name='registro_edit'),
    path('registro-delete/<int:pk>', preregristroDelete.as_view(), name='registro_delete'),
    path('registro-admisiones/pdf/<int:pk>/', Crear_pdf_prospecto.as_view(), name='registro_pdf'),
]