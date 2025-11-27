# Pet Adoption API
API REST construida con Django y Django REST Framework para gestionar un sistema de adopción de mascotas. Incluye usuarios, refugios, mascotas, solicitudes de adopción y seguimiento de adopciones.

## Características

- Autenticación JWT (registro, login, refresh)
- Roles: cliente y administrador
- Endpoints para administrar:
  - Usuarios (admin)
  - Refugios
  - Mascotas
  - Solicitudes de adopción
  - Seguimiento de adopciones
- Clientes pueden registrarse, crear solicitudes y ver mascotas disponibles
- Administradores pueden gestionar todo el sistema

## Requisitos

- Python 3.10+ recomendado
- PostgreSQL
- Virtualenv

## Instalación

1. Clonar el repositorio
git clone https://github.com/KevC17/pet_adoption
cd pet_adoption

2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate

3. Instalar dependencias
pip install -r requirements.txt

4. Crear archivo `.env`.
    - SECRET_KEY=super-secret-key
    - DEBUG=True
    - ALLOWED_HOSTS=*
    - DB_NAME=petadoptiondb
    - DB_USER=postgres
    - DB_PASS=admins
    - DB_HOST=localhost
    - DB_PORT=5432

5. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

6. Crear superusuario
python manage.py createsuperuser

7. Ejecutar servidor
python manage.py runserver

La API estará disponible en: http://localhost:8000/api/ o http://127.0.0.1:8000/api/

## Autenticación Usuarios normales

Registro
POST /api/auth/register/

{
  "username": "juan",
  "email": "juan@example.com",
  "password": "password123"
}

Login
POST /api/auth/login/

{
  "username": "juan",
  "password": "password123"
}

Respuesta
{
  "refresh": "refresh_token",
  "access": "access_token"
}

Refresh
POST /api/auth/refresh/

{
  "refresh": "refresh_token"
}

Respuesta
{
  "access": "access_token"
}

## Creación de variable de entorno para postman

 - base_url: http://localhost:8000 o http://127.0.0.1:8000
 - token: access_token (Obtenido anteriormente)

Crear usuario (admin)

POST /api/admin/users/
Authorization: Bearer {{token}}
{
  "username": "empleado1",
  "email": "empleado1@example.com",
  "first_name": "Juan",
  "last_name": "Perez",
  "is_active": true,
  "is_staff": true,
  "password": "admin12345"
}


## Listado de endpoints

Autenticación

 - POST /api/auth/register/

 - POST /api/auth/login/

 - POST /api/auth/refresh/

Usuarios (admin)

 - GET /api/admin/users/

 - POST /api/admin/users/

 - GET /api/admin/users/{id}/

 - PUT /api/admin/users/{id}/

 - PATCH /api/admin/users/{id}/

 - DELETE /api/admin/users/{id}/

Refugios

 - GET /api/shelters/

 - POST /api/shelters/

 - GET /api/shelters/{id}/

 - PUT /api/shelters/{id}/

 - PATCH /api/shelters/{id}/

 - DELETE /api/shelters/{id}/

Mascotas

 - GET /api/pets/

 - POST /api/pets/

 - GET /api/pets/{id}/

 - PUT /api/pets/{id}/

 - PATCH /api/pets/{id}/

 - DELETE /api/pets/{id}/

Solicitudes de adopción (cliente)

 - GET /api/adoption-requests/

 - POST /api/adoption-requests/

 - GET /api/adoption-requests/{id}/

Seguimiento de adopciones (admin)

 - GET /api/adoption-tracking/

 - POST /api/adoption-tracking/

 - GET /api/adoption-tracking/{id}/

 - PUT /api/adoption-tracking/{id}/

 - PATCH /api/adoption-tracking/{id}/

 - DELETE /api/adoption-tracking/{id}/