from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable": "This is variable"
    }
    #return HttpResponse("This is the Homepage")
    return render(request, 'index.html', context)

def about(request):
    return render(request,'about.html')
   
def services(request):
    return render(request,'services.html')

def contact(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        ask = request.POST.get('ask')
        contact = Contact(name = name, email =email, ask =ask, date = datetime.today())
        contact.save()
    return render(request,'contact.html')

  