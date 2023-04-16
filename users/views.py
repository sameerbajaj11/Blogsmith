from django.shortcuts import render, redirect

# We created our form object using this class.
from django.contrib.auth.forms import UserCreationForm

# Flash messages were displayed using this message function.
from django.contrib import messages

# our userregister form created
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# importing login required decorator
from django.contrib.auth.decorators import login_required

def register(request):
    # creating the form if we ge the post request
    if request.method == 'POST':

        # I want to create a form that will receive the data that was within the post request
        # here request.POST is being used, to pass in the POST data(whatever user enters.)
        form = UserRegisterForm(request.POST)

        # Validating the form, like if the user already exists, passwords fields don't match etc.
        if form.is_valid():

            # Cresting the user if the form is valid, to create the user in our DB.
            form.save()

            username = form.cleaned_data.get('username')

            # messages.success(request, f'Account created for {username}!')
            # return redirect('blog-home')

            # Redirecting the users to the login page to login, after they've successfully registered.
            messages.success(request, f'Your account has been created!, You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# user needs to login in order to view this profile.
@login_required
def profile(request):

    if request.method == 'POST':
        # adding the forms to update username, email and profile picture.
        # Then we pass the instances of the objects it expects, to set a placeholder.
        # request.FILES, in case the user updates the profile picture as well.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!.')
            
            # This profile redirection is implemented under 'the POST-GET redirect pattern'
            # Check out out using chatgpt if you can't recall. It's for enhancing the UX.
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)






        
