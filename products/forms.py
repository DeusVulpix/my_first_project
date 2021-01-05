from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    title       = forms.CharField(label='',
                        widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Your title",
                                }
                            )
                        )

    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 4,
                                    "cols": 60
                                }
                            )
                        )
    price       = forms.DecimalField()

    show        = forms.NullBooleanField()

    summary     = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Summary",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 4,
                                    "cols": 60
                                }
                            )
                        )
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price'
        ]
