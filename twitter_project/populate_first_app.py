import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter_project.settings')

import django
django.setup()

# Fake populate script
import random
from faker import Faker
from first_app.models import User, Tweet, UserProfileInfo

fakegen = Faker()



def populate(N=5):
	for nb_user in range(N):
		user_fake_username = fakegen.user_name()
		user_fake_email = fakegen.email()
		user_fake_password = fakegen.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

		user = User.objects.get_or_create(username=user_fake_username ,email=user_fake_email , password=user_fake_password)[0]

		user_fake_bio = fakegen.text(max_nb_chars=400, ext_word_list=None)

		userprofileinfo = UserProfileInfo.objects.get_or_create(user=user, bio=user_fake_bio)[0]

		for nb_tweets in range(random.randint(0, 25)):
			tweet_fake_text = fakegen.text(max_nb_chars=140, ext_word_list=None)
			tweet_fake_date = fakegen.date()

			tweet = Tweet.objects.get_or_create(text=tweet_fake_text, date=tweet_fake_date, user=userprofileinfo)[0]




if __name__ =='__main__':
	print('Startiing to populate....')
	populate(25)
	print('Finished populating!')

