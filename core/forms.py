from django import forms
from . models import *

class AddPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        widgets = {
            'observacoes': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 3,
            })
        }

    def __init__(self, *args, **kwargs):
        super(AddPizzaForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs['class'] = 'form-control form-control-sm'

class AddSaborForm(forms.ModelForm):
    class Meta:
        model = Sabor
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 3,
            })
        }
          
    def __init__(self, *args, **kwargs):
        super(AddSaborForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs['class'] = 'form-control form-control-sm'
