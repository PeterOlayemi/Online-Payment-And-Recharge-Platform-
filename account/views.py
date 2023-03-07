from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponseRedirect, HttpResponse

from .models import Myuser
from .forms import RegisterForm, MyuserForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

# Create your views here.

def password_reset_request(request):
	msg = None
	password_reset_form = PasswordResetForm(request.POST or None)
	if request.method == "POST":
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "account/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'account',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'olayemipeter2005@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
			else:
				msg = 'Email does not exist'
	return render(request=request, template_name="account/password/password_reset.html", context={"password_reset_form":password_reset_form, 'msg':msg})

@login_required
def profile(request):
    data = Myuser.objects.filter(owner=request.user)
    return render(request, 'account/profile.html', {'data':data})

def myuser(request):
    if request.method != 'POST':
        form = MyuserForm()
    else:
        # Process completed form.
        form = MyuserForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner=request.user
            message.save()
            return HttpResponseRedirect(reverse('account:login'))
    context = {'form': form}
    return render(request, 'account/myuser.html', context)

def signup(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        # Process completed form.
        form = RegisterForm(data=request.POST)
 
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('account:myuser'))

    context = {'form': form}
    return render(request, 'account/signup.html', context)

def signout(request):
    logout(request)
    return redirect('data:home')

@login_required
def welcome(request): 
    return render(request, 'account/welcome.html')

def term(request):
    return render(request, 'account/terms.html')

def privacy(request):
    return render(request, 'account/privacy.html')
