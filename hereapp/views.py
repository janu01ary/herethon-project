from django.shortcuts import render, redirect
from .models import Email, Result

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def showresults(request):
    results = Result.objects.all()
    return render(request, 'see-results.html', {'results':results})

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
