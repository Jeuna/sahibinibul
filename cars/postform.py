from django import forms
from .models import car

class PostForm(forms.ModelForm):

    class Meta:
        model = car
        fields = [
                'renk',
                'model',
                'model_yili',
                'plaka',


        ]