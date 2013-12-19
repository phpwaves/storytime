from django.shortcuts import render_to_response,get_object_or_404
from django.db import models
from .models import Line, ZomatoItem, user_profile, FavItems
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import user_profile_form, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

def login(request):
    c = {}
    c.update(csrf(request))
    render_to_response("story/login.html", c) 

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/all_details', {'username':username})
    else:
        return HttpResponseRedirect('/invalid')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
	
def loggedin():
    return render_to_response('loggedin.html', 
                              {'full_name': request.user.username})

def invalid_login():
    return render_to_response('invalid_login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')
        else:
            return HttpResponseRedirect('/invalid_login')
        
    args = {}
    args.update(csrf(request))
        
    args['form'] = UserCreationForm()
    return render_to_response('story/register.html', args)

def register_success(request):
    return render_to_response('story/register_success.html')

def home_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')
        else:
            return HttpResponseRedirect('/invalid_login')

    args = {}
    args.update(csrf(request))
        
    args['form'] = UserCreationForm()
    #args['user']  = request.user
    return render_to_response('story/home_page.html', args)


@login_required
def profile(request):
	if request.method == 'POST':
		form = user_profile_form(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/all_details')
	else:
		user = request.user
		profile = user.profile
		form = user_profile_form(instance=profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['user'] = user
	return render_to_response('story/profile.html', args)
	

@login_required
def profile_update(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			form.save_m2m() # needed since using commit=False
			return HttpResponseRedirect('/all_details')
	else:
		user = request.user
		profile = user.profile
		form = ProfileForm(instance=profile)
	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['user'] = request.user
	return render_to_response('story/profile.html', args)

@csrf_exempt	
def favItem(request):
	if request.user.is_authenticated():
		url_id = request.POST['client_response']
		fav_name = request.POST['fav_name']
		user_id = request.user
		#object_to_edit = get_object_or_404(ZomatoItem,id=url_id)
		dup = FavItems.objects.filter(user=request.user).filter(fav_choices_id=url_id)
		response_dict = {}
		response_dict.update({'article': url_id})
		if dup:
			response_dict.update({'fav_name': ' Item has already been added'})
			json_data = simplejson.dumps(response_dict)
			return HttpResponse(json_data, mimetype='application/json')
		else:
			p = FavItems(user=request.user)
			p.fav_choices_id=url_id
			p.save(force_insert=True)
			response_dict.update({'fav_name': fav_name+' added to your fav items'})
			json_data = simplejson.dumps(response_dict)
			return HttpResponse(json_data, mimetype='application/json')
			

def starred_items(request):
	if request.user.is_authenticated():
		user_id = request.user
		#favItems = FavItems.objects.filter(user=user_id).distinct()
		favItems = FavItems.objects.filter(user=user_id).distinct()
		return render_to_response('story/starred_items.html', {'favItems': favItems})
		
	
def restaurants(request):
    return render_to_response('story/restaurants.html')


def home(request):
    language = 'en_gb'
    session_language = 'en_gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response("story/home.html", {'lines': Line.objects.all(), 'language' : language, 'session_language' : session_language, 'user':request.user})

def zomato(request):
    return render_to_response("story/zomato.html", {'z_items' : ZomatoItem.objects.all()})

def language(request, language = 'en_gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response

def activities(request):
    return render_to_response('story/activities.html', {'activities': ZomatoItem.objects.all().filter(activity__icontains="Activities")})

def all_details(request, **kwargs):
	if request.user.is_authenticated():
		return render_to_response("story/all_details.html", {'z_items' : ZomatoItem.objects.all()[:15], 'user':request.user})

def sosh_page(request):
	return render_to_response("story/sosh_page.html")
	
def hunch_page(request):
	return render_to_response("story/hunch_page.html")

def restaurants(request):
	items_list = list(ZomatoItem.objects.filter(id__range = (1,11)))
	return render_to_response('story/restaurants.html', {'z_items' : items_list})

def games(request):
	return render_to_response('story/games.html')

def shopping(request):
	return render_to_response('story/shopping.html')


"""

def hunch_page(request):
    return render_to_response("story/hunch_page.html")

def sosh_page(request):
    return render_to_response("story/sosh_page.html")
	
def all_details(request, **kwargs):
	if request.user.is_authenticated():
		username = kwargs
		return render_to_response("story/all_details.html", {'z_items' : ZomatoItem.objects.all()[:15], 'user':request.user})

@login_required
def profile_backup(request):
    if request.method == 'POST':
        form = user_profile_form(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all_details')
        else:
            return HttpResponseRedirect('/home_page')
    else:
        user = request.user
        profile = user.profile
        form = user_profile_form(instance=profile)
    

	
def importitems(request):
    f = open('/Users/rmittal/webapp/ENV/bin/storytime/initial_data.json', 'r')
    obj = json.load(f)
    for o in object:
        record = ZomatoItem
"""
