from .models import Profile, PromDate
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["year"]
        labels = {
            'year': _('Your Year'),
        }

class CreatePromDateForm(ModelForm):
    class Meta:
        model = PromDate 
        fields = ["name", "year"]
        widgets = {
            'name': TextInput(attrs={
                "autocomplete" : "off", 
                "placeholder" : "Enter date's name here...",
                "class" : "form-control"
                }),
        }