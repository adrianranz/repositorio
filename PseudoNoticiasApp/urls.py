from django.urls import path, include

from PseudoNoticiasApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name="Home"),

    path('whoweare', views.whoweare, name="Quienes Somos"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)