from django.test import TestCase

from .conversiones import binario_a_decimal, binario_a_octal
from .forms import ConversorForm


class ConversionesTest(TestCase):
    def test_binario_a_decimal(self):
        casos = {
            "0": 0,
            "1": 1,
            "1010": 10,
            "110101": 53,
            "11111111": 255,
            "000101": 5,
        }

        for entrada, esperado in casos.items():
            with self.subTest(entrada=entrada):
                self.assertEqual(binario_a_decimal(entrada), esperado)

    def test_binario_a_octal(self):
        casos = {
            "0": "0",
            "1": "1",
            "1010": "12",
            "110101": "65",
            "11111111": "377",
            "000101": "5",
        }

        for entrada, esperado in casos.items():
            with self.subTest(entrada=entrada):
                self.assertEqual(binario_a_octal(entrada), esperado)


class ValidacionesTest(TestCase):
    def test_rechaza_valores_invalidos(self):
        for valor in ["", "10201", "abc", "10 01"]:
            with self.subTest(valor=valor):
                form = ConversorForm(
                    data={
                        "numero_binario": valor,
                        "tipo_conversion": "decimal",
                    }
                )
                self.assertFalse(form.is_valid())
                self.assertIn("numero_binario", form.errors)

    def test_acepta_valores_validos(self):
        form = ConversorForm(
            data={
                "numero_binario": "110101",
                "tipo_conversion": "decimal",
            }
        )
        self.assertTrue(form.is_valid())

    def test_rechaza_tipo_conversion_invalido(self):
        form = ConversorForm(
            data={
                "numero_binario": "110101",
                "tipo_conversion": "hexadecimal",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("tipo_conversion", form.errors)


class VistaTest(TestCase):
    def test_pagina_inicial(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Conversor binario")

    def test_conversion_decimal_desde_formulario(self):
        response = self.client.post(
            "/",
            {
                "numero_binario": "110101",
                "tipo_conversion": "decimal",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "53")

    def test_conversion_octal_desde_formulario(self):
        response = self.client.post(
            "/",
            {
                "numero_binario": "110101",
                "tipo_conversion": "octal",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "65")
