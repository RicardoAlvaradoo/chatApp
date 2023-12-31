from django.forms import ModelForm
from chat.models import User
class MyModelForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "interest", "countries","langChosen"]
        