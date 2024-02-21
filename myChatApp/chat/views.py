from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import MyModelForm
from .models import Person
from django.contrib.auth.models import User
def updateDatabase(request):
    current_user = User.objects.get(id= request.user.id)
    form = MyModelForm(request.POST)
    return redirect('chat-page', {'form' : form})
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
   
    
    curPerson = Person.objects.all().get(username_id = User.objects.get(id= request.user.id))
    form = MyModelForm(request.POST)
    if request.method == "POST":
        
        
        if form.is_valid():
            saved_data = form.cleaned_data
            f_name = saved_data['first_name']
            l_name = saved_data['last_name']
            int_val = saved_data['interest']
            count = saved_data['countries']
            
            langChose = saved_data['langChosen']
            curPerson = Person.objects.all().get(username_id = User.objects.get(id= request.user.id))
            print(curPerson.username)
            curPerson.first_name = f_name
            curPerson.last_name = l_name
            curPerson.interest = int_val
            curPerson.countries = count
            curPerson.langChosen = langChose
            curPerson.save()


        else:
            print("NOT VALID")
        return redirect('chat-page')
        
            
    showDrop = True
    
    return render(request, "mainPage.html", {'form' : form, 'showDrop': showDrop, 'curPerson' : curPerson})