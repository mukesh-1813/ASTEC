from django.shortcuts import render, get_object_or_404
from .models import Magazine

def magazine_list(request):
    magazines = Magazine.objects.all()
    return render(request, 'magazines/list.html', {'magazines': magazines})

def magazine_detail(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    return render(request, 'magazines/detail.html', {'magazine': magazine})
