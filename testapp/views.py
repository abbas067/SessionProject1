from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,EmailForm
# Create your views here.
def name_view(request):
 form=NameForm()
 return render(request,'testapp/name.html',{'form':form})
def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form})
def email_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=EmailForm()
    return render(request,'testapp/email.html',{'form':form})
def result_view(request):
    email=request.GET['email']
    request.session['email']=email
    return render(request,'testapp/result.html')
