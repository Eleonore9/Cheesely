from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
	model = User

	# Constrain the UserForm to just these fields.
	fields = ("tagline", "first_name", "last_name", "email")
