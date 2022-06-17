from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home page")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("About Us page")

def company(request):
    return render(request,'company.html')
    #return HttpResponse("CTA for company")

def candidate(request):
    return render(request,'candidate.html')
    #return HttpResponse("CTA for candidate")

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("Contact us page")