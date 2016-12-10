from django.apps import apps

class App():
    def __init__(self,name,url):
        self.name = name
        self.url = url


def getAll():
    applist = []
    for application in apps.get_app_configs():
        if application.name.startswith("django") == False and application.name.startswith("chip") == False:
            applist.append(App(application.name_menu, application.name+"/"))
    return applist
