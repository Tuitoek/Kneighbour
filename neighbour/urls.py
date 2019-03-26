from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.landing,name='landing'),
    url(r'^profile',views.profile,name='profile'),
    url(r'editdp',views.editdp,name='editdp'),
    url(r'home',views.home,name='home'),
    url(r'editdp',views.editdp,name='editdp'),
    url(r'profile',views.profile,name='profile'),
    url(r'business',views.business,name='business'),
    url(r'events',views.events,name='events'),
    url(r'^search/',views.search_hoods,name='search_hoods'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
