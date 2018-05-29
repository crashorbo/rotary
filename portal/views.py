from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.core.mail import send_mail
from io import BytesIO
import time

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF


from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, FormView, ListView, UpdateView
from .forms import InscripcionForm, ParticipanteFormset, ParticipantesFormset, InscripcionUpdateForm, ParticipanteForm
from .models import Inscripcion, Participante

TIPO_SELECT = {
    1: 'SOCIO',
    2: 'DAMA ROTARIA',
    3: 'ROTARACT',
    4: 'SOCIO CONYUGUE',
}

class IndexView(TemplateView):
    template_name = 'index.html'

class AdministracionView(ListView):
    model = Inscripcion
    template_name = 'administracion/lista.html'
    ordering = ['estado']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdministracionView, self).dispatch(request, *args, **kwargs)

def generar_certificado(request, pk):
    p = Participante.objects.get(pk=pk)
    p.certificado = True
    p.save()
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "certificado.pdf"  # llamado clientes
    response['Content-Disposition'] = 'inline; filename=%s' % pdf_name
    buff = BytesIO()
    c = canvas.Canvas(buff, pagesize=landscape(letter))
    
    c.setFont('Helvetica-BoldOblique', 30)
    c.drawCentredString(400,300,p.nombres + ' ' + p.apellidos)
    c.showPage()
    c.save()

    response.write(buff.getvalue())
    buff.close()
    return response

def generar_credencial(request, pk):
    p = Participante.objects.get(pk=pk)
    p.credencial = True
    p.save()

    response = HttpResponse(content_type='application/pdf')
    pdf_name = "crendecial.pdf"  # llamado clientes
    response['Content-Disposition'] = 'inline; filename=%s' % pdf_name
    buff = BytesIO()
    c = canvas.Canvas(buff, pagesize=letter)
    
    c.setFont('Helvetica-BoldOblique', 16)
    c.drawCentredString(110,720,(p.nombres).upper())
    c.setFont('Helvetica', 10)
    c.drawCentredString(110,695,(p.nombres + ' ' + p.apellidos).upper())
    c.drawCentredString(110,670,(p.club).upper())
    c.drawCentredString(110,645,(p.ciudad).upper())
    qrw = QrCodeWidget('CONFERENCIA ROTARY 4690|2018|'+(p.nombres + ' ' + p.apellidos).upper())
    b = qrw.getBounds()

    w=b[2]-b[0] 
    h=b[3]-b[1] 

    d = Drawing(40,40,transform=[40./w,0,0,40./h,0,0]) 
    d.add(qrw)

    renderPDF.draw(d, c, 160, 630)

    c.showPage()
    c.save()

    response.write(buff.getvalue())
    buff.close()
    return response

def entrega_material(request, pk):
    p = Participante.objects.get(pk=pk)
    p.material = True
    p.save()
    return JsonResponse({'success':'entrega completa'}, status=200)

def asistencia_ina(request, pk):
    p = Participante.objects.get(pk=pk)
    p.ina = True
    p.save()
    return JsonResponse({'success':'registro de asistencia exitoso'}, status=200)

def asistencia_pt(request, pk):
    p = Participante.objects.get(pk=pk)
    p.pt = True
    p.save()
    return JsonResponse({'success':'registro de asistencia exitoso'}, status=200)

def asistencia_cg(request, pk):
    p = Participante.objects.get(pk=pk)
    p.cg = True
    p.save()
    return JsonResponse({'success':'registro de asistencia exitoso'}, status=200)

def generarlista_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "inscripcion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    response['Content-Disposition'] = 'inline; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=landscape(letter),
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    #c = canvas.Canvas(buff, pagesize=landscape(letter))
    #Cabecera
    #c.setLineWidth(.3)
    #c.setFont('Helvetica', 22)
    #c.drawString(30,550,'Rotary 4690')
    #c.setFont('Helvetica', 12)
    #c.drawString(30,535,'Reporte')

    #c.setFont('Helvetica-Bold', 12)
    #c.drawString(700,550, time.strftime("%d/%m/%Y"))
    #c.line(700,547,760,547)
    #Cabecera de tabla
    #styles = getSampleStyleSheet()
    #styleBH = styles["Normal"]
    #styleBH.alignment = TA_CENTER
    #styleBH.fontSize = 10

    #email = Paragraph('''Email''', styleBH)
    #tipo = Paragraph('''Tipo''', styleBH)
    #monto = Paragraph('''Monto''', styleBH)
    #deposito = Paragraph('''Deposito''', styleBH)
    #participantes = Paragraph('''Participantes''', styleBH)
    #data = [[email, tipo, monto, deposito, participantes]]

    #tabla
    #styleCell = styles["BodyText"]
    #styleCell.alignment = TA_LEFT
    #styleCell.fontSize = 8

    #high = 300
    #for inscripcion in Inscripcion.objects.all():
    #    iemail = Paragraph(inscripcion.email, styleCell)
    #    itipo = Paragraph(str(inscripcion.tipo), styleCell)
    #    imonto = Paragraph(str(inscripcion.monto), styleCell)
    #    ideposito = Paragraph(inscripcion.detalle_deposito, styleCell)
    #    p = ""
    #    for participante in inscripcion.participante_set.all():
    #        p = p + participante.nombres + " " + participante.apellidos + "\n"
    #    print(p)
    #    iparticipantes = Paragraph(str(p), styleCell)
    #    this_inscripcion = [iemail, itipo, imonto, ideposito, iparticipantes]
    #    data.append(this_inscripcion)
    #    high = high - 18

    #width, height = landscape(letter)
    #table = Table(data, colWidths=[4 * cm, 4 * cm, 2.5 * cm, 4 * cm, 11.5 * cm])
    #table.setStyle(TableStyle([
    #    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    #    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    #]))
    #table.wrapOn(c, width, height)
    #table.drawOn(c, 30, high)
    
    #c.showPage()
    cabeza = ParagraphStyle(name="cabeza", alignment=TA_LEFT, fontSize=14, fontName="Times-Roman", textColor=colors.darkblue)
    cabecera = ParagraphStyle(name="cabecera", alignment=TA_CENTER, fontSize=12, fontName="Times-Roman", textColor=colors.white)
    celdaderecha = ParagraphStyle(name="celdaderecha",alignment=TA_RIGHT, fontsize=8, fontName="Times-Roman")
    celda = ParagraphStyle(name="celda", alignment=TA_LEFT, fontsize=8, fontName="Times-Roman")
    celdaverde = ParagraphStyle(name="celdaverde", alignment=TA_CENTER, fontSize=8, fontName="Times-Roman", textColor=colors.green)
    celdaroja = ParagraphStyle(name="celdaroja", alignment=TA_CENTER, fontSize=8, fontName="Times-Roman", textColor=colors.red)

    inscritos = []
    allinscritos = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Inscritos", styles['Heading2'])
    inscritos.append(header)
    headings = (Paragraph('Email', cabecera), Paragraph('Tipo', cabecera), Paragraph('Monto',cabecera), Paragraph('Detalle Deposito', cabecera), Paragraph('Estado',cabecera), Paragraph('Participantes', cabecera))
    topheading = (Paragraph('Rotary 4690', celda))

    for inscripcion in Inscripcion.objects.all():
        iemail = Paragraph(inscripcion.email, celda)
        itipo = Paragraph(TIPO_SELECT[inscripcion.tipo], celda)
        imonto = Paragraph(str(inscripcion.monto), celdaderecha)
        ideposito = Paragraph(inscripcion.detalle_deposito, celda)
        p = ""
        for participante in inscripcion.participante_set.all():
            p = p + participante.nombres + " " + participante.apellidos + "<br />\n"
        iparticipantes = Paragraph(str(p), celda)
        if (inscripcion.estado):
            iestado = Paragraph("Confirmado", celdaverde)
        else:
            iestado = Paragraph("Por Confirmar", celdaroja)
        this_inscripcion = [iemail, itipo, imonto, ideposito, iestado, iparticipantes]
        allinscritos.append(this_inscripcion)

    t = Table([headings] + allinscritos, colWidths=[4 * cm, 3.5 * cm, 2.5 * cm, 4 * cm, 3 * cm, 8 * cm])
    t.setStyle(TableStyle(
       [
            ('GRID', (0, 0), (5, -1), 1, colors.darkblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue)
        ]
    ))
    inscritos.append(t)
    doc.build(inscritos)

    #guardar pdf
    #c.save()
    response.write(buff.getvalue())
    buff.close()
    return response


class ParticipanteUpdateView(UpdateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = 'administracion/update_participante.html'
    success_url = reverse_lazy('administracion')


class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    form_class = InscripcionUpdateForm
    template_name = 'administracion/update_inscripcion.html'
    success_url = reverse_lazy('administracion')

    def form_valid(self, form):
        inscripcion_email = form.cleaned_data['email']
        inscripcion_estado = form.cleaned_data['estado']
        template = get_template('administracion/confirmacion.txt')
        if (inscripcion_estado):
            send_mail(
                'Confirmacion Conferencia Rotary Distrito 4690',
                'Se le ha enviado este correo para confirmar su deposito e inscripcion a la Conferencia Distrital Rotary 4690.',
                'rotaryconfe2018@gmail.com',
                [inscripcion_email],
                fail_silently=False
            )
        return super(InscripcionUpdateView, self).form_valid(form)


def create_parent(request):
    if request.method == 'POST':
        inscripcion_form = InscripcionForm(request.POST, request.FILES, prefix='inscripcion')
        participante_form = ParticipanteFormset(request.POST, request.FILES, prefix='participantes')

        inscripcion_valid = inscripcion_form.is_valid()
        participante_valid = participante_form.is_valid()

        if inscripcion_valid and participante_valid:
            inscripcion = inscripcion_form.save()
            participante_form.instance = inscripcion
            participante_form.save()
            return render(request, 'forms/form_success.html')
    else:
        inscripcion_form = InscripcionForm(prefix='inscripcion')
        participante_form = ParticipanteFormset(prefix='participantes')

    return render(request, 'forms/registro_ajax.html', {'inscripcion_form': inscripcion_form,
                                                        'participante_forms': participante_form})


def create_parents(request):
    if request.method == 'POST':
        inscripcion_form = InscripcionForm(request.POST, request.FILES, prefix='inscripcion')
        
        participantes_form = ParticipantesFormset(request.POST, request.FILES, prefix='participantes')

        inscripcion_valid = inscripcion_form.is_valid()
        participantes_valid = participantes_form.is_valid()

        if inscripcion_valid and participantes_valid:
            inscripcion = inscripcion_form.save()
            participantes_form.instance = inscripcion
            participantes_form.save()
            return render(request, 'forms/form_success.html')
    else:
        inscripcion_form = InscripcionForm(prefix='inscripcion')
        participantes_form = ParticipantesFormset(prefix='participantes')

    return render(request, 'forms/registros_ajax.html', {'inscripcion_form': inscripcion_form,
                                                        'participante_forms': participantes_form})
