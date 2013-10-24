from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('', 

	# URL pattern for the UserDetailView
	url(
	    regex=r'^(?P<username>[\w\-_]+)/$',
	    view=views.UserDetailView.as_view(),
	    name='detail'
	),
	# URL pattern for the UserUpdateView
	url(
	    regex=r'^~edit/$',
	    view=views.UserUpdateView.as_view(),
	    name='update'
	),
)
