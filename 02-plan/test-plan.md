# Mini Test Plan

## 1. Objetivo
Verificar los flujos principales de un sitio de comercio electrónico de demostración y registrar riesgos relevantes antes de recomendar una salida.

## 2. Sistema y ambiente
- Sistema bajo prueba: https://www.demoblaze.com/
- Navegador propuesto: Chrome estable.
- Sistema operativo: Windows 11 o Ubuntu actualizado.
- Datos: únicamente datos ficticios.
- Registro obligatorio: fecha, navegador, resultado observado y evidencia.

El sitio es externo y puede cambiar; repetir las pruebas antes de utilizar el plan en una evaluación real.

## 3. Estrategia
- Pruebas manuales funcionales con prioridad basada en riesgo.
- Ejecutar primero los casos P1: catálogo, carrito, total, formulario y confirmación.
- Después ejecutar los casos P2/P3 de estado vacío, persistencia y mensajes.
- Repetir un fallo al menos una vez antes de registrarlo como reproducible, salvo que repetirlo genere una acción irreversible.
- No realizar pagos reales ni usar datos personales.

## 4. Alcance
Incluye navegación, detalle de producto, carrito, total, formulario de compra y estados límite. Excluye carga, pentesting, pagos reales y validación de sistemas fuera del sitio de demostración.

## 5. Datos de prueba
Usar nombres, direcciones y números ficticios aceptados por el sitio. No introducir información personal o financiera real. Anotar los datos ficticios necesarios para que otro tester pueda repetir el caso.

## 6. Riesgos y mitigación
- **P1 — Compra incorrecta:** verificar campos requeridos, total y confirmación.
- **P1 — Total incorrecto:** comparar el total con los precios de los ítems.
- **P2 — Pérdida del carrito:** repetir la revisión tras actualizar la página.
- **P2 — Mensajes ambiguos:** registrar texto exacto y captura.
- **Dependencia externa:** registrar disponibilidad del sitio y diferenciar fallos del sitio de problemas de red.

## 7. Entrada
- Sitio accesible.
- Casos y datos revisados.
- Navegador disponible y carpeta de evidencia preparada.

## 8. Salida
- Todos los casos P1 ejecutados o bloqueos documentados.
- Cada caso ejecutado tiene resultado Pass, Fail o Blocked.
- Todo defecto confirmado tiene pasos reproducibles, ambiente y evidencia.
- Go/No-Go basado en resultados reales; nunca deducido de casos aún no ejecutados.

## 9. Entregables
- Matriz CSV de casos de prueba.
- Bug reports con estado de verificación.
- Evidencia real de ejecución.
- Reporte final con conteos y recomendación respaldada.

## 10. Estado actual
El repositorio contiene un plan de prueba y escenarios preparados. No se han ejecutado las pruebas contra el sitio; el reporte debe permanecer como No evaluado hasta registrar resultados.
