from django.views.generic import TemplateView
from django.apps import apps

#--TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
