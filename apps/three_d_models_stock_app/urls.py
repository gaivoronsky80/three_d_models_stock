from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^results$', views.search, name="search"),
    url(r'^register_process$', views.register_process),
    url(r'^login_process$', views.login_process),
    url(r'^admin$', views.admin),
    url(r'^admin_control/(?P<id>\d+)$', views.admin_control),
    url(r'^user_page$', views.user_page),
    url(r'^add_edit_user_page/(?P<id>\d+)$', views.add_edit_user_page),
    url(r'^delete_user_profile/(?P<id>\d+)$', views.delete_user_profile),
    url(r'^add_new_model$', views.add_new_model),
    url(r'^add_update_model/(?P<id>\d+)$', views.add_update_model),
    url(r'^model_info/(?P<id>\d+)$', views.model_info),
    url(r'^session_home$', views.session_home),
    url(r'^category$', views.category),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^logout$', views.logout),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)