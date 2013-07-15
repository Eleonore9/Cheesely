from django.conf.urls import patterns, url

from cheeses import views

urlpatterns = patterns('',
    # URL pattern for the CheeseListView
    url(
        regex=r'^$',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    # URL pattern for the CheeseDetailView
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
)

