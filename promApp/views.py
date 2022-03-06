from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CreateProfileForm, CreatePromDateForm
from .models import Profile, PromDate

# Create your views here.

def index(request):
    return render(request, 'promApp/index.html')

def about(request):
    return render(request, 'promApp/about.html')

def handler404(request, exception):
    return render(request, 'promApp/err404.html', status=404)
    
def handler500(request, *args, **argv): 
    return render(request, 'promApp/err500.html', status=500)

def sorry(request):
    return render(request, "promApp/sorry.html")

def guide(request):
    return render(request, "promApp/guide.html")

@login_required(login_url="/google/login")
def app(request):
    if request.method == "POST":
        if "profile" in request.POST:
            profileForm = CreateProfileForm(data=request.POST)
            if profileForm.is_valid():
                profile = profileForm.save(commit=False)
                profile.owner = request.user               
                profile.save()
                return redirect("promApp:app")
        elif "crush" in request.POST:
            
            crushNameList = PromDate.objects.filter(profile=Profile.objects.filter(owner=request.user).first()).values_list('name', flat=True)
            
            crushName = request.POST['name'].title().strip()
            crushYear = request.POST['year']
            # if inputted name is same as self
            if crushName == request.user.get_full_name():
                return redirect("promApp:app")
            
            # if inputted name already inputted
            if crushName in crushNameList:
                return redirect("promApp:app")
            
            if crushYear == "FR" or crushYear == "SO":
                return redirect("promApp:sorry")
            
            crushForm = CreatePromDateForm(data=request.POST)
            if crushForm.is_valid():
                crusher = Profile.objects.filter(owner=request.user).first()
                crush = crushForm.save(commit=False)
                crush.profile = crusher
                crush.name = crushName
                crush.save()
                return redirect("promApp:app")
        
        return render(request, "promApp/app.html", context={})
    else:
        profileNotCreated = len(Profile.objects.filter(owner=request.user)) == 0
        profileForm = CreateProfileForm()
        crushForm = CreatePromDateForm()

        if not profileNotCreated:

            crusher = Profile.objects.filter(owner=request.user).first()
            
            if crusher.year == "FR" or crusher.year == "SO":
                return redirect("promApp:sorry")

            remaining = 5-PromDate.objects.filter(profile=crusher).count()

            crushList = PromDate.objects.filter(profile=crusher).all()
            crushingOnMe = PromDate.objects.filter(name=request.user.get_full_name(), year=crusher.year)

            numCrushing = crushingOnMe.count()

            matches = []
            for person in crushingOnMe:
                for crush in crushList:

                    if (person.profile.owner.get_full_name() == crush.name) and (crush.year == person.profile.year):
                        matches.append((crush.name, person.profile.year))
            
            
            context = {
                "remaining" : remaining,
                "matches" : matches,
                "profileNotCreated" : profileNotCreated,
                "profileForm" : profileForm,
                "crushForm" : crushForm,
                "crushList": crushList,
                "numCrushing" : numCrushing,
            }
        else:
            
            context = {
                "profileNotCreated" : profileNotCreated,
                "profileForm" : profileForm,
                "crushForm" : crushForm,
            }

        return render(request, "promApp/app.html", context=context)





