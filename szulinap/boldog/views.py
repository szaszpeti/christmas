from django.shortcuts import render
from .forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Counter
# Create your views here.


counter = 0

def index(request):

    return render(request, 'boldog/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        # Check to see  form is valid
        if user_form.is_valid():

            user = user_form.save()  # Save User Form to Databas
            user.set_password(user.password)  # Hash the password
            user.save()  # Update with Hashed password
            registered = True  # Registration Successful!

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'boldog/register.html',
                  {'user_form': user_form,
                   'registered': registered,
                   })




def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('boldog:welcome'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'boldog/login.html', {})


@login_required
def welcome(request):
    usern = request.user.username


    return render(request, 'boldog/welcome.html', {'username':usern})


@login_required
def feladat(request):

    return render(request, 'boldog/feladat.html')

@login_required
def q1(request):
    answere = request.GET.get("q")
    if answere == "e":
        return HttpResponseRedirect(reverse('boldog:q2_64738'))

    return render(request, 'boldog/q1.html')


@login_required
def q2_64738(request):
    a = request.GET.get("q2")
    print (a)
    if a == "g":
        return HttpResponseRedirect(reverse('boldog:q3_23491723'))

    return render(request, 'boldog/q2_64738.html')

@login_required
def q3_23491723(request):
    a = request.GET.get("q3")
    print (a)
    if a == "a":
        return HttpResponseRedirect(reverse('boldog:q4_98362527'))
    return render(request, 'boldog/q3_23491723.html')


@login_required
def q4_98362527(request):
    a = request.GET.get("q4")

    global counter
    if counter < 3:
        print(counter)
        if a == "ae":
            return HttpResponseRedirect(reverse('boldog:ajandek'))
        else:
            counter =+ 1
            return render(request, 'boldog/q4_98362527.html')

    return HttpResponseRedirect(reverse('boldog:failed'))


def failed(request):

    return render(request, 'boldog/failed.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'boldog/login.html')

@login_required
def ajandek(request):
    usern = request.user.username
    return render(request, 'boldog/ajandek.html',{'username':usern})

def by(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'boldog/by.html')