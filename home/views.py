from django.shortcuts import render, HttpResponse
import requests
from datetime import datetime, timezone, timedelta
import json
from django.conf import settings
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MyForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == "POST":
        city = str(request.POST.get('city'))

        # Enter your "openweathermap.org" API_KEY below
        api_key = settings.API_KEY
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        data = requests.get(url).json()
        try:
            if data['cod'] == '404':
                return HttpResponse('{"status": "notfound"}')
            else:
                city_name = data['name']
                country = data.get('sys').get('country', '-')
                ts = data['dt']
                tzone = data['timezone']
                date_time = datetime.fromtimestamp(ts, tz=timezone(timedelta(seconds=tzone))).strftime('%Y-%m-%d')
                temp = int(data['main']['temp'])
                temp_F = format((temp*1.8)+32, '.1f')
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                feels_like = int(data['main']['feels_like'])
                wind = format(data['wind']['speed']*3.6, '.1f')
                visibility = format(data['visibility']/1000, '.2f') 

                context = {'status': 'success', 'city': city_name, 'country': country, 'date_time':date_time, 'temp': temp, 'temp_F': temp_F, 'description': description, 'humidity': humidity, 'feels_like': feels_like, 'wind': wind, 'visibility': visibility}
                return HttpResponse(json.dumps(context))
        except:
            return HttpResponse('{"status": "error"}')
            

    return render(request, 'pages/weatherApp.html')

def home(request):
    return render(request, 'pages/home.html')
def portfolio(request):
    return render(request, 'pages/portfolio.html')

def convertor_view(request):
    form = MyForm()
    return render(request, 'pages/text-to-html.html', {'form': form})

def calories_counter(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': settings.CALORIES_API_KEY})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'pages/calories-counter.html', {'api': api})
    else:
        return render(request, 'pages/calories-counter.html', {'query': 'Enter a valid query'})
    
class todo_list(LoginRequiredMixin, generic.ListView):
    template_name = 'pages/todo.html'
    context_object_name = 'todo_list'
    login_url = 'account_login'  # Replace with your login URL

    def get_queryset(self):
        """Return all the latest todos for the authenticated user."""
        if self.request.user.is_authenticated:
            queryset = Todo.objects.filter(user=self.request.user).order_by('-created_at')
        else:
            queryset = Todo.objects.none()  # An empty queryset if the user is not authenticated
        return queryset
def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title,user=request.user)

    return redirect('home:todo_list')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('home:todo_list')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('home:todo_list')
def blog(request):
    if request.method == "POST":
        if 'title' in request.POST:
            title = request.POST["title"]
            content = request.POST["content"]
            q = Post(author=request.user, title=title, content=content)
            q.save()
            messages.success(request, "Blog has uploaded!")
        elif 'like' in request.POST:
            blog_id = list(request.POST.keys())[1]
            blog = Post.objects.filter(id=blog_id)
            blog.like += 1
            blog.save()
            messages.success(request, "Blog has uploaded!")
        else:
            blog_id = list(request.POST.keys())[1]
            del_blog = Post.objects.filter(id=blog_id)
            del_blog.delete()
            messages.success(request, "Blog removed from Uploaded!")

    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'pages/blog_page.html', context=context)



@login_required(login_url='login')
def blog_upload(request):
    if request.method == "POST":
        if 'title' in request.POST:
            name = request.POST["title"]
            content = request.POST["content"]
            q = Post(author=request.user, title=title, content=content)
            q.save()
            messages.success(request, "Blog has uploaded!")
        else:
            blog_id = list(request.POST.keys())[1]
            del_blog = Post.objects.filter(user=request.user, id=blog_id)
            del_blog.delete()
            messages.success(request, "Blog removed from Uploaded!")


    blogs = Post.objects.all()
    context = {'blogs': blogs}
    return render(request, 'pages/blog_page.html', context=context)