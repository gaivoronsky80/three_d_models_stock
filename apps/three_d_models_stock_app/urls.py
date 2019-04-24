from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^user_page/(?P<id>\d+)$', views.user_page),
    url(r'^add_new_model$', views.add_new_model),
    url(r'^new_model_page$', views.new_model_page),
    url(r'^model_page$', views.model_page),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)