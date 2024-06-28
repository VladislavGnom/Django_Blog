from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# OPTIONAL VIEW
def dashboard(request):
    return render(request, 'authapp/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'authapp/register_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegisterForm()
    
    return render(request, 'authapp/register.html', {'user_form': user_form})
