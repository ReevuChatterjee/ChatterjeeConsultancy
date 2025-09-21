from django.shortcuts import render,redirect
from .models import custRequest
import requests
API_KEY="3a9ce86145cb48f1b3a953c972f892e6"

def home(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    return render(request, "index.html", {"error": error, "success": success})

def validate_email_api(email):
    url=f"https://emailreputation.abstractapi.com/v1/?api_key={API_KEY}&email={email}"
    response=requests.get(url).json()
    return response

def requestForm(request):
    if request.method=="POST":
        fullName=request.POST.get("name")
        email=request.POST.get("email")
        result=validate_email_api(email)
        type=request.POST.get("type")
        budget=request.POST.get("budget")
        describe=request.POST.get("message")

        deliverability_info = result.get("email_deliverability", {})
        status = deliverability_info.get("status")
        detail = deliverability_info.get("status_detail", "unknown")

        if status != "deliverable":
            # Save error into session and redirect to home
            request.session["error"] = "Email not deliverable (Email does not Exist!)."
            return redirect("home")
        else:

            custRequest.objects.create(fullName=fullName,
                                    email=email,
                                    type=type,
                                    budget=budget,
                                    describe=describe
                                    )
            request.session["success"] = "Your request was submitted successfully!"
            return redirect("home")

    return render(request,'index.html')

        


# Create your views here.
