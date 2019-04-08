from django.db import models

# Create your models here.
class Prospecto(models.Model):
    prospecto_nombre = models.CharField('Nombre', max_length=70)
    prospecto_apelldo_m = models.CharField('Apellido Materno', max_length=70)
    prospecto_apelldo_p = models.CharField('Apellido Paterno', max_length=70)
    prospecto_liceciatura = models.CharField('Licenciatura/Maestria', max_length=50)
    DIAS = (('LUENES', 'LUNES'), ('MARTES', 'MARTES'), ('MIERCOLES', 'MIERCOLES'), ('JUEVES', 'JUEVES'), ('VIERNES', 'VIERNES'), ('SABADO', 'SABADO'), ('DOMINGO', 'DOMINGO'))
    prospecto_dia_interes = models.CharField('Dia de interes', max_length=15, choices = DIAS)
    prospecto_nacionalidad = models.CharField('Nacionalidad', max_length=50)
    prospecto_naciminto = models.DateField('Fecha de nacimiento')
    estado_civil=(('Soltero','Soltero'),('Casado','Casado'),('Divorsiado','Divorsiado'), ('Union Libre','Union Libre'))
    prospecto_estado_civil = models.CharField('Estado Civil', max_length=15, choices=estado_civil)
    # DOMICILIO
    prospecto_calle = models.CharField('Calle', max_length=70)
    prospecto_numero = models.BigIntegerField('Numero')
    prospecto_colonia = models.CharField("Colonia", max_length=70)
    prospecto_ciudad = models.CharField("Ciudad/Estado", max_length=70)
    prospecto_cp = models.BigIntegerField('Codigo Postal')
    prospecto_tel_casa = models.BigIntegerField('Telefono Casa')
    prospecto_tel_celular = models.BigIntegerField('Telefono Celular')
    prospecto_correo_p = models.EmailField('Correo Personal', max_length=70)
    # DATOS FAMILIARES
    prospecto_nombre_familiar = models.CharField('Nombre Familiar', max_length=50)
    prospecto_parentesco_familiar = models.CharField('Parentesco', max_length=30)
    prospecto_telefono_familiar = models.BigIntegerField('Telefono Familiar')
    prospecto_familiar_redes_social = models.CharField('Redes sociales', max_length=100)
    # DATOS ACADEMICOS
    INGLES = (
        ('BAJO', 'BAJO'),
        ('MEDIO', 'MEDIO'),
        ('ALTO', 'ALTO')
        )
    prospecto_nivel_ingles = models.CharField('Nivel de ingles', choices=INGLES, max_length=50)
    prospecto_nivel_estudios = models.CharField('Nivel de Estudios', max_length=80)
    prospecto_institucion = models.CharField('Institucion', max_length=80)
    prospecto_nombre_programa = models.CharField('Nombre del Programa', max_length=50)
    prospecto_programa_inicio = models.DateField('Fecha inicio')
    prospecto_programa_termino = models.DateField('Fecha Terminno')
    prospecto_cedula = models.CharField('Numero cedula profesional', max_length=50)
    prospecto_cedula_carrera = models.CharField('Carrera ', max_length=50)
    prospecto_cedula_expedicion = models.DateField('Año de expedicion')
    # EXPERIENCIA LABORAL
    respuesta=(('SI', 'SI'), ('NO', 'NO'))
    prospecto_qstion_trabaja = models.CharField('Trabaja Actualmente', max_length=5, choices=respuesta, default='SI')
    prospecto_empresa_nombre = models.CharField('Empresa', max_length=50)
    prospecto_empresa_giro = models.CharField('Giro Empresa', max_length=50)
    prospecto_empresa_puesto_ocupado = models.CharField('Puesto Ocupado', max_length=50)
    prospecto_empresa_telefono = models.BigIntegerField()
    prospecto_emoresa_correo = models.EmailField('Coerreo Empresa', max_length=254)

    prospecto_interes = models.CharField('En breves palabras exponga su interés por cursar este programa:', max_length=2000)
    prospecto_como_se_entero = models.CharField('¿Cómo se enteró del programa?', max_length=100)
    prospecto_fecha_creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.prospecto_nombre


