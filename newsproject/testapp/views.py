from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'testapp/base.html')

def home_view(request):
    return render(request,'testapp/home.html')

def movies_view(request):
    return render(request,'testapp/movies.html')

def politics_view(request):
    return render(request,'testapp/politics.html')

def sports_view(request):
    return render(request,'testapp/sports.html')                 
