from django.shortcuts import render
from myapp.forms import *
from myapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def marks():
    pass


def exam(request):
    e=Exam.objects.all()
    return render(request, 'myapp/exam.html', {'exam':e})

def question(request,exam_id):
    e=Exam.objects.get(pk=exam_id)
    q=e.question_set.all()
    return render(request, 'myapp/question.html', {'question':q})


def register(request):
    if request.method=='POST':
        form=RForm(request.POST)
        if form.is_valid():
            user_form=form.save()
            user_form.set_password(user_form.password)
            user_form.save()
        else:
            print('form.errors')
    else:
        form=RForm
    dict={'form':form}
    return render(request, 'myapp/register.html', context=dict)

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                exam=Exam.objects.all()
                return HttpResponseRedirect('exam/')
            else:
                return HttpResponse('inacive user')
        else:
            print('invalid details')
    else:
        form=LoginForm
    dict={'form':form}
    return render(request, 'myapp/register.html', context=dict)

@login_required
def userlogout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
