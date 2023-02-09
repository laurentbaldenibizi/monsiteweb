from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import Categories
from app.forms import CategoriesForm


@login_required(login_url='/login')
def index(request):
    assert isinstance(request, HttpRequest)
    categories = Categories.objects.all()
    return render(
        request,
        'app/categories/index.html',
        {
            'categories': categories
        }
    )


@login_required(login_url='/login')
def create(request):
    form = CategoriesForm()
    return render(
        request,
        'app/categories/create.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login')
def store(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "categorie ajoutee !")
        return redirect('/categories')


@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoriesForm()
        else:
            categories = Categories.objects.get(pk=id)
            form = CategoriesForm(instance=categories)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CategoriesForm(request.POST)
        else:
            categories = Categories.objects.get(pk=id)
            form = CategoriesForm(request.POST, instance=categories)
        if form.is_valid():
            form.save()
        messages.success(request, "modification reussie !")
        return redirect('/categories')


@login_required(login_url='/login')
def delete(request, id):
    categories = Categories.objects.get(pk=id)
    categories.delete()
    messages.success(request, "Categorie supprimee !")
    return redirect('/categories')
