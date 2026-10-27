# Bug Report

**Título:** Checkout permite enviar formulario con campos obligatorios vacíos  
**ID:** BR-001-checkout-validation
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
- Alta

## Prioridad
- P0

## Frecuencia
- Siempre

## Evidencia
- Captura pendiente (no adjunta; caso no ejecutado): `04-evidence/screenshots/BR-001-checkout-validation.png`

## Notas
- Recomendar validaciones client-side + server-side.
