from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

users = User.objects.all()
for user in users:
    Token.objects.filter(user=user).delete()
