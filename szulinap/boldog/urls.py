from django.conf.urls import url
from boldog import views

# SET THE NAMESPACE!
app_name = 'boldog'

urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^welcome/$',views.welcome,name='welcome'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^ajandek/$',views.ajandek,name='ajandek'),
    url(r'^feladat/$', views.feladat, name='feladat'),
    url(r'^failed/$', views.failed, name='failed'),
    url(r'^q1/$', views.q1, name='q1'),
    url(r'^q2_64738/$', views.q2_64738, name='q2_64738'),
    url(r'^q3_23491723/$', views.q3_23491723, name='q3_23491723'),
    url(r'^q4_98362527/$', views.q4_98362527, name='q4_98362527'),
    url(r'^by/$',views.by,name='by'),

]