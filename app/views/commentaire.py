from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import Commentaire,Publication

from app.forms import CommentForm


@login_required(login_url='/login')
def index(request):
    assert isinstance(request, HttpRequest)
    commentaires = Commentaire.objects.all()
    return render(
        request,
        'app/commentaire/index.html',
        {
            'commentaires': commentaires
        }
    )


@login_required(login_url='/login')
def create(request,id):
    form = CommentForm()
    return render(
        request,
        'app/commentaire/create.html',
        {
            'form': form,
            'id':id
        }
    )


@login_required(login_url='/login')
def store(request,id):
    if request.method == 'POST' or None:
       
        form = CommentForm(request.POST or None)
        if form.is_valid():
            publication= Publication.objects.get(id=id)
            nom = form.cleaned_data["nom"]
            prenom = form.cleaned_data["prenom"]
            email = form.cleaned_data["email"]
            contenu = form.cleaned_data["contenu"]
            commentaire=Commentaire.objects.create(publication=publication,nom=nom,prenom=prenom,email=email,contenu=contenu)
            commentaire.save()
        messages.success(request, "commentaire envoyee !")
        return redirect('/publication')


@login_required(login_url='/login')
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CommentForm()
        else:
            commentaires = Commentaire.objects.get(pk=id)
            form = CommentForm(instance=commentaires)
        return render(
            request,
            'app/commentaire/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CommentForm(request.POST)
        else:
            commentaires = Commentaire.objects.get(pk=id)
            form = CommentForm(request.POST, instance=commentaires)
        if form.is_valid():
            form.save()
        messages.success(request, "commentaire  modifiée !")
        return redirect('/publication')







# lister les commentairess par post
@login_required(login_url='/login')
def list_per_post(request,id):
    assert isinstance(request, HttpRequest)
    commentaires_post = Commentaire.objects.filter(publication=id)
    return render(
        request,
        'app/commentaire/post.html',
        {
            'commentaires_post': commentaires_post
        }
    )