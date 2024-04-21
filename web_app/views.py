from django.shortcuts import render,redirect,HttpResponse
from .models import blog,contactus,profile
from .forms import blogfrom,contactfrom,profilefrom,leavecomment
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Home Function
@login_required(login_url='login')
def home(request):
    data = blog.objects.all()
    return render(request,'index.html',{'data':data})

#Show blog function
@login_required(login_url='login')
def showb(request):
    data = blog.objects.all()
    return render(request,'index.html',{'data':data})

#form blog function
@login_required(login_url='login')
def formb(request):
    if request.method == 'GET':
        form =blogfrom()
        return render(request,'formblog.html',{'form':form})

    else:
        form = blogfrom(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('showb')

        else:
            return redirect('formblog')

#delete blog function 
@login_required(login_url='login')      
def delete(request,id):
    data = blog.objects.get(id=id)
    data.delete()
    return redirect('showb')

#Update blog function
@login_required(login_url='login')
def update(request,id):
    data = blog.objects.get(id=id)
    if request.method == 'GET':
        form = blogfrom(instance=data)
        return render(request,'formblog.html',{'form':form})

    else:
        form = blogfrom(request.POST,instance=data)
        if form.is_valid:
            form.save()
            return redirect('showb')
        else:
            return redirect('formb')

        
#Signup function
def signup(request):
    if request.method =='POST':
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password==confirm:
            if User.objects.filter(username=user).exists():
                messages.success(request,'user already exists')
                return redirect('sign')

            elif User.objects.filter(email=email).exists():
                messages.success(request,'email already exists')
                return redirect('sign')

            else:
                User.objects.create_user(username=user,email=email,password=password).save()
                return redirect('login')
            
        else:
            messages.success(request,'password not match')
        return render(request,'sign.html')
    return render(request,'sign.html')

#login function
def login(request):
    if request.method =='POST':
        user = request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(username=user,password=password)

        if user is None:
            messages.error(request,'user/password not exist')
            return redirect('sign')
        else:
            auth.login(request,user)
            return redirect('home')

    else:
        return render(request,'login.html') 

#logout function
def logout(request):
    auth.logout(request)
    return redirect('hbase') 
   
#Show login function
@login_required(login_url='login')
def show(request):
    data = User.objects.all()
    return render(request,'show.html',{'data':data})

#Read about blog function
@login_required(login_url='login')
def readmore(request,id):
    data1 = blog.objects.get(id=id)
    data2 = leavecomment.objects.filter(user_id=id)
    return render(request,'readmore.html',{'data':data1,'data2':data2})

#show contact function
@login_required(login_url='login')
def contact(request):
    data = contactus.objects.all()
    return render(request,'showcontact.html',{'data':data})

#form contect function
@login_required(login_url='login')
def formc(request):
    if request.method == 'GET':
        form =contactfrom()
        return render(request,'contactform.html',{'form':form})

    else:
        form = contactfrom(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('showc')

        else:
            return redirect('formc')

# Show profile function
@login_required(login_url='login')    
def sprofile(request):
    data = profile.objects.all()
    return render(request,'showprofile.html',{'data':data})

#Edit blog Function     
@login_required(login_url='login')    
def edit(request):
    data=blog.objects.filter(created_by=request.user)
    return render(request,'edit.html',{'data':data})

#Show profile function  
@login_required(login_url='login')  
def sfile(request):
    if request.user.is_authenticated:
        if profile.objects.filter(user=request.user).exists():
            image = profile.objects.filter(user=request.user)
            data1 = blog.objects.filter(created_by=request.user)
            return render(request,'showprofile.html',{'image':image,'data1':data1})
        else:
            return redirect('showf')
    else:
        return redirect('login')
          
#Form profile function
@login_required(login_url='login')       
def ffile(request):
    try:
        
        data = profile.objects.get(user=request.user)
        if data:
            return redirect("showf")
        else:
            if request.method == 'GET':
                form =profilefrom()
                return render(request,'formprofile.html',{'form':form})

            else:
                form = profilefrom(request.POST,request.FILES)
                if form.is_valid:
                    form.save()
                    return redirect('showf')
            
    except:
       if request.method == 'GET':
                form =profilefrom()
                return render(request,'formprofile.html',{'form':form})

       else:
                form = profilefrom(request.POST,request.FILES)
                if form.is_valid:
                    form.save()
                    return redirect('showf')

# first Login function 
@login_required(login_url='login')
def lbase(request):
    data=blog.objects.all()
    return render(request,'loginhome.html',{'data':data})    

#show signup function
@login_required(login_url='login')
def showsign(request):
     data = User.objects.all()
     return render(request,'showfile.html',{'data':data})

#show all blog function
@login_required(login_url='login')
def adds(request):
    data = User.objects.all()
    return render(request,'edit.html',{'data':data})

#delete sign function
@login_required(login_url='login')
def delete1(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('show')

#Update sign function
@login_required(login_url='login')
def update1(request,id):
    if request.method=='POST':
        username=request.POST['username']
        
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']

        if password==confirm:
            if User.objects.filter(id=id,username=username).exists():
                messages.success(request,'User name already exists')
                return redirect('show')
            
            elif User.objects.filter(id=id,email=email).exists():
                messages.success(request,'Email-addres is already exists ')
                return redirect('show')
            else:
                data=User.objects.create_user(id=id,username=username,email=email,password=password)
                return redirect('show')
        else:
            messages.success(request,'Password does not match')

    return render(request,'sign.html')

#Search function
@login_required(login_url='login')
def search(request):
    if request.method == "POST":
        search = request.POST['search']

        data = blog.objects.filter(tittle__contains=search)
        return render(request,'search.html',{'data':data})
    else:
        return render(request,'search.html')
    
#update profile photo
@login_required(login_url='login')
def updatei(request,id):
    data = profile.objects.get(id=id)
    if request.method == 'GET':
        form = profilefrom(instance=data)
        return render(request,'formprofile.html',{'form':form})

    else:
        form = profilefrom(request.POST,request.FILES,instance=data)
        if form.is_valid:
            form.save()
            return redirect('showf')
        else:
            return redirect('formf')

#delete profile photo
@login_required(login_url='login')
def deletei(request,id):
    data = profile.objects.get(id=id)
    data.delete()
    return render(request,'showprofile.html',{'data':data})

#About us function
@login_required(login_url='login')
def abouts(request):
    return render(request,'about.html')


#password change
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('showp')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'password.html',{'form':form})


#Filter function
@login_required(login_url='login')
def filtr(request,name):
    print(name)
    dat = blog.objects.all().order_by(name)
    return render(request,'filter.html',{'data':dat})

#Comment function
@login_required(login_url='login')
def com(request):
    print("in")
    if request.method =="POST":
        print("u")
        user  = request.POST['u_id']
        post = request.POST['post_id']
        comment = request.POST['comment']
        print(comment)
        leavecomment.objects.create(adds_id=user,user_id=post,comment=comment)
        return redirect("readmore",post)
    return render(request,'readmore.html')

#SHow comment function
def comment(request,id):
    data = leavecomment.objects.filter(user_id=id)
    return render(request,'comment.html',{'data':data})

#delete comment function
def deletecomment(request,id,post_id):
    data = leavecomment.objects.get(id=id)
    data.delete()
    return redirect('readmore',id=post_id)

#forgot  password 
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.shortcuts import render, redirect

# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('password_change_done')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change-password/change_password.html', {'form': form})

# def password_change_done(request):
#     return render(request, 'change-password/password_change_done.html')

from django.shortcuts import render

def password_reset_done(request):
    # Assuming you have a user object with uidb64 and token attributes
    user = get_user_somehow(request)

    context = {
        'user': user,
        'protocol': 'https',  # Replace with your protocol
        'domain': 'gmail.com',  # Replace with your domain
    }

    return render(request, 'registration/password_reset_done.html', context)


