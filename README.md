# Servicio de Sedes

## Descripción

Este servicio permite gestionar las sedes del sistema académico. Proporciona funcionalidades para crear, obtener y listar sedes, facilitando su integración con otros módulos.

## Endpoints

### Registrar una sede

**POST** `/sedes/`

#### Request Body

```json
{
  "nombre": "Sede Principal"
}
```

#### Response

**Status:** 200 OK

```json
{
  "id_sede": 1,
  "nombre": "Sede Principal"
}
```

### Obtener una sede por ID

**GET** `/sedes/{id_sede}`

#### Response

**Status:** 200 OK

```json
{
  "id_sede": 1,
  "nombre": "Sede Principal"
}
```

**Status:** 404 Not Found

```json
{
  "detail": "Sede not found"
}
```

### Listar todas las sedes

**GET** `/sedes/`

#### Response

**Status:** 200 OK

```json
[
  {
    "id_sede": 1,
    "nombre": "Sede Principal"
  },
  {
    "id_sede": 2,
    "nombre": "Sede Secundaria"
  }
]
```

## Instalación

1. Asegúrate de tener el entorno configurado:

   ```bash
   pip install -r requirements.txt
   ```
2. Configura la base de datos en el archivo `.env`:

   ```env
   DATABASE_URL="mysql+pymysql://user:password@host:port/database"
   ```
3. Ejecuta el servidor:

   ```bash
   uvicorn app.main:app --reload --port 8006
   ```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest app/tests/test_sedes.py
```

## Dependencias

* **FastAPI**: Framework principal.
* **SQLAlchemy**: ORM para manejar la base de datos.
* **Pytest**: Framework para pruebas unitarias.

## Documentación interactiva

Accede a la documentación Swagger en [http://localhost:8007/docs](http://localhost:8007/docs) o ReDoc en [http://localhost:8007/redoc](http://localhost:8007/redoc).

## Contacto

Para más información, cont