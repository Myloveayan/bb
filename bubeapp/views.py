from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

#def contact(request):
#    return render(request, 'contact.html')
