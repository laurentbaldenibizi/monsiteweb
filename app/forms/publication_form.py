from django.forms import ModelForm
from app.models import Publication


class PublicationForm(ModelForm):

    class Meta:
        model = Publication
        fields = '__all__'