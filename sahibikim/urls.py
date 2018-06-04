
from django.contrib import admin
from django.urls import path
from cars import views as cars_view
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', cars_view.home_view),
    url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^hallettim/$', cars_view.home_view),
    url(r'^bildirim/$', cars_view.search),
    url(r'^searchform/$', cars_view.search_form),
    url(r'^search/$', cars_view.search),
    url(r'^success/$', cars_view.success),
    url(r'^signup/$', cars_view.signup, name='signup'),
    url(r'^aracform/$', cars_view.arac_create, name='arac'),
]
