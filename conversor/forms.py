from django import forms


class ConversorForm(forms.Form):
    numero_binario = forms.CharField(
        label="Número binario",
        max_length=255,
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ejemplo: 110101",
                "autocomplete": "off",
                "inputmode": "numeric",
            }
        ),
    )

    tipo_conversion = forms.ChoiceField(
        label="Convertir a",
        choices=[
            ("decimal", "Decimal"),
            ("octal", "Octal"),
        ],
        widget=forms.Select(),
    )

    def clean_numero_binario(self):
        valor = self.cleaned_data["numero_binario"]

        if not valor:
            raise forms.ValidationError(
                "Debe ingresar un número binario."
            )

        # Validación explícita en el servidor.
        if any(caracter not in "01" for caracter in valor):
            raise forms.ValidationError(
                "El valor solo puede contener los caracteres 0 y 1."
            )

        return valor

    def clean_tipo_conversion(self):
        tipo = self.cleaned_data["tipo_conversion"]
        opciones_validas = {"decimal", "octal"}

        if tipo not in opciones_validas:
            raise forms.ValidationError(
                "El tipo de conversión seleccionado no es válido."
            )

        return tipo
