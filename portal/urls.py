from django.conf.urls import url

from .views import IndexView, AdministracionView, InscripcionUpdateView, create_parent, create_parents, ParticipanteUpdateView, generarlista_pdf

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^inscripcion-ajax/$', create_parent, name='registro_ajax'),
    url(r'^inscripcions-ajax/$', create_parents, name='registros_ajax'),
    url(r'^administracion/$', AdministracionView.as_view(), name='administracion'),
    url(r'^administracion/inscripcion/(?P<pk>\d+)/$', InscripcionUpdateView.as_view(), name='inscripcion_update'),
    url(r'^administracion/participante/(?P<pk>\d+)/$', ParticipanteUpdateView.as_view(), name='participante_update'),
    url(r'^administracion/inscripcion/lista_pdf/$', generarlista_pdf, name='inscripcion_reporte'),
]