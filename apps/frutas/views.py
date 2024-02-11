from django.shortcuts import render, redirect, get_object_or_404
from .models import Fruta, FrutaForm

def list(request):
    frutas = Fruta.objects.all()
    return render(request, 'list.html', {'list': frutas})

def create(request):
    if request.method == 'POST':
        form = FrutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frutas')
    else:
        form = FrutaForm()
    return render(request, 'create.html', {'form': form})

def read(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    return render(request, 'read.html', {'item': fruta})

def update(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        form = FrutaForm(request.POST, instance=fruta)
        if form.is_valid():
            form.save()
            return redirect('frutas')
    else:
        form = FrutaForm(instance=fruta)
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        fruta.delete()
        return redirect('frutas')
    return render(request, 'delete.html', {'item': fruta})
