'''creating views for the app users'''
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



def register(request):
    '''registering new users'''
    if request.method != 'POST':
        # display  blank form
        form = UserCreationForm()
    else:
        # process completed
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #log the user in and then redirect to homepage
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form':form}
    return render(request, 'registration/register.html', context)


