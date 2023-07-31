from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyRegisterForm(UserCreationForm):
    ''' Create a new user registration form based on Bulit-in one. This form will have email address field additional'''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# dodaje 1 komentarz - będzie merga do develop
# dodaje 2 komentarz - drugi push 
# dodaje 3 komentarz - trzeci push

# checking4 - 1st
# checking 4 # 2nd

#dodane w checking 10 i bedzie merg z checking9

# adding something 

# adding somethin2 - branch myBranch - file branches

# added - branchesProjekt - branch my Branch

# added - branches - branch my Branch 

# added - branches - branch my Branch - one more time.

#checking

