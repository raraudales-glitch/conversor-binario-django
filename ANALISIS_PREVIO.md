# Análisis previo al desarrollo

## Entrada

- Número binario como texto.
- Tipo de conversión: decimal u octal.

## Proceso

Validar que el número contenga únicamente 0 y 1. Después, convertir según la opción seleccionada.

## Salida

Mostrar el número original, el tipo de conversión y el resultado.

## Pseudocódigo: binario a decimal

```text
INICIO
    recibir numero_binario
    decimal ← 0

    PARA cada digito del numero_binario HACER
        SI digito = "1" ENTONCES
            bit ← 1
        SI NO
            bit ← 0
        FIN SI

        decimal ← decimal × 2 + bit
    FIN PARA

    devolver decimal
FIN
```

## Pseudocódigo: binario a octal

```text
INICIO
    recibir numero_binario
    decimal ← binario_a_decimal(numero_binario)

    SI decimal = 0 ENTONCES
        devolver "0"
    FIN SI

    digitos ← lista vacía

    MIENTRAS decimal > 0 HACER
        residuo ← decimal MOD 8
        agregar residuo a digitos
        decimal ← decimal DIV 8
    FIN MIENTRAS

    invertir digitos
    devolver digitos
FIN
```

## Conversión manual

```text
110101₂
= 1×2⁵ + 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
= 32 + 16 + 0 + 4 + 0 + 1
= 53₁₀
```

Para octal:

```text
110 101
 6   5

110101₂ = 65₈
```

## Recorrido

```text
Formulario → ruta → vista → función de conversión → plantilla
```
