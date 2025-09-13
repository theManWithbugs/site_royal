from django.core.exceptions import ValidationError
from django import forms
from . models import *

# class AddPizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['tamanho', 'sabores']

#     def clean_sabores(self):
#         sabores = self.cleaned_data.get('sabores')
#         tamanho = self.cleaned_data.get('tamanho')

#         if tamanho and sabores and len(sabores) > tamanho.max_sabores:
#             raise ValidationError(
#                 f"O tamanho {tamanho.nome} permite no máximo {tamanho.max_sabores} sabores."
#             )
#         return sabores

class AddPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['sabores', 'observacoes']
        exclude = ['tamanho']
        widgets = {
            'observacoes': forms.Textarea(attrs={'class': 'form-control form-control-sm w-50', 'rows': 3}),
            'sabores': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        self.tamanho = kwargs.pop('tamanho', None)
        super().__init__(*args, **kwargs)

    def clean_sabores(self):
        sabores = self.cleaned_data.get('sabores')
        if self.tamanho and sabores and len(sabores) > self.tamanho.max_sabores:
            raise forms.ValidationError(
                f"O tamanho {self.tamanho.nome} permite no máximo {self.tamanho.max_sabores} sabores."
            )
        return sabores

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
