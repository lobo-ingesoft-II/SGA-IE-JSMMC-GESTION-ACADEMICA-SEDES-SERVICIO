# Changelog - Servicio de Sedes

## [1.0.0] - 2025-06-09
### Agregado
- Creación del servicio de sedes.
- Endpoint **POST** `/sedes/` para registrar una nueva sede.
- Endpoint **GET** `/sedes/{id_sede}` para obtener una sede por ID.
- Endpoint **GET** `/sedes/` para listar todas las sedes.
- Integración de modelos, esquemas y servicios con SQLAlchemy y Pydantic.
- Pruebas unitarias básicas para las operaciones CRUD de sedes.

## [1.1.0] - 2025-07-05
### Agregado
- Modelo ORM `ProfesorSede` y esquemas Pydantic para la tabla intermedia `profesor_sede`.
- Servicio `assign_profesor_sede` y `get_sedes_by_profesor` con validación de `auth_api`.
- Endpoint **POST** `/sedes/profesor_sede/` para asignar un profesor a una sede.
- Endpoint **GET** `/sedes/por_profesor/{id_profesor}` para listar sedes asignadas a un profesor.
