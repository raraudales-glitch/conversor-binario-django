from django.shortcuts import render

from .conversiones import binario_a_decimal, binario_a_octal
from .forms import ConversorForm


def inicio(request):
    resultado = None
    datos_resultado = None

    if request.method == "POST":
        form = ConversorForm(request.POST)

        if form.is_valid():
            numero = form.cleaned_data["numero_binario"]
            tipo = form.cleaned_data["tipo_conversion"]

            if tipo == "decimal":
                resultado = binario_a_decimal(numero)
                nombre_tipo = "Decimal"
            else:
                resultado = binario_a_octal(numero)
                nombre_tipo = "Octal"

            datos_resultado = {
                "numero": numero,
                "tipo": nombre_tipo,
                "resultado": resultado,
            }
    else:
        form = ConversorForm()

    contexto = {
        "form": form,
        "resultado": resultado,
        "datos_resultado": datos_resultado,
    }

    return render(request, "conversor/index.html", contexto)
