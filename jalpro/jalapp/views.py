from django.shortcuts import render
from .models import ServicesData,FeedbackData,EnquiryData
from .forms import FeedbackForm,EnquiryForm
from django.http.response import HttpResponse
import datetime as  dt
date1=dt.datetime.now()

# Create your views here.
def home_view(request):
    return render(request,'home.html')


def services_view(request):
    services=ServicesData.objects.all()
    return render(request,'services.html',{'services':services})


def enquiry_view(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name1=request.POST.get('name')
            mobile1=request.POST.get('mobile')
            email1=request.POST.get('email')
            gender1=request.POST.get('gender')
            courses1=eform.cleaned_data.get('course')
            shifts1=eform.cleaned_data.get('shifts')
            start_date1=eform.cleaned_data.get('start_date')
            data=EnquiryData(
                name=name1,
                mobile=mobile1,
                email=email1,
                gender=gender1,
                course=courses1,
                shifts=shifts1,
                start_date=start_date1
            )
            data.save()
            eform=EnquiryForm()
            return render(request,'enquiry.html',{'eform':eform})
        else:
            return HttpResponse("Invalid Data")
    else:
        eform=EnquiryForm()
        return render(request,'enquiry.html',{'eform':eform})


def gallery_view(request):
    return render(request,'gallery.html')


def feedback_view(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name1=request.POST.get('name')
            rating1=request.POST.get('rating')
            feedback1=request.POST.get('feedback')
            data=FeedbackData(
                name=name1,
                rating=rating1,
                feedback=feedback1,
                date=date1
            )
            data.save()
            fform=FeedbackForm()
            feedback=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'feedback':feedback})
        else:
            return HttpResponse("User Invalid Data")

    else:
        fform=FeedbackForm()
        feedback=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'feedback':feedback})