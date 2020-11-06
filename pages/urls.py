from django.urls import path,re_path

from . import views
from .views import ErrorTemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    re_path(r"^.*$", ErrorTemplateView.as_view(), name='entry-point'),
]