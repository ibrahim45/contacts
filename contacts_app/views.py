from django.http.response import HttpResponseRedirect
from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponse
from contacts_app.forms import Contactform
from contacts_app.models import Contact

def view_all(request):
    c=Contact.objects.all().order_by('name')
    return render(request,'test.html',dict(f=c))

def all_c(request):
    c=Contact.objects.all().order_by('name')
    return render(request,'listview.html',dict(f=c))

def delete_all(request):
    Contact.objects.all().delete()
    return HttpResponse('your all contacts are deleted')

      
def create_contact(request):
    f =Contactform(request.POST)
    if request.method=="POST":
        if f.is_valid():
            n=f.cleaned_data['name']
            num=f.cleaned_data['number']
            Contact.objects.create(name=n,number=num)
            return HttpResponseRedirect('view_all')
    else:
        f=Contactform()
    return render(request,'cv.html',{'form':f})


def index(request):
    return render(request,"index.html")


def update(request,Contact_id):
    p=Contact.objects.get(pk=Contact_id)
    print p.number,p.name
    f =Contactform(request.POST)
    if request.method=="POST":
        if f.is_valid():
            n=f.cleaned_data['name']
            num=f.cleaned_data['number']            
            Contact.objects.filter(pk=Contact_id).update(name=n,number=num)    
            return HttpResponseRedirect('/admin/index')
    return render(request,"update.html",dict(d=p))

def delete(request,Contact_id):
    p=Contact.objects.get(pk=Contact_id)
    if request.method=="POST":
        Contact.objects.filter(pk=Contact_id).delete()
        return HttpResponseRedirect('/admin/index')
    return render(request,'confirm_del.html',dict(d=p))


def all_u(request):
    c=Contact.objects.all().order_by('name')
    return render(request,'a.html',dict(f=c))
    