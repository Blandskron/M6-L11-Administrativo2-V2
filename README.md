# **Library Project**

Este proyecto es una aplicación de Django diseñada para gestionar información sobre libros, géneros, autores y copias de libros (instancias). Incluye un sistema administrativo funcional, registro de modelos, gestión de usuarios y restricciones de acceso.

---

## **Características del Proyecto**

1. **Gestión de Libros y Autores**:
   - CRUD completo (Crear, Leer, Actualizar y Eliminar) para libros, autores, géneros y copias de libros.
   - Personalización del sitio administrativo con vistas detalladas.

2. **Sistema de Usuarios**:
   - Gestión de usuarios y grupos mediante el sitio administrativo.
   - Creación de un usuario de prueba con permisos limitados.

3. **Restricción de Acceso**:
   - Acceso protegido a ciertas vistas para usuarios autenticados.

4. **Modelos Avanzados**:
   - Implementación del método `get_absolute_url` para facilitar la navegación entre objetos.

---

## **Requisitos Previos**

- Python 3.8 o superior.
- Django 4.0 o superior.
- SQLite (configuración por defecto para bases de datos).

---

## **Instrucciones de Instalación**

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/library-project.git
   cd library-project
   ```

2. **Crear un entorno virtual e instalar dependencias**:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos**:
   Realizar las migraciones para generar las tablas:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Crear un superusuario**:
   Ejecuta el siguiente comando para crear un administrador:
   ```bash
   python manage.py createsuperuser
   ```

5. **Iniciar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

6. **Acceder al sitio administrativo**:
   - URL: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Inicia sesión con las credenciales del superusuario.

---

## **Instrucciones de Uso**

### **1. Sitio Administrativo**
Desde el sitio administrativo, puedes:
- Agregar, editar y eliminar libros, autores, géneros e instancias.
- Gestionar usuarios y permisos.

### **2. Crear un Usuario de Prueba**
Para crear un usuario de prueba con permisos limitados, sigue estos pasos:
1. Abre la consola interactiva:
   ```bash
   python manage.py shell
   ```
2. Ejecuta el script para crear un usuario:
   ```python
   from catalog.utils import create_test_user
   create_test_user()
   ```
   Esto crea un usuario con las siguientes credenciales:
   - Usuario: `testuser`
   - Contraseña: `testpassword`

### **3. Acceso a Vistas Protegidas**
El proyecto incluye una vista protegida que solo es accesible para usuarios autenticados:
- URL: [http://127.0.0.1:8000/catalog/protected](http://127.0.0.1:8000/catalog/protected)

---

## **Estructura del Proyecto**

```
library_project/
├── catalog/
│   ├── migrations/
│   ├── templates/
│   │   └── protected_page.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── library_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

---

## **Funciones Implementadas**

### **Modelos**
- **Author**: Representa un autor con nombre, apellido y fecha de nacimiento.
- **Genre**: Representa géneros literarios.
- **Book**: Representa un libro, asociado con autores y géneros.
- **BookInstance**: Representa copias físicas de un libro.

### **Sistema Administrativo**
- Todos los modelos están registrados en el sitio administrativo.
- Personalización de vistas con búsqueda y filtros.

### **Restricción de Acceso**
- Vistas protegidas que redirigen a usuarios no autenticados.

---

## **Pruebas y Depuración**

1. Verifica que los modelos aparecen correctamente en el sitio administrativo.
2. Prueba el acceso a la vista protegida con usuarios autenticados y no autenticados.
3. Crea usuarios y asigna permisos para validar la gestión de roles.

---

## **Notas Importantes**

- El proyecto usa SQLite por defecto. Para entornos de producción, se recomienda cambiar a PostgreSQL o MySQL.
- Implementa medidas de seguridad adicionales como HTTPS y autenticación de dos factores (2FA) si es necesario.

---

## **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas colaborar:
1. Haz un fork del repositorio.
2. Crea una rama nueva para tus cambios.
3. Envía un pull request con una descripción detallada.

---
