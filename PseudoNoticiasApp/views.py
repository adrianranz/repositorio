from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'PseudoNoticiasApp/home.html')



def whoweare(request):

    return render(request, 'PseudoNoticiasApp/whoweare.html')



def login(request):

    return render(request, 'PseudoNoticiasApp/login.html')

