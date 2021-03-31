from loginmodule.views import login, auth_view, logout,loggedin, invalidlogin,registration,admin,modify,modified
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout),
    url(r'^loggedin/$', loggedin),
    url(r'^invalidlogin/$', invalidlogin),
    url(r'^registration/$', registration),
    url(r'^admin/$', admin),
    url(r'^modify/$', modify),
    url(r'^modified/$', modified),
]
