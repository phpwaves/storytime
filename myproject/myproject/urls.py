from django.conf.urls import patterns, include, url
from story.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', 'story.views.home', name='home'),
	url(r'^$', 'story.views.home_page', name='home_page'),
	url(r'^home_page$', 'story.views.home_page', name = 'home_page'),
	url(r'^zomato/$', 'story.views.zomato', name='zomato'),
	url(r'^language/(?P<language>[a-z\-]+)/$', 'story.views.language', name='language'),
	url(r'^activities/$', 'story.views.activities', name='activities'),
	url(r'^all_details/$', 'story.views.all_details', name='all-details'),
	url(r'^hunch_page/$', 'story.views.hunch_page', name='hunch_page'),
	url(r'^sosh_page/$', 'story.views.sosh_page', name='sosh_page'),
	url(r'^login/$', 'story.views.login', name='login'),
	url(r'^auth/$', 'story.views.auth_view', name='auth_view'),
	url(r'^logout/$', 'story.views.logout', name='logout'),
	url(r'^loggdein/$', 'story.views.loggedin', name='loggedin'),
	url(r'^invalid_login/$', 'story.views.invalid_login', name='invalid_login'),
	url(r'^register/$', 'story.views.register_user', name='register_user'),
	url(r'^register_success/$', 'story.views.register_success', name='register_success'),
	url(r'^profile/$', 'story.views.profile', name='profile'),
	url(r'^favItem/$', 'story.views.favItem', name='favItem'),
	url(r'^starred_items/$', 'story.views.starred_items', name='starred_items'),
	url(r'^profile_update/$', 'story.views.profile_update', name='profile_update'),
	#url(r'^profile/$', 'story.views.user_profile', name='profile'),
	url(r'^restaurants/$', 'story.views.restaurants', name='restaurants'),
	#url(r'^storytime/', include('storytime.foo.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
