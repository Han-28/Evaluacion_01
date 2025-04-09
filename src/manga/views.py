from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Manga
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

import requests

def get_cover_url(manga_id):
    """Obtiene la URL de la portada de un manga desde MangaDex API."""
    try:
        # 1. Obtener el ID del cover art
        cover_response = requests.get(
            f"https://api.mangadex.org/cover?manga[]={manga_id}&limit=1"
        )
        cover_data = cover_response.json()
        
        if cover_data['data']:
            cover_id = cover_data['data'][0]['id']
            filename = cover_data['data'][0]['attributes']['fileName']
            # 2. Construir la URL final de la imagen
            return f"https://uploads.mangadex.org/covers/{manga_id}/{filename}"
    except Exception as e:
        print(f"Error al obtener portada: {e}")
    return None  

def search_manga(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        url = f"https://api.mangadex.org/manga?title={query}&limit=8"
    else:
        url = "https://api.mangadex.org/manga?limit=8&order[followedCount]=desc"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get('data', [])
        for manga in results:
            manga['cover_url'] = get_cover_url(manga['id'])

    # Obtener IDs ya guardados
    saved_ids = set(Manga.objects.values_list('manga_id', flat=True))

    return render(request, 'manga/search.html', {
        'query': query,
        'results': results,
        'saved_ids': saved_ids,
    })


def save_manga(request):
    if request.method == 'POST':
        manga_id = request.POST.get('manga_id')
        title = request.POST.get('title')
        cover_url = request.POST.get('cover_url')
        
        # Guardar en la base de datos (usa el usuario anónimo si no hay login)
        user = User.objects.get_or_create(username='anonimo')[0]  # Temporal hasta añadir login
        Manga.objects.create(
            user=user,
            title=title,
            manga_id=manga_id,
            cover_url=cover_url,
            status='planned',  # Valor por defecto
            description='',  # Descripción opcional
        )
         # Verifica si ya existe (evita duplicados)
        if not Manga.objects.filter(manga_id=manga_id).exists():
            Manga.objects.create(
                manga_id=manga_id,
                title=title,
                cover_url=cover_url,
                description="",  # o lo puedes obtener de la API si quieres
                status='planned',  # valor por defecto
                rating=None
            )
        return redirect('search_manga')
    
def manga_detail(request, pk):
    # Obtiene el manga o muestra 404 si no existe
    manga = get_object_or_404(Manga, pk=pk)
    
    return render(request, 'manga/detail.html', {
        'manga': manga,
    })
def manga_list(request):
    saved_mangas = Manga.objects.all()
    return render(request, 'manga/list.html', {'saved_mangas': saved_mangas})


def edit_manga(request, pk):
    manga = get_object_or_404(Manga, pk=pk)

    if request.method == 'POST':
        manga.status = request.POST.get('status')
        manga.rating = request.POST.get('rating')
        manga.description = request.POST.get('description')
        manga.save()
        return redirect('manga_list')

    return render(request, 'manga/edit_manga.html', {'manga': manga})

def delete_manga(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    manga.delete()
    return redirect('manga_list')


