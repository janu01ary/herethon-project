from django.shortcuts import render, redirect
from .models import Email

# Create your views here.
def index(request):
    return render(request, 'index.html')

def showresults(request):
    return render(request, 'see-results.html')

def addemail(request):
    if request.method == 'POST':
        newEmail = Email()
        newEmail.name = request.POST['name']
        newEmail.email = request.POST['email']
        newEmail.save()
        return redirect('mypage')
    else:
        return render(request, 'addemail.html')

def mypage(request):
    emails = Email.objects.all()
    return render(request, 'mypage.html', {'emails':emails})