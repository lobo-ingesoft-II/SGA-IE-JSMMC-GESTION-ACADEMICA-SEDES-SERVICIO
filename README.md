```markdown
# Servicio de Sedes

## Descripción

Este servicio permite gestionar las sedes del sistema académico. Proporciona funcionalidades para crear, obtener, actualizar, listar y eliminar sedes, facilitando su integración con otros módulos.

## Endpoints

Todas las rutas parten de la raíz `/sedes`.

| Método | Ruta                   | Descripción                        |
| ------ | ---------------------- | ---------------------------------- |
| POST   | `/sedes/`              | Crear una nueva sede               |
| GET    | `/sedes/`              | Listar todas las sedes             |
| GET    | `/sedes/{id_sede}`     | Obtener una sede por su ID         |
| PUT    | `/sedes/{id_sede}`     | Actualizar el nombre de una sede   |
| DELETE | `/sedes/{id_sede}`     | Eliminar una sede                  |

### 1. Crear una sede

```

POST /sedes/
Content-Type: application/json

````

#### Request Body

```json
{
  "nombre": "Sede Principal"
}
````

#### Response

**200 OK**

```json
{
  "id_sede": 1,
  "nombre": "Sede Principal"
}
```

### 2. Listar sedes

```
GET /sedes/
```

#### Response

**200 OK**

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

### 3. Obtener una sede por ID

```
GET /sedes/{id_sede}
```

#### Response

* **200 OK**

  ```json
  {
    "id_sede": 1,
    "nombre": "Sede Principal"
  }
  ```

* **404 Not Found**

  ```json
  {
    "detail": "Sede no encontrada"
  }
  ```

### 4. Actualizar una sede

```
PUT /sedes/{id_sede}
Content-Type: application/json
```

#### Request Body

```json
{
  "nombre": "Sede Principal Actualizada"
}
```

#### Response

* **200 OK**

  ```json
  {
    "id_sede": 1,
    "nombre": "Sede Principal Actualizada"
  }
  ```

* **404 Not Found**

  ```json
  {
    "detail": "Sede no encontrada"
  }
  ```

### 5. Eliminar una sede

```
DELETE /sedes/{id_sede}
```

#### Response

* **204 No Content**

* **404 Not Found**

  ```json
  {
    "detail": "Sede no encontrada"
  }
  ```

---

## Instalación y arranque

1. Clona el repositorio y ve a su carpeta raíz:

   ```bash
   git clone <url_del_repositorio>
   cd SGA-IE-JSMMC-GESTION-ACADEMICA-SEDES-SERVICIO
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   . .venv/Scripts/activate       # Windows
   source .venv/bin/activate      # macOS / Linux
   ```

3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea el archivo `.env` en la raíz (no lo subas a Git) con estas variables:

   ```env
   DATABASE_URL="mysql+pymysql://root:TU_CONTRASEÑA@127.0.0.1:3306/sedes_db"
   SECRET_KEY="valor_aleatorio_32_caracteres_o_más"
   DEBUG=True
   CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
   HOST="127.0.0.1"
   PORT=8000
   ```

   > **Importante:** Genera tu `SECRET_KEY` con:
   >
   > ```bash
   > python - <<'EOF'
   > import secrets; print(secrets.token_urlsafe(32))
   > EOF
   > ```

5. Inicializa la base de datos (requiere MySQL Workbench o CLI):

   ```sql
   SOURCE scripts/init_db.sql;
   ```

   (Opcional) Poblar datos de ejemplo:

   ```sql
   SOURCE scripts/seed_sedes.sql;
   ```

6. Arranca la aplicación:

   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

   o bien:

   ```bash
   python -m app.main
   ```

---

## Pruebas

Ejecuta las pruebas unitarias con pytest:

```bash
pytest app/test/test_sedes.py
```

---

## Documentación interactiva

* **Swagger UI:**  `http://127.0.0.1:8000/docs`
* **ReDoc:**         `http://127.0.0.1:8000/redoc`

---

## Dependencias principales

* **FastAPI**: Framework web
* **SQLAlchemy**: ORM
* **Pydantic**: Validación de datos
* **Pytest**: Pruebas unitarias
* **python-jose**: JWT y criptografía (si se extiende en el futuro)

---



```
```

````markdown
## 🛠️ Configuración del entorno

Antes de ejecutar la API, crea tu archivo de variables de entorno a partir del ejemplo:

```bash
cp .env.example .env
````

Abre `.env` y sustituye los placeholders por tus datos reales:

```ini
DATABASE_URL="mysql+pymysql://USER:PASSWORD@HOST:PORT/sedes_db"
SECRET_KEY="TU_SECRET_KEY"
DEBUG=True
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
HOST="127.0.0.1"
PORT=8001
AUTH_API_URL="http://localhost:8000"
```

**Descripción de variables**

* `DATABASE_URL`: cadena de conexión a MySQL (usuario, contraseña, host, puerto, nombre de la BD).
* `SECRET_KEY`: clave secreta para la aplicación.
* `DEBUG`: `True` para modo desarrollo (muestra SQL en consola).
* `CORS_ORIGINS`: orígenes permitidos para CORS.
* `HOST` y `PORT`: dirección y puerto donde correrá la API de sedes.
* `AUTH_API_URL`: URL base de tu servicio de autenticación (por defecto `http://localhost:8000`).

---

## ▶️ Ejecutar la API en local

1. Activa tu entorno virtual y asegúrate de tener las dependencias instaladas:

   ```bash
   source .venv/bin/activate      # UNIX/macOS
   . .\.venv\Scripts\Activate.ps1 # Windows PowerShell
   pip install -r requirements.txt
   ```

2. Inicia la aplicación:

   ```bash
   uvicorn app.main:app --reload --host ${HOST} --port ${PORT}
   ```

3. Accede a la documentación interactiva en tu navegador:

   ```
   http://127.0.0.1:8001/docs
   ```

```
```

