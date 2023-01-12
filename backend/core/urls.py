

from django.urls import include, path

from backend.core import views as v

app_name = 'core'

v1_urlpatterns = [
    path('lotes/', v.lote_list, name='lote_list'),
    path('lote/<int:pk>', v.lote_detail, name='lote_detail'),
    path('lote/create/', v.lote_create, name='lote_create'),
    path('lote/bulk-events/', v.bulk_events, name='bulk_events'),
    path('lote/bulk-batches/', v.bulk_STD_batches, name='bulk_STD_batches'),
    path('lote/bulk-weigths/', v.bulk_weigths, name='bulk_weigths'),
    # path('lote/create/', v.lote_create_dinamic, name='lote_create_dinamic'),
]

urlpatterns = [
    path('api/v1/', include(v1_urlpatterns)),
]
