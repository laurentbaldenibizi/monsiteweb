from django.forms import ModelForm
from app.models import Commentaire


class CommentForm(ModelForm):

    class Meta:
        model = Commentaire
        fields = '__all__'
        exclude=['publication']