from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=400)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return self.user.username


class Tweet(models.Model):
	text = models.CharField(max_length=140, unique=False)
	date = models.DateField()
	user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)


	def __repr__(self):
		return "<Tweet {}>".format(self.text[10])

	def __str__(self):
		return self.text[0:15]
