# Changelog - Servicio de Sedes

## [1.1.0] - 2025-07-05
### Agregado
- Modelo ORM `ProfesorSede` y esquemas Pydantic para la tabla intermedia `profesor_sede`.
- Servicio `assign_profesor_sede` y `get_sedes_by_profesor` con validación de `auth_api`.
- Endpoint **POST** `/sedes/profesor_sede/` para asignar un profesor a una sede.
- Endpoint **GET** `/sedes/por_profesor/{id_profesor}` para listar sedes asignadas a un profesor.

## [1.2.0] - 2025-07-08
### Agregado
- Instrumentación Prometheus: contador de peticiones, histograma de latencia (buckets ajustados), contador de errores y endpoint `/metrics`.
- Configuración de Prometheus (`prometheus.yml`) para scrapear el servicio de sedes.
- Pruebas de integración para endpoints CRUD de sedes y rutas `profesor_sede`.
- Script de generación de reporte PDF de resultados de pruebas.


## [1.2.1] - 2025-07-13
### Agregado
- Pruebas unitarias básicas con pytest y FastAPI TestClient para los endpoints de sedes y profesor-sede.