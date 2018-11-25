from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')




# class FormName(forms.Form):
# 	text = forms.CharField(max_length=140, widget=forms.Textarea)
# 	date = forms.DateField()
# 	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

# 	def clean(self):
# 		# all_clean.. is a dictionary
# 		all_clean_data = super().clean()



class FormTweetbyId(forms.Form):
	text = forms.CharField(max_length=140, widget=forms.Textarea)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		# all_clean.. is a dictionary
		all_clean_data = super().clean()
		return all_clean_data