# Generated by Django 2.1.7 on 2019-02-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0002_auto_20190226_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_cp',
            field=models.BigIntegerField(verbose_name='Codigo Postal'),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_empresa_telefono',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_numero',
            field=models.BigIntegerField(verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_qstion_trabaja',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=5, verbose_name='Trabaja Actualmente'),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_tel_casa',
            field=models.BigIntegerField(verbose_name='Telefono Casa'),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_tel_celular',
            field=models.BigIntegerField(verbose_name='Telefono Celular'),
        ),
        migrations.AlterField(
            model_name='prospecto',
            name='prospecto_telefono_familiar',
            field=models.BigIntegerField(verbose_name='Telefono Familiar'),
        ),
    ]
