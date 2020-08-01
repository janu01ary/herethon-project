from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from .models import Email, Result

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def result(request):
    return render(request, 'result.html')
  
def showresults(request):
    results = Result.objects.all()
    return render(request, 'see-results.html', {'results':results})

def sendallresults(request):
    results = Result.objects.all()
    message = results
    subject = "결과들을 전송합니다."
    emails = Email.objects.all()
    email = emails.first()
    for email in emails:
        send_email = EmailMessage(subject, message, to=[email.email])
        send_email.send()
    return redirect('okpage')
    
def okpage(request):
    return render(request, 'okpage.html')

def addemail(request):
    if request.method == 'POST':
        newEmail = Email()
        newEmail.name = request.POST['name']
        newEmail.email = request.POST['email']
        newEmail.save()
        return redirect('mypage')
    else:
        return render(request, 'addemail.html')

def deleteemail(request, pk):
    email = get_object_or_404(Email, pk = pk)
    email.delete()
    return redirect('mypage')

def mypage(request):
    emails = Email.objects.all()
    return render(request, 'mypage.html', {'emails':emails})

