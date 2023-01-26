from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    views = {}
    views['tables'] = Table.objects.all()
    views['final'] = Finale.objects.all()
    views['winner'] = Wcup.objects.all()
    views['players'] = Stat.objects.all()

    return render(request, 'index.html',views)

def contact(request):
    views ={}
    views['infos'] = Information.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name= name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        views['mess'] = 'The message is submitted!'
        return render(request, 'contact.html',views)

    return render(request, 'contact.html',views)

def blog(request):
    views ={}
    views['blogs'] = Blog.objects.all()

    return render(request, 'blog.html',views)

def match(request):
    views = {}
    views['games'] = Upcoming.objects.all()
    views['final'] = Finale.objects.all()
    views['players'] = Stat.objects.all()

    return render(request, 'matches.html',views)


def player(request):
    views = {}
    views['players'] = Stat.objects.all()

    return render(request, 'players.html',views)

def single(request):
    return render(request, 'single.html')



