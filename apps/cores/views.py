from django.shortcuts import render, redirect, get_object_or_404
from .models import Cor, CorForm

base_url = 'cores'

def list(request):
    cores = Cor.objects.all()
    return render(request, f'{base_url}/list.html', {'list': cores})

def create(request):
    if request.method == 'POST':
        form = CorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cores')
    else:
        form = CorForm()
    return render(request, f'{base_url}/create.html', {'form': form})

def read(request, id):
    cor = get_object_or_404(Cor, id=id)
    return render(request, f'{base_url}/read.html', {'item': cor})

def update(request, id):
    cor = get_object_or_404(Cor, id=id)
    if request.method == 'POST':
        form = CorForm(request.POST, instance=cor)
        if form.is_valid():
            form.save()
            return redirect('cores')
    else:
        form = CorForm(instance=cor)
    return render(request, f'{base_url}/update.html', {'form': form, 'item': cor})

def delete(request, id):
    cor = get_object_or_404(Cor, id=id)
    if request.method == 'POST':
        cor.delete()
        return redirect('cores')
    return render(request, f'{base_url}/delete.html', {'item': cor})
