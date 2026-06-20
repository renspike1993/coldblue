from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'auth/home.html', {
        'user': request.user,
    })


@login_required
def logout(request):
    return render(request, 'auth/login.html')


@login_required
def portal(request):
    return render(request, 'auth/portal.html')