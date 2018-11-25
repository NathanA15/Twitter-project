Ffrom django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Tweet
from django.contrib.auth import authenticate, login
from . import forms
import datetime
now = datetime.datetime.now()




def get_lasts_tweets(n_tweets):
	pass
	# tweets = {
	# 	'list': Tweet.objects.all().order_by('-date')[:n_tweets],
	# }

	# return tweets

def get_all_user_tweet(user_id):
	pass
	# tweets = {
	# 	'list': Tweet.objects.filter(user  = user_id)
	# }
	# return tweets




# Create your views here.
def index(request):
	pass
	# must create a function to get the 20 last tweets with their author.
	# return render(request, 'index.html', context=get_lasts_tweets(20))


def user_info(request, user_id):
	pass
	# return render(request, 'profile.html', context=get_all_user_tweet(user_id))


def form_user_view(request):
	pass
	# form = forms.FormName()
	# if request.method == 'POST':
	# 	form = forms.FormName(request.POST)
	# 	if form.is_valid():
	# 		# make sure that we are actually saving to the database
	# 		form.save(commit=True)
	# 		return index(request)
	# 	else:
	# 		print("Error - form is invalid")
	
	# return render(request, 'form.html', {'form': form}) 


def form_user_id_view(request, user_id):
	pass
	# user = User.objects.get(id=user_id)
	# form = forms.FormTweetbyId()
	# if request.method == 'POST':
	# 	form = forms.FormTweetbyId(request.POST)
	# 	# print(form['text'])
	# 	if form.is_valid():
	# 		# make sure that we are actually saving to the database
	# 		twt = Tweet(text=form.clean()['text'], date=now, user=user)
			
	# 		twt.save()
	# 		return index(request)
	# 	else:
	# 		print("Error - form is invalid")
	
	# return render(request, 'form.html', {'form': form, 'user': user }) 


def signup(request):
	registered = False
	
	if request.method == 'POST':
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				print(request.FILES)
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()
			registered = True

		else:
			print(user_form.errors, profile_form.errors)
 
	else:
		user_form = forms.UserForm()
		profile_form = forms.UserProfileInfoForm()

	return render(request, 'signup.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
		})
			

# def login(request):
# 	username = request.POST['username']
# 	password = request.POST['password']




