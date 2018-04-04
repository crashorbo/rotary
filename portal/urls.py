from django.conf.urls import url

from .views import IndexView, RegistroView, create_parent, create_parents

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^inscripcion-ajax/$', create_parent, name='registro_ajax'),
    url(r'^inscripcions-ajax/$', create_parents, name='registros_ajax'),
]