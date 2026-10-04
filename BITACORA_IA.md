# Bitácora de uso de inteligencia artificial

La IA se utilizó como tutor y revisor durante el desarrollo. No se implementó ninguna conexión entre la aplicación Django y una API de IA.

## 1. Comprensión

**Consulta:** Revisión del pseudocódigo de conversión binaria.

**Objetivo:** Detectar errores conceptuales antes de programar.

**Recomendación:** Separar las funciones y mantener el cálculo manual.

**Decisión:** Aceptada.

**Verificación:** Conversión manual de `110101₂` a `53₁₀`.

## 2. Desarrollo

**Consulta:** Organización de formulario, rutas, vista, lógica y plantilla en Django.

**Objetivo:** Mantener una estructura MVT clara.

**Recomendación:** Utilizar `forms.py` para validación, `views.py` para coordinar el flujo y `conversiones.py` para la lógica numérica.

**Decisión:** Aceptada.

**Verificación:** Flujo funcional desde el formulario hasta el resultado.

## 3. Verificación

**Consulta:** Revisión de casos de prueba y validaciones.

**Objetivo:** Encontrar errores que no aparecieran con una entrada normal.

**Recomendación:** Probar cero, ceros iniciales, `11111111` y entradas inválidas.

**Decisión:** Aceptada.

**Verificación:** Ejecución de:

```bash
python manage.py test
```

y comprobación manual de `110101 → 53 / 65`.

> Importante: para la entrega final, conservar las consultas reales realizadas al asistente y, si el docente lo solicita, agregar capturas de las conversaciones como evidencia.
