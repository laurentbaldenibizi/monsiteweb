from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import Publication
from app.forms import PublicationForm


@login_required(login_url='/login')
def index(request):
    assert isinstance(request, HttpRequest)
    publications = Publication.objects.all()
    return render(
        request,
        'app/publication/index.html',
        {
            'publications': publications
        }
    )


@login_required(login_url='/login')
def create(request):
    form = PublicationForm()
    return render(
        request,
        'app/publication/create.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login')
def store(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "actu ajoutee !")
        return redirect('/publication')


@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = PublicationForm()
        else:
            publications = Publication.objects.get(pk=id)
            form = PublicationForm(instance=publications)
        return render(
            request,
            'app/publication/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = PublicationForm(request.POST)
        else:
            publications = Publication.objects.get(pk=id)
            form = PublicationForm(request.POST, instance=publications)
        if form.is_valid():
            form.save()
        messages.success(request, "modification reussie !")
        return redirect('/publication')


@login_required(login_url='/login')
def delete(request, id):
    publications = Publication.objects.get(pk=id)
    publications.delete()
    messages.success(request, "actu supprimee !")
    return redirect('/publication')
