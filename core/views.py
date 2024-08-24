from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'core/index.html')


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to your desired page after login
        else:
            # Handle invalid login
            return render(request, 'authentication/login.html', {'error_message': 'invalid username or password!'})
        
    return render(request, 'authentication/login.html')


def registerPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = request.POST['email'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name']
            )

            login(request, user)

            return redirect('index')

    return render(request, 'authentication/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index') 
