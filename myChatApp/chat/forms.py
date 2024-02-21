from django.forms import ModelForm
from chat.models import Person
class MyModelForm(ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "interest", "countries","langChosen"]
        