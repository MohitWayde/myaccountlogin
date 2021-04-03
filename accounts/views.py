from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = User.objects.get(email=username),password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Login successfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('signin')

    return render(request, 'signin.html')
    
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        address = request.POST['address']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email address already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        username = username,
                        email = email,
                        password = password,
                        # address = address,
                    )
                    user.set_password(request.POST['password'])
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('signin')
        else:
            messages.warning(request, 'password does not match')
            return redirect('signup')

        return redirect('signin')

    return render(request, 'signup.html')

@login_required(login_url='signin')
def dashboard(request):
    # request.session['name'] = 'mysession'
    # if 'name' in request.session:
    #     name = request.session['name']
    #     request.session.modified = True
    #     request.session.flush()
    #     request.session.clear_expired()
    return render(request, 'dashboard.html')
    # else:
    #     return HttpResponse("Session is expired....")
def logout_user(request):
    logout(request)
    return redirect('signin')
