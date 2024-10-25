from django.shortcuts import render
from account.forms import LoginForm
# Create your views here.
def login_views(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form' : form})