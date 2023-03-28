from django.shortcuts import render , redirect , get_object_or_404 
from django.conf import settings
from django.core.mail import send_mail
from .models import list_name , ver ,log , logins
# Create your views here.


def foodpage(request):
    list = list_name.objects.all()
    if(request.method == "POST"):
        s=request.POST['s']
        items = ''
        if s is None or s is "":
            flowers = list_name.objects.all()
        elif s is not None:
            flowers = list_name.objects.filter(list_location__contains=s)
        return render(request, 'foodpage.html', {'list':flowers })

         
    return render (request,'foodpage.html',{'list':list})
def registration(request):
    if(request.method == "POST"):
        bon=request.POST['email']
        bn=request.POST['name']
        an=request.POST['loc']
        sf=request.POST['price']
        ver(list_name=bn,list_location=an,list_price=sf,list_email=bon).save()
        return redirect(foodpage)
    return render  (request,'register.html',{})




def verification(request):
    v=ver.objects.all()
    if(request.method == "POST"):
        bon=request.POST['name']
        bn=request.POST['loc']
        an=request.POST['pr']
        sf=request.POST['ex']
        bonn=request.POST['em']
        bnn=request.POST['ra']
        a=ver.objects.filter(list_name=bon,list_location=bn).first()
        if(a is not None):  
            list_name(list_name=bon,list_location=bn,list_quality_expiry=sf,list_price=an,list_rating=bnn,list_email=bonn).save()
            a.delete()
            send_mail(f'your {bon} is accepted', f'your {bon} with brand {bn}  has accepted \n your product {sf} \n rating {bnn}' , settings.EMAIL_HOST_USER, [bonn], fail_silently=False)
    
            return redirect(verification)
        
        else:
                return render (request,'verification.html',{'v':v,'key':'not  found '})

       
        # ver(list_name=bn,list_location=an,list_price=sf,list_email=bon).save()
        
    return render (request,'verification.html',{'v':v})

def login(request):
    if(request.method == "POST"):
        u=request.POST['u']
        p=request.POST['p']
        a=log.objects.filter(name=u,password=p)
        if(a is not None):
            return redirect(main)
        
    return render (request ,'login.html',{})

def register(request):
    if(request.method == "POST"):
        u=request.POST['u']
        p=request.POST['p']
        e=request.POST['e']
        cp=request.POST['cp']
        a=log.objects.filter(name=u,password=p)
        if(p==cp):
            if(a is not None):
                pass
            else:
                log.objects.all(name=u,email=e,password=p).save()
                return redirect(login)
        
        
    return render (request ,'registerlog.html',{})



def main(request):
    return render  (request,'main.html',{})








def loginver(request):
    if(request.method == "POST"):
        u=request.POST['u']
        p=request.POST['p']
        a=logins.objects.filter(name=u,password=p)
        if(a is not None):
            return redirect(verification)
        
    return render (request ,'loginverification.html',{})
