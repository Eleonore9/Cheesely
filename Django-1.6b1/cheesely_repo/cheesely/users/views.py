from django.shortcuts import render
# Import the detail view
from django.views.generic import DetailView
# Import the customized User model
from .models import User

class UserDetailView(DetailView):
	model = User
	# index lookups by username
	slug_field = "username"
	slug_url_kwarg = "username"

from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
# Only authenticated users can access views
from braces.views import LoginRequiredMixin

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    # send the user back to their own page after a successful update
    def get_success_url(self):
	    return reverse("users:detail",
			    kwargs={"username": self.request.user.username})
    def get_object(self):
	    # only get the User record for the user making the request
	    return User.objects.get(username=self.request.user.username)
