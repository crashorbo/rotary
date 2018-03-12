from django.conf.urls import url

from .views import index, inicio, ParticipanteList, ParticipanteCreate, ParticipanteUpdate, ParticipanteDelete, PagoList

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^portal/$', inicio, name='inicio'),
    url(r'^portal/participante/$', ParticipanteList.as_view(), name='participante'),
    url(r'^portal/participante/registro/$', ParticipanteCreate.as_view(), name='participante_create'),
    url(r'^portal/participante/editar/(?P<pk>\d+)/$', ParticipanteUpdate.as_view(), name='participante_update'),
    url(r'^portal/participante/eliminar/(?P<pk>\d+)/$', ParticipanteDelete.as_view(), name='participante_delete'),
    url(r'^portal/pago/$', PagoList.as_view(), name='pago'),
]