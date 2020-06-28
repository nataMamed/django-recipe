from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def singup_view(request):

    if request.method == 'POST':

        name      = request.POST['nome']
        email     = request.POST['email'] 
        password  = request.POST['password']
        password2 = request.POST['password2']

        if not name.strip():
            return redirect(to='singup')

        if not email.strip():
            return redirect(to='singup')

        if password != password2:
            return redirect(to='singup')
        
        if User.objects.filter(email=email).exists():
            return redirect(to='login')
        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()

        return redirect(to='login')
    else:
        return render(request, template_name='users/singup.html')


def login_view(request):

    return render(request, template_name='users/login.html')


def logout_view(request):
    pass
    # return render(request, template_name='logout.html')


def dashboard_view(request):
    pass
    # return render(request, template_name='dashboard.html')