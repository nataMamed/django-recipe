from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from recipe.models import Recipe


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

    if request.method == 'POST':

        email    = request.POST['email']
        password = request.POST['senha']
        
        if email.strip() == '' or password.strip() == '':
            return redirect(to='login')

        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user     = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                print('login com sucesso')

        return redirect(to='dashboard')

    return render(request, template_name='users/login.html')


def logout_view(request):
    
    auth.logout(request)
    return redirect(to='index')



def dashboard_view(request):

    if request.user.is_authenticated:

        id = request.user.id
        recipes = Recipe.objects.order_by('-registration_date').filter(person=id)

        data = {
            'recipes':recipes   
        }
        return render(request, template_name='users/dashboard.html', context=data)
    else:
        return redirect(to='index')

def create_recipe_view(request):

    if request.method == 'POST':
        recipe_name        = request.POST['nome_receita']
        ingredients        = request.POST['ingredientes']
        preparation_method = request.POST['modo_preparo']
        preparation_time   = request.POST['tempo_preparo']
        revenue            = request.POST['rendimento']
        category           = request.POST['categoria']
        recipe_photo       = request.FILES['foto_receita']

        user = get_object_or_404(User, pk=request.user.id)

        recipe = Recipe.objects.create(
            person=user,
            recipe_name=recipe_name,
            ingredients=ingredients,
            preparation_method=preparation_method,
            preparation_time=preparation_time,
            revenue=revenue,
            category=category,
            recipe_photo=recipe_photo
        )
        return redirect(to='dashboard')
    else:
        return render(request, template_name='users/create_recipe.html')