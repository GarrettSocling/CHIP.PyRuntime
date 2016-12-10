from django.shortcuts import render
import chip.AppsInfo

# Create your views here.

def index(request):
    apps = chip.AppsInfo.getAll()
    context = {
        'apps':apps
    }
    return render(request, 'smsgw/index.html', context)

def listInbox(request):
    pass