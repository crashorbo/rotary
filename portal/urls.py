from django.conf.urls import url

from .views import index, inicio, ParticipanteList, ParticipanteCreate

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^portal/$', inicio, name='inicio'),
    url(r'^portal/participante/$', ParticipanteList.as_view(), name='participante'),
    url(r'^portal/participante/registro/$', ParticipanteCreate.as_view(), name='participante_create')
]