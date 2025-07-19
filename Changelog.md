# Changelog - Servicio de Sedes

- Creación del servicio de sedes.
- Endpoint **POST** `/sedes/` para registrar una nueva sede.
- Endpoint **GET** `/sedes/{id_sede}` para obtener una sede por ID.
- Endpoint **GET** `/sedes/` para listar todas las sedes.
- Integración de modelos, esquemas y servicios con SQLAlchemy y Pydantic.
- Pruebas unitarias básicas para las operaciones CRUD de sedes.


## [1.0.0] - 2025-06-09
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



