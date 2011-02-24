from django.conf.urls.defaults import *

from django.views.generic import TemplateView
from sleeptracker.views import UserView

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name="sleeptracker/landing_page.html")),
    (r'^(?P<username>\w+)$', UserView.as_view()),
)
