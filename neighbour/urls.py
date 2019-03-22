from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.landing,name='landing'),
    url(r'^profile',views.profile,name='profile'),
    url(r'editdp',views.editdp,name='editdp'),
]
