# Mini Test Plan

Portfolio de QA Manual que demuestra cómo convertir requisitos y riesgos en una estrategia de prueba breve, priorizada y verificable.

## Entregables
- `01-requirements/scope.md`: alcance, riesgos y criterios de entrada/salida.
- `01-requirements/user-stories.md`: historias con criterios de aceptación.
- `02-plan/test-plan.md`: estrategia, datos, riesgos, criterios y entregables.
- `03-work/test-cases.csv`: matriz de 10 casos priorizados.
- `03-work/bug-reports/`: ejemplos pendientes de reproducción.
- `05-results/report.md`: estado real de ejecución y recomendación.

## Sistema bajo prueba propuesto
https://www.demoblaze.com/

El sitio es externo y puede cambiar. Los resultados esperados son criterios por verificar, no afirmaciones de que el sitio tenga defectos. Los casos están en estado `Not executed` hasta que se ejecuten.

## Método
1. Revisar el alcance y los riesgos.
2. Ejecutar primero los casos P1 con datos ficticios.
3. Registrar Pass, Fail o Blocked solo después de la ejecución.
4. Adjuntar evidencia real y documentar únicamente defectos reproducibles.
5. Emitir Go/No-Go cuando los resultados sean suficientes.

## Validación de artefactos
El repositorio incluye controles estáticos para confirmar que el plan contiene sus secciones esenciales, que los IDs de casos son únicos y que el reporte no afirma resultados antes de la ejecución.

```powershell
python scripts/validate_plan.py
python -m unittest discover -s tests -v
```

Estos controles validan la documentación; no ejecutan el sitio ni reemplazan las pruebas manuales.

## Estado actual
El plan está preparado, pero la ejecución está pendiente. El reporte indica **No evaluado** hasta que existan resultados y evidencias.

## Licencia
MIT. Consultá [LICENSE](LICENSE).
