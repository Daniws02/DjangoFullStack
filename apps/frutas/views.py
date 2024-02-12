from django.shortcuts import render, redirect, get_object_or_404
from .models import Fruta, FrutaForm

base_url = 'frutas'

def list(request):
    frutas = Fruta.objects.all()
    return render(request, f'{base_url}/list.html', {'list': frutas})

def create(request):
    if request.method == 'POST':
        form = FrutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frutas')
    else:
        form = FrutaForm()
    return render(request, f'{base_url}/create.html', {'form': form})

def read(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    return render(request, f'{base_url}/read.html', {'item': fruta})

def update(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        form = FrutaForm(request.POST, instance=fruta)
        if form.is_valid():
            form.save()
            return redirect('frutas')
    else:
        form = FrutaForm(instance=fruta)
    return render(request, f'{base_url}/update.html', {'form': form, 'item': fruta})

def delete(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        fruta.delete()
        return redirect('frutas')
    return render(request, f'{base_url}/delete.html', {'item': fruta})
