from django.shortcuts import render,redirect
from userauths.forms import ProfileForm
from userauths.models import Profile

def home(req):
    candidates=Profile.objects.all()
    if req.method=='POST':
        form=ProfileForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form=ProfileForm()
    return render(req,'userauths/home.html',context={'form':form,'cand':candidates})

def candidate_details(req,id):
    candidates=Profile.objects.get(pk=id)
    return render(req,'userauths/candidate.html',context={'candidate':candidates})
