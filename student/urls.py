from django.conf.urls import url

from .views import IndexView


name_space = 'student'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]