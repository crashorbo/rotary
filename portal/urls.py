from django.conf.urls import url

from .views import IndexView, AdministracionView, create_parent, create_parents

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^inscripcion-ajax/$', create_parent, name='registro_ajax'),
    url(r'^inscripcions-ajax/$', create_parents, name='registros_ajax'),
    url(r'^administracion/$', AdministracionView.as_view(), name='administracion'),

]