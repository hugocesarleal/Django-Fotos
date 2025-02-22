from django.shortcuts import render, get_object_or_404, redirect
from .models import Foto
from .forms import FotoForm
import os
from django.conf import settings


def upload_foto(request):
    if request.method == 'POST' and request.FILES['imagem']:
        foto = Foto(imagem=request.FILES['imagem'])
        foto.save()
        return render(request, 'fotos/upload_success.html', {'foto': foto})

    return render(request, 'fotos/upload.html')

def fotos_lista(request):
    fotos = Foto.objects.all()  # Pega todas as fotos do banco de dados
    return render(request, 'fotos/fotos_lista.html', {'fotos': fotos})

def excluir_foto(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)  # Encontra a foto pelo ID
    
    # Exclui o arquivo físico da imagem
    if foto.imagem:
        foto_path = os.path.join(settings.MEDIA_ROOT, foto.imagem.name)
        if os.path.exists(foto_path):
            os.remove(foto_path)
    
    foto.delete()  # Exclui a foto do banco de dados
    return redirect('fotos_lista')  # Redireciona de volta para a galeria