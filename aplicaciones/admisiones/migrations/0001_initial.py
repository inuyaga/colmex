# Generated by Django 2.1.7 on 2019-02-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prospecto_nombre', models.CharField(max_length=70, verbose_name='Nombre')),
                ('prospecto_apelldo_m', models.CharField(max_length=70, verbose_name='Apellido Materno')),
                ('prospecto_apelldo_p', models.CharField(max_length=70, verbose_name='Apellido Paterno')),
                ('prospecto_liceciatura', models.CharField(max_length=50, verbose_name='Licenciatura/Maestria')),
                ('prospecto_dia_interes', models.CharField(choices=[('LUENES', 'LUNES'), ('MARTES', 'MARTES'), ('MIERCOLES', 'MIERCOLES'), ('JUEVES', 'JUEVES'), ('VIERNES', 'VIERNES'), ('SABADO', 'SABADO'), ('DOMINGO', 'DOMINGO')], max_length=15, verbose_name='Dia de interes')),
                ('prospecto_nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('prospecto_naciminto', models.DateField(verbose_name='Fecha de nacimiento')),
                ('prospecto_estado_civil', models.CharField(max_length=15, verbose_name='Estado Civil')),
                ('prospecto_calle', models.CharField(max_length=70, verbose_name='Calle')),
                ('prospecto_numero', models.IntegerField(verbose_name='Numero')),
                ('prospecto_colonia', models.CharField(max_length=70, verbose_name='Colonia')),
                ('prospecto_ciudad', models.CharField(max_length=70, verbose_name='Ciudad/Estado')),
                ('prospecto_cp', models.IntegerField(verbose_name='Codigo Postal')),
                ('prospecto_tel_casa', models.IntegerField(verbose_name='Telefono Casa')),
                ('prospecto_tel_celular', models.IntegerField(verbose_name='Telefono Celular')),
                ('prospecto_correo_p', models.EmailField(max_length=70, verbose_name='Correo Personal')),
                ('prospecto_nombre_familiar', models.CharField(max_length=50, verbose_name='Nombre Familiar')),
                ('prospecto_parentesco_familiar', models.CharField(max_length=30, verbose_name='Parentesco')),
                ('prospecto_telefono_familiar', models.IntegerField(verbose_name='Telefono Familiar')),
                ('prospecto_familiar_redes_social', models.CharField(max_length=100, verbose_name='Redes sociales')),
                ('prospecto_nivel_ingles', models.CharField(choices=[('BAJO', 'BAJO'), ('MEDIO', 'MEDIO'), ('ALTO', 'ALTO')], max_length=50, verbose_name='Nivel de ingles')),
                ('prospecto_nivel_estudios', models.CharField(max_length=80, verbose_name='Nivel de Estudios')),
                ('prospecto_institucion', models.CharField(max_length=80, verbose_name='Institucion')),
                ('prospecto_nombre_programa', models.CharField(max_length=50, verbose_name='Nombre del Programa')),
                ('prospecto_programa_inicio', models.DateField(verbose_name='Fecha inicio')),
                ('prospecto_programa_termino', models.DateField(verbose_name='Fecha Terminno')),
                ('prospecto_cedula', models.CharField(max_length=50, verbose_name='Numero cedula profesional')),
                ('prospecto_cedula_carrera', models.CharField(max_length=50, verbose_name='Numero Carrera ')),
                ('prospecto_cedula_expedicion', models.DateField(verbose_name='Año de expedicion')),
                ('prospecto_empresa_nombre', models.CharField(max_length=50, verbose_name='Empresa')),
                ('prospecto_empresa_giro', models.CharField(max_length=50, verbose_name='Giro Empresa')),
                ('prospecto_empresa_puesto_ocupado', models.CharField(max_length=50, verbose_name='Puesto Ocupado')),
                ('prospecto_empresa_telefono', models.IntegerField()),
                ('prospecto_emoresa_correo', models.EmailField(max_length=254, verbose_name='Coerreo Empresa')),
                ('prospecto_interes', models.CharField(max_length=250, verbose_name='En breves palabras exponga su interés por cursar este programa:')),
                ('prospecto_como_se_entero', models.CharField(max_length=100, verbose_name='¿Cómo se enteró del programa?')),
                ('prospecto_fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
