from django.shortcuts import render
from django.views import generic as views


class LandingPageView(views.TemplateView):
    template_name = 'landing_page.html'
