from django.conf.urls import url

from .views import index, inicio, ParticipanteList, ParticipanteCreate, ParticipanteUpdate, ParticipanteDelete

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^portal/$', inicio, name='inicio'),
    url(r'^portal/participante/$', ParticipanteList.as_view(), name='participante'),
    url(r'^portal/participante/registro/$', ParticipanteCreate.as_view(), name='participante_create'),
    url(r'^portal/participante/editar/(?P<pk>\d+)/$', ParticipanteUpdate.as_view(), name='participante_update'),
    url(r'^portal/participante/eliminar/(?P<pk>\d+)/$', ParticipanteDelete.as_view(), name='participante_delete'),
    #url(r'^portal/pago/$', PagoList.as_view(), name='pago'),
    #url(r'^portal/pago/registro/$', PagoCreate.as_view(), name='pago_create'),
    #url(r'^portal/pago/editar/(?P<pk>\d+)/$', PagoUpdate.as_view(), name='pago_update'),
    #url(r'^portal/pago/eliminar/(?P<pk>\d+)/$', PagoDelete.as_view(), name='pago_delete'),
]