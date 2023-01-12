from django.db import models


class Lote(models.Model):
    id = models.IntegerField('Id', primary_key=True)
    production_date = models.CharField('Data de produção', max_length=30, null=True, blank=True)
    terminal = models.IntegerField('Terminal', default=0, null=True, blank=True)
    sequencial = models.IntegerField('Sequencial', default=0, null=True, blank=True)
    batch = models.IntegerField('Lote', default=0, null=True, blank=True)
    type = models.CharField('Tipo', max_length=30, null=True, blank=True)
    liquid = models.IntegerField('Líquido', default=0, null=True, blank=True)
    tara = models.IntegerField('tara', default=0, null=True, blank=True)
    unit_of_measurement = models.CharField('Unidade de Medida', max_length=30, null=True, blank=True)
    client = models.CharField('Cliente', max_length=30, null=True, blank=True)
    product_number = models.IntegerField('Número do Produto', default=0, null=True, blank=True)
    product_name = models.CharField('Nome do Produto', max_length=30, null=True, blank=True)
    sub_total = models.IntegerField('SubTotal', default=0, null=True, blank=True)
    total = models.IntegerField('Total', default=0, null=True, blank=True)
    message = models.CharField('Mensagem', max_length=30, null=True, blank=True)



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
    terminal = models.IntegerField('Terminal', default=0, null=True, blank=True)
    dateTime = models.CharField('Data do Evento', max_length=30, null=True, blank=True)
    evtType = models.IntegerField('evtType', default=0, null=True, blank=True)
    evtCode = models.IntegerField('evtCode', null=True, blank=True)
    evtMessage = models.CharField('evtMessage',max_length=30, default=0, null=True, blank=True)
 

    class Meta:
        ordering = ('eventID',)
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'events {self.id}'

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
    terminal = models.CharField('Terminal', max_length=30, null=True, blank=True)
    batchStatus = models.IntegerField('Status do Lote', default=0, null=True, blank=True)
    userField1 = models.IntegerField('userField1', default=0, null=True, blank=True)
    userField2 = models.IntegerField('userField2', default=0, null=True, blank=True)
    userField3 = models.CharField('userField3', max_length=30, null=True, blank=True)
    userField4 = models.IntegerField('userField4', default=0, null=True, blank=True)
    userField5 = models.IntegerField('userField5', default=0, null=True, blank=True)
    userField6 = models.CharField('userField6', max_length=30, null=True, blank=True)
    prodNumberList = models.CharField('Número de Produção', max_length=30, null=True, blank=True)
    subtotNumberList = models.CharField('SubTotal', max_length=30, null=True, blank=True)
    targetValueList = models.IntegerField('Valor', default=0, null=True, blank=True)
  


    class Meta:
        ordering = ('batchID',)
        verbose_name = 'Bulk padrão de Lote'
        verbose_name_plural = 'Bulk padrão de Lotes'

    def __str__(self):
        return f'LoteID {self.id}'

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
    dateTime = models.CharField('Data', max_length=30, null=True, blank=True)
    opType = models.CharField('Tipo de OP', max_length=30, default=0, null=True, blank=True)
    terminal = models.IntegerField('Terminal', default=0, null=True, blank=True)
    net = models.FloatField('Net', default=0, null=True, blank=True)
    tare = models.FloatField('Tara', max_length=30, null=True, blank=True)
    wtUnit = models.CharField('Unidade', max_length=30, default=0, null=True, blank=True)
    stepNumber = models.IntegerField('stepNumber', default=0, null=True, blank=True)
    subtotNumber = models.IntegerField('subtotNumber', null=True, blank=True)
    prodNumber = models.IntegerField('Número de Produção', null=True, blank=True)
    stepTotal = models.FloatField('stepTotal', max_length=30, null=True, blank=True)
    subtotTotal = models.CharField('SubTotal', max_length=30, default=0, null=True, blank=True)
    prodTotal = models.FloatField('Produção Total', default=0, null=True, blank=True)
    grandTotal = models.FloatField('grandTotal', default=0, null=True, blank=True)
    flow = models.FloatField('Fluxo', default=0, null=True, blank=True)
    flowUnit = models.CharField('flowUnit', max_length=30, default=0, null=True, blank=True)
    batchID = models.IntegerField('LoteID', default=0, null=True, blank=True)
  


    class Meta:
        ordering = ('weightID',)
        verbose_name = 'Peso dos Lotes'
        verbose_name_plural = 'Bulk peso de Lotes'

    def __str__(self):
        return f'weightID {self.id}'

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