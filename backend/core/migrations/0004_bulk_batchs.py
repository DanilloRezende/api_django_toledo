# Generated by Django 4.1.4 on 2023-01-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk_Batchs',
            fields=[
                ('batchID', models.IntegerField(primary_key=True, serialize=False, verbose_name='LoteID')),
                ('terminal', models.CharField(blank=True, max_length=30, null=True, verbose_name='Terminal')),
                ('batchStatus', models.IntegerField(blank=True, default=0, null=True, verbose_name='Status do Lote')),
                ('userField1', models.IntegerField(blank=True, default=0, null=True, verbose_name='userField1')),
                ('userField2', models.IntegerField(blank=True, default=0, null=True, verbose_name='userField2')),
                ('userField3', models.CharField(blank=True, max_length=30, null=True, verbose_name='userField3')),
                ('userField4', models.IntegerField(blank=True, default=0, null=True, verbose_name='userField4')),
                ('userField5', models.IntegerField(blank=True, default=0, null=True, verbose_name='userField5')),
                ('userField6', models.CharField(blank=True, max_length=30, null=True, verbose_name='userField6')),
                ('prodNumberList', models.CharField(blank=True, max_length=30, null=True, verbose_name='Número de Produção')),
                ('subtotNumberList', models.CharField(blank=True, max_length=30, null=True, verbose_name='SubTotal')),
                ('targetValueList', models.IntegerField(blank=True, default=0, null=True, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Bulk padrão de Lote',
                'verbose_name_plural': 'Bulk padrão de Lotes',
                'ordering': ('batchID',),
            },
        ),
    ]
