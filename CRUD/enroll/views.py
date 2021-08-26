from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
# This function will add And shows The Data.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pswd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pswd)
            reg.save()
            fm = StudentRegistration()
    else:
     fm = StudentRegistration()
    data = User.objects.all()
    return render(request,'add&show.html',{'form': fm, 'dat':data})


# This function will update and Edit.
def update_edit(request,id):
    if request.method == 'POST':
        ud = User.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=ud)
        if fm.is_valid():
            fm.save()
    else:
        ud = User.objects.get(pk=id)
        fm = StudentRegistration(instance=ud)
    return render(request,'update.html',{'form': fm})



# This function will Delete The Data.
def del_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')


