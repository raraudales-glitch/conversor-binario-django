# Conversor numérico en Django

Aplicación web académica para la asignatura **Arquitectura de Computadoras**, primer parcial: **Sistemas numéricos y representación de datos**.

La aplicación recibe un número binario y permite convertirlo manualmente a **decimal** o **octal**.

## 1. Requerimientos de la actividad

El proyecto cumple los siguientes puntos solicitados:

- Aplicación web desarrollada con Django.
- Conversión de binario a decimal.
- Conversión de binario a octal.
- Patrón Modelo–Vista–Plantilla (MVT).
- Formulario Django.
- Validación de los datos en el servidor.
- Mensajes de error.
- Separación de la lógica de conversión y la presentación.
- Pruebas de los casos indicados.
- Sin necesidad de almacenar un historial en base de datos.
- Documentación del uso de inteligencia artificial como tutor y revisor.

## 2. Requisitos del entorno

Se requiere:

- Python 3.12 o superior recomendado.
- pip.
- Django.

El proyecto no incluye el entorno virtual `.venv`, de acuerdo con la instrucción de entrega.

## 3. Instalación en Fedora/Linux

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Comprobar Django:

```bash
python -m django --version
```

Aplicar las migraciones internas de Django:

```bash
python manage.py migrate
```

Ejecutar las pruebas:

```bash
python manage.py test
```

Iniciar el servidor:

```bash
python manage.py runserver
```

Abrir:

```text
http://127.0.0.1:8000/
```

## 4. Inicialización desde cero

Si se quisiera reconstruir el proyecto, los comandos principales son:

```bash
mkdir conversor-binario
cd conversor-binario

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install django

django-admin startproject config .
python manage.py startapp conversor

mkdir -p conversor/templates/conversor

python manage.py migrate
python manage.py runserver
```

Después se incorporan los archivos fuente incluidos en este proyecto.

## 5. Estructura del proyecto

```text
conversor-binario/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── conversor/
│   ├── migrations/
│   ├── templates/
│   │   └── conversor/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── conversiones.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## 6. Análisis previo

### 6.1 Entrada

La aplicación recibe dos datos:

1. `numero_binario`: cadena formada exclusivamente por `0` y `1`.
2. `tipo_conversion`: puede ser `decimal` u `octal`.

### 6.2 Proceso

El formulario envía los datos mediante HTTP POST.

La vista recibe la solicitud y delega la validación al formulario. Si los datos son válidos, la vista llama a la función correspondiente de `conversiones.py`.

Para decimal se utiliza `binario_a_decimal()`.

Para octal se utiliza `binario_a_octal()`, que primero obtiene el valor decimal y posteriormente realiza divisiones sucesivas entre 8.

### 6.3 Salida

La plantilla muestra:

- Número original.
- Tipo de conversión.
- Resultado.
- Cantidad de dígitos ingresados.

Si la validación falla, se muestran mensajes indicando qué debe corregirse.

## 7. Pseudocódigo inicial

### 7.1 Binario a decimal

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

La operación `decimal × 2` desplaza el valor acumulado una posición en la representación binaria. Al agregar el bit actual se incorpora el nuevo dígito.

### 7.2 Binario a octal

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

    devolver digitos como texto
FIN
```

Los residuos se obtienen desde el dígito octal menos significativo hacia el más significativo, por lo que deben invertirse antes de presentar el resultado.

## 8. Conversión manual de 110101₂

### 8.1 A decimal

Se utilizan los pesos de las posiciones binarias:

```text
110101₂

= 1×2⁵ + 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰

= 32 + 16 + 0 + 4 + 0 + 1

= 53₁₀
```

Por tanto:

```text
110101₂ = 53₁₀
```

### 8.2 A octal

Se puede utilizar el valor decimal y aplicar divisiones sucesivas entre 8:

```text
53 ÷ 8 = 6  residuo 5
 6 ÷ 8 = 0  residuo 6
```

Los residuos se leen de abajo hacia arriba:

```text
65₈
```

Por tanto:

```text
110101₂ = 65₈
```

También se observa directamente la agrupación de tres bits:

```text
110 101
 ↓   ↓
 6   5

= 65₈
```

## 9. Recorrido de los datos

```text
Formulario HTML
      │
      ▼
POST /
      │
      ▼
conversor.urls
      │
      ▼
views.inicio()
      │
      ▼
ConversorForm
      │
      ├── Validación del número
      └── Validación del tipo
      │
      ▼
conversiones.py
      │
      ├── binario_a_decimal()
      │
      └── binario_a_octal()
      │
      ▼
views.inicio()
      │
      ▼
index.html
      │
      ▼
Resultado mostrado
```

## 10. Relación con MVT

### Modelo

No se utiliza un modelo porque la actividad no requiere almacenar conversiones.

Si posteriormente se quisiera almacenar un historial, podría crearse un modelo con:

- número binario;
- tipo de conversión;
- resultado;
- fecha y hora.

### Vista

`conversor/views.py` contiene `inicio()`.

La vista:

1. Recibe la solicitud.
2. Crea o procesa el formulario.
3. Verifica si los datos son válidos.
4. Llama a la función de conversión correspondiente.
5. Envía los datos a la plantilla.

### Plantilla

`conversor/templates/conversor/index.html` presenta la interfaz y muestra:

- formulario;
- errores;
- número original;
- tipo de conversión;
- resultado;
- cantidad de dígitos.

### Lógica de negocio

La conversión se separa de la vista en:

```text
conversor/conversiones.py
```

Esto evita colocar el algoritmo numérico directamente dentro de la plantilla o mezclarlo innecesariamente con el procesamiento HTTP.

## 11. Restricciones de conversión

No se utilizan:

```python
int(valor, 2)
oct()
eval()
```

ni librerías que realicen automáticamente las conversiones.

La conversión decimal utiliza un ciclo y operaciones aritméticas.

La conversión octal utiliza divisiones sucesivas entre 8:

```python
residuo = decimal % 8
decimal //= 8
```

## 12. Validaciones

Las validaciones se realizan en el servidor mediante `ConversorForm`.

Se rechazan:

```text
vacío
10201
abc
10 01
```

Se aceptan únicamente cadenas cuyos caracteres sean `0` o `1`.

También se valida que el tipo de conversión pertenezca al conjunto:

```text
decimal
octal
```

El navegador puede utilizar atributos HTML para facilitar la entrada, pero la decisión final se realiza en Django.

## 13. Pruebas

Los casos solicitados son:

| Entrada | Decimal esperado | Octal esperado |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 1010 | 10 | 12 |
| 110101 | 53 | 65 |
| 11111111 | 255 | 377 |
| 000101 | 5 | 5 |

Además:

| Entrada | Resultado esperado |
|---|---|
| vacío | Rechazada |
| 10201 | Rechazada |
| abc | Rechazada |
| 10 01 | Rechazada |

Para ejecutar las pruebas:

```bash
python manage.py test
```

Las pruebas automatizadas se encuentran en:

```text
conversor/tests.py
```

## 14. Relación con Arquitectura de Computadoras

### ¿Por qué la computadora utiliza representación binaria?

Los circuitos digitales trabajan naturalmente con estados discretos que pueden representarse mediante dos niveles lógicos. Por ello, los estados se modelan mediante los valores `0` y `1`.

### ¿Por qué octal puede agrupar bits?

Como:

```text
8 = 2³
```

cada dígito octal representa exactamente tres bits.

Por ejemplo:

```text
000 → 0
001 → 1
010 → 2
011 → 3
100 → 4
101 → 5
110 → 6
111 → 7
```

Por ello:

```text
110101₂
```

puede separarse como:

```text
110 101
 6   5
```

y obtener:

```text
65₈
```

### Mayor entero sin signo representable con 8 bits

Con 8 bits existen:

```text
2⁸ = 256
```

combinaciones posibles.

Como se empieza en cero, el mayor valor es:

```text
2⁸ - 1 = 255
```

Por tanto:

```text
11111111₂ = 255₁₀
```

## 15. Modificación para la defensa

La aplicación muestra actualmente la cantidad de dígitos ingresados:

```text
Cantidad de dígitos: 6
```

Esto corresponde a una modificación pequeña del tipo solicitado en la defensa.

Para demostrar comprensión, el estudiante debería poder explicar que la plantilla obtiene la longitud mediante:

```django
{{ datos_resultado.numero|length }}
```

Esta modificación puede servir como práctica antes de la defensa, pero durante la demostración debe poder realizarse sin consultar a la IA.

## 16. Bitácora de uso de IA

> Esta sección debe mantenerse como registro de las interacciones reales utilizadas durante el desarrollo. No debe presentarse como si fueran consultas realizadas en otra fecha.

### Interacción 1 — Comprensión

**Consulta:**

> Revisa mi pseudocódigo de conversión binaria. Señala errores y dame pistas sin escribir la solución completa.

**Propósito:**

Revisar la lógica antes de implementar las funciones.

**Recomendación obtenida:**

Separar la conversión binario→decimal de la conversión binario→octal y utilizar operaciones aritméticas para conservar el objetivo didáctico.

**Decisión:**

Se aceptó la separación de responsabilidades.

**Verificación:**

Se comprobó manualmente `110101₂ = 53₁₀`.

### Interacción 2 — Desarrollo

**Consulta:**

> Necesito implementar el conversor en Django. ¿Cómo puedo separar formulario, rutas, vista, lógica de conversión y plantilla siguiendo MVT?

**Propósito:**

Definir la estructura del proyecto.

**Recomendación obtenida:**

Utilizar un formulario Django para la validación, una vista para coordinar la solicitud, un archivo separado para los algoritmos y una plantilla para la presentación.

**Decisión:**

Se aceptó esta estructura.

**Verificación:**

Se comprobó el recorrido:

```text
formulario → ruta → vista → función de conversión → plantilla
```

### Interacción 3 — Verificación

**Consulta:**

> Revisa los casos de prueba de un conversor binario a decimal y octal y señala entradas que podrían revelar errores.

**Propósito:**

Comprobar el algoritmo y las validaciones.

**Recomendación obtenida:**

Probar cero, números con ceros iniciales, entradas con caracteres distintos de `0` y `1`, y el caso `11111111`.

**Decisión:**

Se incorporaron los casos solicitados por la actividad y pruebas automatizadas para ellos.

**Verificación:**

Se ejecutó:

```bash
python manage.py test
```

y se comprobó además manualmente el caso:

```text
110101₂ = 53₁₀ = 65₈
```

## 17. Evidencia de comprensión

Para la defensa se debe poder explicar:

1. Que `forms.py` valida los datos en el servidor.
2. Que `urls.py` dirige `/` hacia `views.inicio`.
3. Que `views.py` coordina el formulario y la conversión.
4. Que `conversiones.py` contiene los algoritmos.
5. Que `index.html` presenta los datos.
6. Que `binario_a_decimal()` procesa cada bit mediante un ciclo.
7. Que la conversión octal obtiene residuos mediante `% 8` y reduce el número mediante `// 8`.
8. Que el caso `0` necesita tratamiento porque no debe producir una cadena vacía.

## 18. Entrega

Antes de comprimir el proyecto, eliminar:

```text
.venv/
__pycache__/
db.sqlite3
```

El proyecto entregable debe contener:

- código fuente;
- `requirements.txt`;
- `README.md`;
- pruebas;
- pseudocódigo;
- conversión manual;
- bitácora de IA.

No se debe entregar el entorno virtual.
