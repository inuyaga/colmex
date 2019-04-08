from django import forms
from aplicaciones.admisiones.models import Prospecto
class ProspectoForm(forms.ModelForm):
    class Meta:
        model = Prospecto
        fields = '__all__'
        widgets= {
        'prospecto_naciminto' : forms.DateInput(attrs={'type': 'date'}),
        'prospecto_programa_inicio': forms.DateInput(attrs={'type': 'date'}),
        'prospecto_programa_termino': forms.DateInput(attrs={'type': 'date'}),
        'prospecto_cedula_expedicion': forms.DateInput(attrs={'type': 'date'}),
        'prospecto_interes': forms.Textarea(attrs={'cols': 25, 'rows': 5}),
        }
    def __init__(self, *args, **kwargs):
        super(ProspectoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
class ProspectoFormEdit(forms.ModelForm):
    class Meta:
        model = Prospecto
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProspectoFormEdit, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})







