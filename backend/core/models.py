from django.db import models


class Lote(models.Model):
    id = models.IntegerField('id', primary_key=True)
    production_date = models.DateTimeField('Data de produção', null=True, blank=True, default=None)
    terminal = models.IntegerField('Terminal',  null=True, blank=True, default=None)
    sequencial = models.IntegerField('Sequencial',  null=True, blank=True, default=None)
    batch = models.IntegerField('Lote',  null=True, blank=True, default=None)
    type = models.CharField('Tipo', max_length=30, null=True, blank=True, default=None)
    liquid = models.FloatField('Líquido',  null=True, blank=True, default=None)
    tara = models.FloatField('tara',  null=True, blank=True, default=None)
    unit_of_measurement = models.CharField('Unidade de Medida', max_length=30, null=True, blank=True, default=None)
    client = models.CharField('Cliente', max_length=30, null=True, blank=True, default=None)
    product_number = models.IntegerField('Número do Produto',  null=True, blank=True, default=None)
    product_name = models.CharField('Nome do Produto', max_length=30, null=True, blank=True, default=None)
    sub_total = models.FloatField('SubTotal',  null=True, blank=True, default=None)
    total = models.FloatField('Total', null=True, blank=True, default=None)
    message = models.CharField('Mensagem', max_length=30, null=True, blank=True, default=None)



    class Meta:
        ordering = ('id',)
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return f'Lote {self.id}'

    def to_dict(self):
        return{
            'id': self.id,
            'production_date': self.production_date,
            'terminal': self.terminal,
            'sequencial': self.sequencial,
            'batch': self.batch,
            'type': self.type,
            'liquid': self.liquid,
            'tara': self.tara,
            'unit_of_measurement': self.unit_of_measurement,
            'client': self.client,
            'product_number': self.product_number,
            'product_name': self.product_name,
            'sub_total': self.sub_total,
            'total': self.total,
            'message': self.message,
        }


class events(models.Model):
    eventID = models.IntegerField('eventID', primary_key=True)
    terminal = models.IntegerField('Terminal', null=True, blank=True, default=None)
    dateTime = models.DateTimeField ('Data do Evento', null=True, blank=True, default=None)
    evtType = models.IntegerField('evtType', null=True, blank=True, default=None)
    evtCode = models.IntegerField('evtCode', null=True, blank=True, default=None)
    evtMessage = models.CharField('evtMessage',max_length=300, null=True, blank=True, default=None)
 

    class Meta:
        ordering = ('eventID',)
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'events {self.eventID}'

    def to_dict(self):
        return{
            'eventID', self.eventID,
            'Terminal', self.terminal,
            'Data do Evento', self.dateTime,
            'evtType', self.evtType,
            'evtCode', self.evtCode,
            'evtMessage', self.evtMessage,
                    }


class Bulk_Batchs(models.Model):
    batchID = models.IntegerField('LoteID', primary_key=True)
    terminal = models.IntegerField('Terminal', default=None, null=True, blank=True)
    batchStatus = models.IntegerField('Status do Lote', default=None, null=True, blank=True)
    userField1 = models.IntegerField('userField1', default=None, null=True, blank=True)
    userField2 = models.IntegerField('userField2', default=None, null=True, blank=True)
    userField3 = models.IntegerField('userField3', default=None, null=True, blank=True)
    userField4 = models.IntegerField('userField4', default=None, null=True, blank=True)
    userField5 = models.IntegerField('userField5', default=None, null=True, blank=True)
    userField6 = models.IntegerField('userField6', default=None, null=True, blank=True)
    prodNumberList = models.CharField('Número de Produção', max_length=30, null=True, blank=True)
    subtotNumberList = models.CharField('SubTotal', max_length=30, null=True, blank=True)
    targetValueList = models.CharField('Valor', max_length=300, default=0, null=True, blank=True)
  


    class Meta:
        ordering = ('batchID',)
        verbose_name = 'Bulk padrão de Lote'
        verbose_name_plural = 'Bulk padrão de Lotes'

    def __str__(self):
        return f'LoteID {self.batchID}'

    def to_dict(self):
        return{
            'Terminal', self.terminal,
            'Status do Lote', self.batchStatus,
            'LoteID', self.batchID,
            'userField1', self.userField1,
            'userField2', self.userField2,
            'userField3', self.userField3,
            'userField4', self.userField4,
            'userField5', self.userField5,
            'userField6', self.userField6,
            'Número de Produção', self.prodNumberList,
            'SubTotal', self.subtotNumberList,
            'Valor', self.targetValueList,
                        
                    }


class Bulk_Weigths(models.Model):
    weightID = models.IntegerField('weightID', primary_key=True)
    dateTime = models.CharField('Data', max_length=30, null=True, blank=True, default=None)
    opType = models.CharField('Tipo de OP', max_length=30,  null=True, blank=True, default=None)
    terminal = models.IntegerField('Terminal',  null=True, blank=True, default=None)
    net = models.FloatField('Net',  null=True, blank=True, default=None)
    tare = models.FloatField('Tara', max_length=30, null=True, blank=True, default=None)
    wtUnit = models.CharField('Unidade', max_length=30,  null=True, blank=True, default=None)
    stepNumber = models.IntegerField('stepNumber',default=None, null=True, blank=True)
    subtotNumber = models.IntegerField('subtotNumber', default=None, null=True, blank=True)
    prodNumber = models.IntegerField('Número de Produção', null=True, blank=True, default=None)
    stepTotal = models.FloatField('stepTotal', max_length=30, null=True, blank=True, default=None)
    subtotTotal = models.CharField('SubTotal', max_length=30, null=True, blank=True, default=None)
    prodTotal = models.FloatField('Produção Total', null=True, blank=True, default=None)
    grandTotal = models.FloatField('grandTotal', null=True, blank=True, default=None)
    flow = models.FloatField('Fluxo', null=True, blank=True, default=None)
    flowUnit = models.CharField('flowUnit', max_length=30, null=True, blank=True, default=None)
    batchID = models.IntegerField('LoteID', null=True, blank=True, default=None)
  


    class Meta:
        ordering = ('weightID',)
        verbose_name = 'Peso dos Lotes'
        verbose_name_plural = 'Bulk peso de Lotes'

    def __str__(self):
        return f'weightID {self.weightID}'

    def to_dict(self):
        return{
            'weightID', self.weightID,
            'Data', self.dateTime,
            'Tipo de OP', self.opType,
            'Terminal', self.terminal,
            'Net', self.net,
            'Tara', self.tare,
            'Unidade', self.wtUnit,
            'stepNumber', self.stepNumber,
            'subtotNumber', self.subtotNumber,
            'Número de Produção', self.prodNumber,
            'stepTotal', self.stepTotal,
            'SubTotal', self.subtotTotal,
            'Produção Total', self.prodTotal,
            'grandTotal', self.grandTotal,
            'Fluxo', self.flow,
            'flowUnit', self.flowUnit,
            'LoteID', self.batchID,
                        
                    }