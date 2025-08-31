from django import forms
from .models import *

class form_investimentos(forms.ModelForm):
  class Meta:
    model = Investimentos
    fields = '__all__'
    exclude = ['user', 'data']
    widgets = {
      'descricao': forms.Textarea(attrs={
          'class': 'form-control form-control-sm',
          'rows': 3,
          'placeholder': 'Descrição do material...',
      }),
    }

  def __init__(self, *args, **kwargs):
    super(form_investimentos, self).__init__(*args, **kwargs)
    for i in self.fields:
        self.fields[i].widget.attrs['class'] = 'form-control form-control-sm'