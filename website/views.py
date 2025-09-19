from django.shortcuts import render
from .models import custRequest

def home(request):
    return render(request,'index.html')
def requestForm(request):
    if request.method=="POST":
        fullName=request.POST.get("name")
        email=request.POST.get("email")
        type=request.POST.get("type")
        budget=request.POST.get("budget")
        describe=request.POST.get("message")

        custRequest.objects.create(fullName=fullName,
                                   email=email,
                                   type=type,
                                   budget=budget,
                                   describe=describe
                                   )

    return render(request,'index.html')

        


# Create your views here.
