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
            return redirect('listar_frutas')
    else:
        form = FrutaForm()
    return render(request, 'frutas/criar_fruta.html', {'form': form})

def read(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    return render(request, 'frutas/detalhar_fruta.html', {'fruta': fruta})

def update(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        form = FrutaForm(request.POST, instance=fruta)
        if form.is_valid():
            form.save()
            return redirect('listar_frutas')
    else:
        form = FrutaForm(instance=fruta)
    return render(request, 'frutas/atualizar_fruta.html', {'form': form})

def delete(request, id):
    fruta = get_object_or_404(Fruta, id=id)
    if request.method == 'POST':
        fruta.delete()
        return redirect('listar_frutas')
    return render(request, 'frutas/excluir_fruta.html', {'fruta': fruta})
