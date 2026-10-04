def binario_a_decimal(numero_binario):
    """
    Convierte manualmente una cadena binaria a decimal.

    No utiliza int(valor, 2) ni ninguna función automática de conversión.
    Para cada dígito se desplaza el resultado una posición binaria:
        resultado = resultado * 2 + bit
    """
    decimal = 0

    for digito in numero_binario:
        bit = 1 if digito == "1" else 0
        decimal = decimal * 2 + bit

    return decimal


def binario_a_octal(numero_binario):
    """
    Convierte una cadena binaria a octal.

    Primero obtiene el valor decimal mediante binario_a_decimal.
    Después aplica divisiones sucesivas entre 8 y conserva los residuos.
    """
    decimal = binario_a_decimal(numero_binario)

    if decimal == 0:
        return "0"

    digitos = []

    while decimal > 0:
        residuo = decimal % 8
        digitos.append(str(residuo))
        decimal //= 8

    # Los residuos se obtienen de derecha a izquierda.
    digitos.reverse()
    return "".join(digitos)
