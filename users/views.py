from django.contrib import messages
from django.shortcuts import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .forms import SignUpForm,UserEditForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from users.models import Reviews
from django.http import JsonResponse
import json
# neha valiya jfalj@jdslfjk

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                success=f"You have succesfully SignUp..."
                return JsonResponse({'message': success,"errors":''}, status=200)
            except Exception as err:
                return JsonResponse({'message': "we are not able to register your account at this moment please try again after sometime","errors":"server error\n"}, status=200)
            # messages.success(request, success)
            # return redirect('/users/profile')
        else:
            return JsonResponse({'message': "errors",'errors': form.errors}, status=200)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    # return HttpResponse("signup")

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                success=f"You have Successfully sign in..."
                messages.success(request, success)
                return redirect('/users/profile')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})
    # return HttpResponse("signin")

def signout(request):
    # return HttpResponse("signout")
    logout(request)
    success=f"You Have Signout the website..."
    messages.success(request, success)
    return redirect('/users/signin')

@login_required
def profile(request):
    user = request.user
    reviews = Reviews.objects.filter()
    context = {
        "title":"Profile page",
        'user': user,
        "reviews":reviews,
    }
    context["form"] = UserEditForm(instance=user)
    return render(request=request, template_name='viewbio.html', context=context)

@login_required
def changepassword(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user=user,data=request.POST)
        # print(form.non_field_errors())
        # return HttpResponse("submit")
        if form.is_valid():
            user = form.save()
            login(request, user)
            success=f"Your password has Now changed"
            messages.success(request, success)
            return redirect('/users/profile')
        # else:
        #     print("Form errors:", form.errors)  
    else:
        form = PasswordChangeForm(user)
    context={
        'user': user,"form":form,
        "page":"Change Password",
        "name":"ChangePassword",
    }
    return render(request=request, template_name='changepassword.html', context=context)

def reviews(request):
    context = {
        "title":"Add Review",
        "name":"reviews",
        "page":"Reviews",
    }
    form = ReviewForm()
    if request.user.is_authenticated:
        context["title"] = "Edit Review"
        reviews = Reviews.objects.filter(author=request.user.username).first()
        if reviews:
            data={
                "author":reviews.author,
                "rating":reviews.rating,
                "comment":reviews.comment,
            }
            form = ReviewForm(data=data)

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if request.user.is_authenticated:
            if reviews:
                form = ReviewForm(request.POST, instance=reviews)
        if form.is_valid():
            form.save()
            success=f"Your Review has Been Submitted"
            messages.success(request, success)
            return redirect('/users/profile')

    context["form"]=form
    if request.user.is_authenticated:
        context["username"]=request.user.username
        context["email"]=request.user.email

    return render(request, 'formsformat.html', context=context)

# @login_required
# @csrf_exempt
# def changedetails(request):
#     user = request.user
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             form = UserEditForm(data, instance=request.user)
#             if form.is_valid():
#                     user = form.save()
#                     login(request, user)
#                     success=f"Your Details Had Been Changed"
#                     return JsonResponse({'message': success,"errors":False}, status=200)
#                 # messages.success(request, success)
#                 # return redirect('/users/profile')
#             else:
#                 return JsonResponse({'message': form.errors,"errors":True}, status=404) 
#         except Exception as err:
#             return JsonResponse({'message': "There is error","errors":True}, status=404)
#     else:
#         return JsonResponse({'message': "Not Allowed","errors":True}, status=404)
    
@login_required
def changedetails(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            success=f"Your Details Had Been Changed"
            # return JsonResponse({'message': success,"errors":False}, status=200)
            messages.success(request, success)
            return redirect('/users/profile')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'changedetails.html', {'form': form})

    # user = request.user
    # if request.method == 'POST':
    #     form = UserEditForm(request.POST, instance=request.user)
    #     if form.is_valid():
            
    # else:
    #     form = UserEditForm(request, instance=request.user)
    #     context = {
    #     "title":"Change Deatils",
    #     "name":"Change Details",
    #     "page":"Edit Profile",
    #     "form": form,
    # }
        # return render(request=request, template_name="changedetails.html",context=context)
    