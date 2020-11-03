from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import student,studentmessage,Item

# Create your views here.
def video(request):
    obj=Item.objects.all()
    return render(request,"video.html",{'obj':obj})

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        sfname=request.POST["sfname"]
        slname=request.POST["slname"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        msg=studentmessage.objects.create(sfname=sfname,slname=slname,email=email,subject=subject,message=message)
        msg.save()
        messages.info(request,"sending successful")
        return redirect(contact)
    else:
        return render(request,"contact.html")
def admission(request):
    if request.method=="POST":
        sname=request.POST["sname"]
        sfathername=request.POST["sfathername"]
        sdob=request.POST["sdob"]
        saadharno=request.POST["saadharno"]
        smothername=request.POST["smothername"]
        sschoolname=request.POST["sschoolname"]
        sgrade=request.POST["sgrade"]
        scollegename=request.POST["scollegename"]
        smarks=request.POST["smarks"]
        shouseno=request.POST["shouseno"]
        scolonyname=request.POST["scolonyname"]
        scityname=request.POST["scityname"]
        sdistrictname=request.POST["sdistrictname"]
        smandalname=request.POST["smandalname"]
        sphonenumber=request.POST["sphonenumber"]
        sgmail=request.POST["sgmail"]
        gender=request.POST["gender"]
        degreegroup=request.POST["degreegroup"]
        board=request.POST["board"]
        intergroup=request.POST["intergroup"]
        country=request.POST["country"]
        code=request.POST["code"]

        
        if student.objects.filter(saadharno=saadharno).exists():
            messages.info(request,"student taken")
            return redirect(admission)
        else:
            user=student.objects.create(sname=sname,sfathername=sfathername,sdob=sdob,saadharno=saadharno,smothername=smothername,sschoolname=sschoolname,sgrade=sgrade,scollegename=scollegename,smarks=smarks,shouseno=shouseno,scolonyname=scolonyname,scityname=scityname,sdistrictname=sdistrictname,smandalname=smandalname,sphonenumber=sphonenumber,sgmail=sgmail,gender=gender,degreegroup=degreegroup,board=board,intergroup=intergroup,country=country,code=code)                               
            user.save()
            messages.info(request,"submit successfull")
            return redirect(admission)
    else:
        return render(request,"form.html")



        
    
