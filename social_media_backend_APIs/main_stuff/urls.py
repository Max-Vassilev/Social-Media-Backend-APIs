from django.urls import path
from social_media_backend_APIs.main_stuff.views import *

urlpatterns = [

    path("", LandingPageView.as_view(), name="landing page view"),

]
