from .views import *
from django.urls import path


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('aboutipssm', aboutipssm, name='aboutipssm'),
    path('aboutsrinivas', aboutsrinivas, name='aboutsrinivas'),
    path('logistics', logistics, name='logistics'),
    path('port', port, name='port'),
    path('mba', mba, name='mba'),
    path('contact', contact, name='contact'),
    path('events', events, name='events'),
    path('events/<pk>', eventview, name='eventdetails'),
    path('faculty', faculty, name='faculty'),
    path('gallery', gallery, name='gallery'),
    path('placement', placement, name='placement'),
    path('Faculty-Achivements', tchach, name='tchach'),
    path('Student-Achivements', stdach, name='stdach'),
]