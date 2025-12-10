from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CadastroForm, LoginForm, TonalidadeForm
from .models import TonalidadeConfig


def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # cria config padrão
            TonalidadeConfig.objects.create(user=user)
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'core/cadastro.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # tentar por username
            user = authenticate(request, username=username_or_email, password=password)

            if user is None:
                # tentar por email
                from django.contrib.auth.models import User
                try:
                    user_obj = User.objects.get(email=username_or_email)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    """
    Tela inicial com o botão LIGUE AQUI.
    O estado "ligado/desligado" fica na sessão.
    """
    if request.method == 'POST':
        liga = request.POST.get('ligar')
        request.session['filtro_ativo'] = (liga == '1')

    filtro_ativo = request.session.get('filtro_ativo', False)

    # pegar config do usuário (ou padrão)
    config, _ = TonalidadeConfig.objects.get_or_create(user=request.user)

    context = {
        'filtro_ativo': filtro_ativo,
        'config': config,
    }
    return render(request, 'core/home.html', context)


@login_required
def config_tonalidades_view(request):
    config, _ = TonalidadeConfig.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = TonalidadeForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas!')
            return redirect('home')
    else:
        form = TonalidadeForm(instance=config)

    return render(request, 'core/config_tonalidades.html', {'form': form})


@login_required
def user_info_view(request):
    """
    Tela de informações do usuário / explicação do Tonalizze.
    Você pode colar trechos da sua introdução aqui.
    """
    return render(request, 'core/user_info.html')
