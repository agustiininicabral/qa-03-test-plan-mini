# Alcance del plan de pruebas

## Sistema bajo prueba
Sitio público de demostración: https://www.demoblaze.com/ . Registrar fecha y versión del navegador durante la ejecución.

## Objetivo
Definir una estrategia breve y priorizada para verificar catálogo, detalle de producto, carrito y formulario de compra. Este documento define el plan; no afirma que las pruebas se hayan ejecutado.

## Dentro del alcance
- Navegación y visualización de productos.
- Agregar productos y verificar el total del carrito.
- Validación del formulario de compra.
- Carrito vacío, actualización de página y doble confirmación.
- Registro de resultados y evidencia.

## Fuera del alcance
- Compras o pagos reales y datos personales.
- Pruebas de carga y pentesting.
- Garantías sobre un sitio público de terceros.

## Riesgos
- P1: compra confirmada con datos incompletos o total incorrecto.
- P2: pérdida del carrito o mensajes de error poco claros.
- P3: problemas menores de navegación.

## Criterios de entrada
- Sitio accesible, navegador disponible y datos ficticios preparados.

## Criterios de salida
- Ejecutar todos los casos P1 o documentar el bloqueo.
- Registrar el estado de cada caso y adjuntar evidencia para fallos reproducibles.
- Emitir Go/No-Go solo con resultados reales suficientes.

Los casos no ejecutados deben permanecer como Not executed. Las hipótesis no son defectos confirmados sin reproducción y evidencia.
