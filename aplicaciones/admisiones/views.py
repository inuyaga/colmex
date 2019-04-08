from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, View, ListView, UpdateView, DeleteView
from aplicaciones.admisiones.models import Prospecto
from aplicaciones.admisiones.forms import ProspectoForm, ProspectoFormEdit
from aplicaciones.admisiones import views

import io
from django.http import HttpResponse, HttpResponseRedirect
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors



# Create your views here.
class RegiatroAdmision(CreateView):
    model = Prospecto
    form_class = ProspectoForm
    template_name = "admisiones/inicio.html"
    # success_url = reverse_lazy('index:home')
    def form_valid(self, form):
        prospect=form.save(commit=False)
        prospect.save()
        primarykey=prospect.pk
        return HttpResponseRedirect(reverse_lazy('admisiones:registro_pdf', kwargs={'pk':primarykey}))

class PreregistroList(ListView):
    model = Prospecto
    template_name = 'admisiones/listar_admisiones.html'

class PreregistroEdit(UpdateView):
    model = Prospecto
    form_class = ProspectoFormEdit
    template_name = "admisiones/inicio.html"
    success_url = reverse_lazy('admisiones:registro_list')

class preregristroDelete(DeleteView):
    model = Prospecto
    template_name = "admisiones/eliminar.html"
    success_url = reverse_lazy('admisiones:registro_list')





class Crear_pdf_prospecto(TemplateView):

    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo_django.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)

    def get(self, request, *args, **kwargs):
            from reportlab.lib.colors import Color, gray
            import textwrap

            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = io.BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer, pagesize=letter)
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            # self.cabecera(pdf)
            #Con show page hacemos un corte de página para pasar a la siguiente

            pdf.setFont("Helvetica", 16)
            pdf.rect(500, 705, 70, 80, stroke=1, fill=0)
            pdf.drawString(150, 710, "SOLICITUD DE ADMISIÓN LICENCIATURA")
            pdf.line(50,700,550,700)
            pdf.setFont("Helvetica", 12)
            pdf.drawString(220, 690, "Datos generales del solicitante")

            persona = Prospecto.objects.get(id=self.kwargs.get('pk'))

            pdf.setFont("Helvetica", 10)
            pdf.drawString(60, 670, "Maestría a la que se inscribe:")
            pdf.rect(60, 650, 250, 18, stroke=1, fill=0)
            pdf.drawString(70, 655, persona.prospecto_liceciatura)


            pdf.drawString(320, 670, "¿Qué dÍa te interesa asistir a CUCM?")
            pdf.rect(320, 650, 250, 18, stroke=1, fill=0)
            pdf.drawString(325, 655, persona.prospecto_dia_interes)


            pdf.drawString(60, 630, "Apellido paterno:")
            pdf.rect(60, 610, 170, 18, stroke=1, fill=0)
            pdf.drawString(65, 615, persona.prospecto_apelldo_p)

            pdf.drawString(235, 630, "Apellido materno:")
            pdf.rect(230, 610, 170, 18, stroke=1, fill=0)
            pdf.drawString(235, 615, persona.prospecto_apelldo_m)

            pdf.drawString(400, 630, "Nombre:")
            pdf.rect(400, 610, 170, 18, stroke=1, fill=0)
            pdf.drawString(405, 615, persona.prospecto_nombre)



            pdf.drawString(60, 590, "Nacionalidad:")
            pdf.rect(60, 570, 170, 18, stroke=1, fill=0)
            pdf.drawString(65, 575, persona.prospecto_nacionalidad)

            pdf.drawString(235, 590, "Fecha de nacimiento:")
            pdf.rect(230, 570, 170, 18, stroke=1, fill=0)
            pdf.drawString(235, 575, str(persona.prospecto_naciminto))

            pdf.drawString(400, 590, "Estado civil:")
            pdf.rect(400, 570, 170, 18, stroke=1, fill=0)
            pdf.drawString(405, 575, persona.get_prospecto_estado_civil_display())

            pdf.setFont("Helvetica", 14)
            pdf.drawString(60, 550, "Domicilio de residencia")

            red50transparent = Color( 100, 0, 0, alpha=0.5)

            pdf.setFont("Helvetica", 10)
            # pdf.setFillColor(gray)
            pdf.rect(60, 530, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 535, "Calle: "+persona.prospecto_calle+" Numero : "+str(persona.prospecto_numero)+" Colonia: "+persona.prospecto_colonia)

            pdf.rect(60, 510, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 515, "Ciudad Estado: "+persona.prospecto_ciudad+" Código Postal: "+str(persona.prospecto_cp)+" Teléfono casa: "+str(persona.prospecto_tel_casa))

            pdf.rect(60, 490, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 495, "e-mail: "+persona.prospecto_correo_p+" Celular: "+str(persona.prospecto_tel_celular))

            pdf.setFont("Helvetica", 14)
            pdf.drawString(60, 450, "Datos familiares")
            pdf.setFont("Helvetica", 11)
            pdf.drawString(60, 440, "En caso de emergencia:")
            pdf.setFont("Helvetica", 10)
            pdf.rect(60, 420, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 425, "Parentesco: "+persona.prospecto_parentesco_familiar+" Nombre: "+persona.prospecto_nombre_familiar)

            pdf.rect(60, 400, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 405, "Teléfono casa: "+str(persona.prospecto_telefono_familiar)+" Redes Sociales: "+persona.prospecto_familiar_redes_social)

            pdf.setFont("Helvetica", 14)
            pdf.drawString(60, 370, "Datos académicos")
            pdf.setFont("Helvetica", 10)
            pdf.drawString(62, 360, "Nivel de inglés: "+persona.get_prospecto_nivel_ingles_display())


            pdf.rect(60, 340, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 345, persona.prospecto_nivel_estudios+" Institución: "+persona.prospecto_institucion)


            pdf.rect(60, 320, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 325, "Nombre del programa: "+persona.prospecto_nombre_programa+" Inicio: "+str(persona.prospecto_programa_inicio)+" Termino: "+str(persona.prospecto_programa_termino))

            pdf.rect(60, 300, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 305, "Cedula: "+str(persona.prospecto_cedula)+" Carrera: "+persona.prospecto_cedula_carrera+" Expedición: "+str(persona.prospecto_cedula_expedicion))

            pdf.setFont("Helvetica", 14)
            pdf.drawString(60, 280, "Experiencia Laboral")
            pdf.setFont("Helvetica", 10)

            pdf.drawString(60, 270, "Trabaja actualmente:")
            pdf.drawString(155, 270, persona.get_prospecto_qstion_trabaja_display())

            pdf.rect(60, 250, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 255, "Nombre: "+persona.prospecto_empresa_nombre+" Giro de la empresa: "+persona.prospecto_empresa_giro)

            pdf.rect(60, 230, 510, 18, fill=False, stroke=True)
            pdf.drawString(62, 235, "Puesto: "+persona.prospecto_empresa_puesto_ocupado+" Teléfono: "+str(persona.prospecto_empresa_telefono)+" e-mail: "+persona.prospecto_emoresa_correo)


            pdf.setFont("Helvetica", 12)
            pdf.drawString(60, 210, "En breves palabras exponga su interés por cursar este programa:")
            pdf.setFont("Helvetica", 10)

            styles = getSampleStyleSheet()
            stylesBH = styles['Normal']
            stylesBH.alignment = TA_CENTER
            stylesBH.fontSize = 11
            #pdf.drawString(60, 200, Paragraph(persona.prospecto_interes, stylesBH))

            textobject = pdf.beginText(cm, 2.5*cm)
            textobject.setTextOrigin(60, 190)
            # Set font face and size
            textobject.setFont('Times-Roman', 12)

            inicio = 0
            fin = 0
            contador = 0
            comentario = persona.prospecto_interes
            partes = []
            for i in range(len(persona.prospecto_interes)):
                if contador == 105:
                    inicio = i-105
                    fin = i
                    partes.append(comentario[inicio:fin])
                    contador = 0
                elif i == len(persona.prospecto_interes)-1:
                    partes.append(comentario[fin:len(persona.prospecto_interes)])
                contador += 1



            for parte in partes:
                textobject.textLine(parte)
            pdf.drawText(textobject)

            pdf.drawString(60, 120, "¿Cómo se enteró del programa?")
            pdf.drawString(220, 120, "R: "+persona.prospecto_como_se_entero)



            pdf.drawString(250, 90, "Firma del solicitante")


            textobject = pdf.beginText(cm, 2.5*cm)
            textobject.setTextOrigin(200, 65)
            # Set font face and size
            textobject.setFont('Times-Roman', 12)
            textobject.textLine(persona.prospecto_nombre+" "+persona.prospecto_apelldo_p+" "+persona.prospecto_apelldo_m)
            pdf.drawText(textobject)
            pdf.line(50,60,570,60)
            pdf.drawString(230, 50, "Nombre completo y firma.")





            # pdf.drawText(persona.prospecto_interes)


            # pdf.rect(160, 530, 100, 18, fill=True, stroke=True)
            # pdf.rect(260, 530, 100, 18, fill=True, stroke=True)
            # pdf.rect(360, 530, 100, 18, fill=True, stroke=True)
            # pdf.rect(460, 530, 100, 18, fill=True, stroke=True)
            # pdf.drawString(60, 550, "Calle")
            # pdf.drawString(60, 550, "Número")
            # pdf.drawString(60, 550, "Colonia")
            # pdf.drawString(60, 550, "Ciudad Estado")
            # pdf.drawString(60, 550, "Código Postal")

            # pdf.rect(260, 530, 100, 18, fill=True, stroke=False)
            # pdf.rect(360, 530, 100, 18, fill=True, stroke=False)
            # pdf.rect(460, 530, 100, 18, fill=True, stroke=False)





            # self.tabla(pdf, 690, persona)
            # HEADER DE LA TABLA
            # styles = getSampleStyleSheet()
            # stylesBH = styles['Normal']
            # stylesBH.alignment = TA_CENTER
            # stylesBH.fontSize = 11

            # maestria=Paragraph('''Maestria''', stylesBH)
            # dia=Paragraph('''Dia''', stylesBH)

            # data = (maestria, dia)




            # width, height = letter
            # tabla = Table([data], colWidths=[11 * cm, 6 * cm])
            # tabla.setStyle(TableStyle(
            # [
            #         #Los bordes de todas las celdas serán de color negro y con un grosor de 1
            #         ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            #         #El tamaño de las letras de cada una de las celdas será de 10
            #         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            # ]
            # ))
            # tabla.wrapOn(pdf, width, height)
            # #Definimos la coordenada donde se dibujará la tabla
            # tabla.drawOn(pdf, 60,680)



            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response


    def tabla(self,pdf,y, persona):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = (persona.prospecto_liceciatura, persona.prospecto_dia_interes)
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(persona.prospecto_nombre, persona.prospecto_apelldo_m, persona.prospecto_apelldo_p, persona.prospecto_liceciatura) for persona in Prospecto.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados], colWidths=[11 * cm, 6 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(1,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)




