from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'users.html', context)

def register_user(request):
    if request.method=='POST':
        User.objects.create(first_name=request.POST['FN'], last_name=request.POST['LN'], email_address=request.POST['mail'], age=request.POST['years_old'])
    return redirect('/')
# Create your views here.
