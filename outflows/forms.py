from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from . import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'description': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponivel em estoque para o produto {product.title} e de {product.quantity} unidades.'
            )
        
        return quantity