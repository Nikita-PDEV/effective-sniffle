from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def page1(request):
    return render(request, 'myapp/page1.html')

@login_required
def page2(request):
    return render(request, 'myapp/page2.html')

def page3(request):
    return render(request, 'myapp/page3.html')
