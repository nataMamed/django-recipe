from django.shortcuts import render



def singup_view(request):

    return render(request, template_name='users/singup.html')


def login_view(request):

    return render(request, template_name='users/login.html')


def logout_view(request):
    pass
    # return render(request, template_name='logout.html')


def dashboard_view(request):
    pass
    # return render(request, template_name='dashboard.html')