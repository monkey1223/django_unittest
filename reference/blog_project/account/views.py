from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    user_name = request.POST.get('username', '')
    pass_word = request.POST.get('password', '')
    _user = auth.authenticate(username=user_name, password=pass_word)

    if _user is not None:
        auth.login(request, _user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    # return render_to_response('loggedin.html',
    #                             {"fullname": request.user.username})
    return HttpResponseRedirect('/')

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    # return render_to_response('logout.html')
    return HttpResponseRedirect('/')

from account.forms import MyRegistrationFrom

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationFrom()
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

