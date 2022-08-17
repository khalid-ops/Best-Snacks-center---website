from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("login_user", views.login_user, name='login_user'),
    path("logout_user", views.logout_user, name='logout_user'),
    path("snacks", views.rapi_snack, name='rapi_snack'),
    #rest api urls
    path("north", views.north_filter, name='north_filter'),
    path("south", views.south_filter, name='south_filter'),
    path("inter", views.inter_filter, name='inter_filter'),
    path("contactapi", views.contactapi, name='contactapi'),
    path("search", views.search_filter.as_view()),
   
# rest api urls
    path("n_display", views.n_display, name='n_display'),
    path("s_display", views.s_display, name='s_display'),
    path("i_display", views.i_display, name='i_display'),
    path("search_display", views.search_display, name='search_display'),
    path("con_display", views.con_display, name='con_display'),
    path("feedback", views.feedbacksend_mail, name='feedbacksend_mail'),
    path("signup", views.signup, name='signup')


]