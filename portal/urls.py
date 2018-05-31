from django.conf.urls import url

from .views import IndexView, AdministracionView, InscripcionUpdateView, create_parent, create_parents,\
                   ParticipanteUpdateView, generarlista_pdf, generar_certificado, generar_credencial,\
                   entrega_material, asistencia_ina, asistencia_pt, asistencia_cg, entrega_ag                   

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^inscripcion-ajax/$', create_parent, name='registro_ajax'),
    url(r'^inscripcions-ajax/$', create_parents, name='registros_ajax'),
    url(r'^administracion/$', AdministracionView.as_view(), name='administracion'),
    url(r'^administracion/inscripcion/(?P<pk>\d+)/$', InscripcionUpdateView.as_view(), name='inscripcion_update'),
    url(r'^administracion/participante/(?P<pk>\d+)/$', ParticipanteUpdateView.as_view(), name='participante_update'),
    url(r'^administracion/inscripcion/lista_pdf/$', generarlista_pdf, name='inscripcion_reporte'),
    url(r'^administracion/participante/certificado/(?P<pk>\d+)/$', generar_certificado, name='certificado_reporte'),
    url(r'^administracion/participante/credencial/(?P<pk>\d+)/$', generar_credencial, name='credencial_reporte'),
    url(r'^administracion/participante/material/(?P<pk>\d+)/$', entrega_material, name='entrega_material'),
    url(r'^administracion/participante/ag/(?P<pk>\d+)/$', entrega_ag, name='entrega_agenda'),
    url(r'^administracion/participante/ina/(?P<pk>\d+)/$', asistencia_ina, name='asistencia_ina'),
    url(r'^administracion/participante/pt/(?P<pk>\d+)/$', asistencia_pt, name='asistencia_pt'),
    url(r'^administracion/participante/cg/(?P<pk>\d+)/$', asistencia_cg, name='asistencia_cg'),
]