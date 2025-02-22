from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from fotos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload_foto, name='upload_foto'),
    path('fotos/', views.fotos_lista, name='fotos_lista'),  # Nova URL para listar as fotos
    path('fotos/excluir/<int:foto_id>/', views.excluir_foto, name='excluir_foto'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
