from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and not user.is_staff:  # Only non-staff users
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid login'})
    
    return render(request, 'auth/login.html')