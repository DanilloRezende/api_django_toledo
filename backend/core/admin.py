from django.contrib import admin

from backend.core.models import Bulk_Batchs, Bulk_Weigths, Lote, events


class LoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_date', 'terminal', 'sequencial', 'batch', 'total')


admin.site.register(Lote, LoteAdmin)


class BulkEvent(admin.ModelAdmin):
    list_display = ('eventID', 'terminal', 'dateTime', 'evtType', 'evtCode', 'evtMessage')

admin.site.register(events, BulkEvent)


class BulkBatchs(admin.ModelAdmin):
    list_display = ('batchID', 'terminal', 'batchStatus', 'userField1', 'userField2', 'userField3', 'userField4', 'userField5', 'userField6', 'prodNumberList', 'subtotNumberList', 'targetValueList')

admin.site.register(Bulk_Batchs, BulkBatchs)

class BulkWeigth(admin.ModelAdmin):
    list_display = ("weightID", "dateTime", "opType", "terminal", "net", "tare", "wtUnit", "stepNumber", "subtotNumber", "prodNumber", "stepTotal", "subtotTotal", "prodTotal", "grandTotal", "flow", "flowUnit", "batchID")

admin.site.register(Bulk_Weigths, BulkWeigth)