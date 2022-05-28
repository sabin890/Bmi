
from django.shortcuts import redirect, render
from .forms import Bmform, Login
from .models import Bmi
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, "home/landing.html")


def bmi(request):
    def Bmcalculate(result):
        if result <= 18.5:
            return "your bmi is 18.5, then it means that you are underweight. To avoid health complications that may arise due to low levels of body fat, you need to put on more weight. Make sure you get in touch with your doctor or a dietician for professional insight and advice."
        elif result >= 18.5 and result <= 24:
            return "you have a BMI that falls in between 18.5 to 23.9, then it means that you have a healthy weight in relation to your height. This is your normal BMI range. When you maintain a healthy level of body fat, it means that you have a much lower risk of developing health complications."
        elif result >= 24 and result <= 29.9:
            return "you have a BMI that falls in between 24.0 to 29.8, it means that you are overweight. In other words, you have a higher than ideal level of body fats considering your height. In such cases, it is important that you lose some amount of weight in order to improve your health. It is recommended that you talk to a doctor or dietician for professional advice"
        elif result > 30:
            return "your BMI is more than 30.0, then it indicates that you are obese, or in other words, heavily overweight. It is far from your ideal BMI and it means that you have way too much body fat in relation to your height, and this can pose serious health risks. It is important that you lose weight for health reasons. Make sure to contact your doctor or dietician for professional advice in such a situation."
    if request.method == "POST":
        fm = Bmform(request.POST)
        if fm.is_valid:
                weight = float(request.POST["weight"])
                height = float(request.POST["hight"])
                age = int(request.POST["age"])
                if age <= 18:
                    messages.warning(
                        request, "Your age is less than 18 so we cant calculate your BMI!!!")
                    fm = Bmform()
                    return render(request, 'home/home.html', {'bm': fm})

                result = round((weight/(height*0.3048)**2), 2)
                fb = Bmcalculate(result)
                cg = fm
                cg.suggest = fb
                cg.result = result
                request.session["height"] = height
                request.session["wieght"] = weight
                request.session["age"] = age
                request.session["result"] = result
                request.session["suggest"] = fb
                return render(request, 'home/Bmi.html', {'bm': fm, "fb": fb, "result": result})
    else:
        fm = Bmform()
        return render(request, 'home/Bmi.html', {'bm': fm})


def singup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password1 = request.POST.get('password2')
        if User.objects.filter(username=username).first():
            messages.warning(
                request, 'The username you entered is already exist!!!')
            return redirect('abc')
        elif User.objects.filter(email=email).first():
            messages.warning(
                request, 'The Email address you entered is already exist!!!')
            return redirect('abc')
        else:
            user_obj = User(username=username, email=email)
            if password == password1:
                user_obj.set_password(password)
                user_obj.save()
                return redirect('login')
    else:
        return render(request, "home/singup.html")


def log_in(request):
    if request.method == "POST":
        fm = Login(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        fm = Login()
    return render(request, "home/login.html", {"form": fm})


def sv(request):
    height = request.session["height"]
    wieght = request.session["wieght"]
    age = request.session["age"]
    result = request.session["result"]
    suggest = request.session["suggest"]
    bmi_save = Bmi(hight=height, weight=wieght, age=age,
                   result=result, suggest=suggest, user=request.user)
    bmi_save.save()
    messages.success(request, "You Data has been successfully saved!!")
    return redirect("bmi")


def log_out(request):
    logout(request)
    return redirect("login")


def profile(request):
    fm = Bmi.objects.filter(user=request.user)
    return render(request, "home/profile.html", {'fm': fm, })


def delete(request, id):
    fm = Bmi.objects.get(pk=id)
    fm.delete()
    messages.error(request, "You Data has been Deleted!!")
    return redirect("profile")
