from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse
from account.forms import LoginForm

# Create your views here.
def login_views(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem')
                else:
                    return HttpResponse('konto jest zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form' : form})