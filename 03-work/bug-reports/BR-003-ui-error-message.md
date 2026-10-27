# Bug Report

**Título:** Mensaje de error no describe causa ni cómo corregir  
**ID:** BR-003-ui-error-message
**Estado:** Hipótesis pendiente de reproducción; no confirmado.

## Ambiente
- OS: Windows 11
- Navegador/App: Chrome (última)
- URL / Build / Versión: https://www.demoblaze.com/ (versión no identificada)

## Precondiciones
- Usuario con carrito con al menos 1 ítem (si aplica)

## Pasos para reproducir
1. Ir a checkout / formulario de compra
2. Borrar campos obligatorios (Nombre, Dirección, etc.)
3. Enviar formulario

## Resultado actual
- Hipótesis a verificar: el comportamiento descrito podría ocurrir; aún no fue reproducido.

## Resultado esperado
- Verificar que el sitio rechace datos incompletos y explique qué debe corregirse.

## Severidad
- Baja

## Prioridad
- P3

## Frecuencia
- Siempre

## Evidencia
- Captura pendiente (no adjunta; caso no ejecutado): `04-evidence/screenshots/BR-003-ui-error-message.png`

## Notas
- Recomendar validaciones client-side + server-side.
