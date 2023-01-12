from django import forms

from backend.core.models import Lote


class LoteForm(forms.ModelForm):

    class Meta:
        model = Lote
        fields = ('id',
            'production_date',
            'terminal',
            'sequencial',
            'batch',
            'type',
            'liquid',
            'tara',
            'unit_of_measurement',
            'client',
            'product_number',
            'product_name',
            'sub_total',
            'total',
            'message',)