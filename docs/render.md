## Tabla de Contenidos
1. [Parte Uno: Implementación de la Base de Datos en Filess.io](#parte-uno-implementación-de-la-base-de-datos-en-filessio)
2. [Parte Dos: Implementación de la Aplicación en Render](#parte-dos-implementación-de-la-aplicación-en-render)
   - [Iniciar sesión en Render](#iniciar-sesión-en-render)
   - [Crear una Instancia de la Aplicación](#crear-una-instancia-de-la-aplicación)
     - [Configuración Básica](#configuración-básica)
     - [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno)
   - [Verificar el Proceso de Implementación](#verificar-el-proceso-de-implementación)

---

## Parte Uno: Implementación de la Base de Datos en Filess.io

### Base de Datos Externa
Render solo tiene soporte nativo para PostgreSQL. Para MariaDB, utilizaremos el servicio de Filess.io como alojamiento.

### Pasos:
1. Ingresa a [Filess.io](https://filess.io) y crea una cuenta.
2. Haz clic en **+ New Database** (Nueva Base de Datos).
3. En **Database identifier** (Identificador de la Base de Datos), ingresa `uvlhubdatabase`.
4. En **Database engine** (Motor de Base de Datos), selecciona **MariaDB**.

Luego, serás redirigido al panel principal de gestión de tu base de datos en la nube. Guarda las credenciales que te proporcionen, ya que las necesitarás más adelante.

---

## Parte Dos: Implementación de la Aplicación en Render

### Iniciar sesión en Render
1. Ve a [Render](https://render.com).
2. Haz clic en **Sign in** (Iniciar Sesión). Es recomendable usar tu cuenta de GitHub para facilitar la vinculación del repositorio.

---

### Crear una Instancia de la Aplicación

#### Configuración Básica
1. En el menú superior, haz clic en **[Dashboard](https://dashboard.render.com/) -> New -> Web Service** (Tablero -> Nuevo -> Servicio Web) si ya esta creado usa el de uvlhub_practicas.
2. En **Git Provider**, pega la URL del repositorio Git que deseas implementar.  
   - Si el repositorio no aparece listado, haz clic en **Credentials -> Configure GitHub** (Credenciales -> Configurar GitHub), selecciona tu usuario de GitHub y otorga permisos con **Install**.
3. Haz clic en **Connect** (Conectar).
4. En **Name** (Nombre), asigna el nombre `uvlhub_<uvus>` (por ejemplo, `uvlhub_drorganvidez` para el UVUS `drorganvidez`).
5. En **Project** (Proyecto), crea un nuevo proyecto llamado `uvlhub` (opcional).
6. Selecciona **Docker** como el sistema de implementación en **Language** (Lenguaje).
7. En **Region**, selecciona **Frankfurt (central EU)**.
8. En **Branch** (Rama), selecciona `main` (predeterminado).
9. En **Dockerfile Path** (Ruta del Dockerfile), ingresa `docker/images/Dockerfile.render`.
10. Elige **Free** (Gratis) como tipo de instancia en **Instance Type**.

#### Configuración de Variables de Entorno
1. En **Environment Variables** (Variables de Entorno), haz clic en **Add from .env** (Agregar desde .env) y pega lo siguiente:

    ```bash
    FLASK_APP_NAME="UVLHUB.IO"
    FLASK_ENV=production
    FLASK_APP=app
    SECRET_KEY=dev_test_key_1234567890abcdefghijklmnopqrstu
    DOMAIN=uvlhub-<uvus>.onrender.com
    MARIADB_HOSTNAME=<CAMBIAR_ESTO>
    MARIADB_DATABASE=<CAMBIAR_ESTO>
    MARIADB_USER=<CAMBIAR_ESTO>
    MARIADB_PORT=<CAMBIAR_ESTO>
    MARIADB_PASSWORD=<CAMBIAR_ESTO>
    MARIADB_ROOT_PASSWORD=<MISMA_CONTRASEÑA_DE_MARIADB_PASSWORD>
    WORKING_DIR=/app/
    ```

2. Reemplaza:
   - `<CAMBIAR_ESTO>` con las credenciales de la base de datos proporcionadas por Filess.io.
   - `<uvus>` con tu UVUS (identificador universitario).

3. Haz clic en **Deploy** (Implementar).

**Nota:**
- Agrega manualmente cualquier variable de entorno adicional que requieran tus módulos.
- El CLI de Rosemary o el comando `rosemary compose:env` no están disponibles en entornos de producción.

---

### Verificar el Proceso de Implementación

1. Observa los registros (logs) de implementación para detectar errores.
2. Una vez implementada, tu aplicación estará disponible en:
   ```
   https://uvlhub-<uvus>.onrender.com
   ```
3. El proceso de implementación puede tardar hasta 5 minutos.

**¡Felicidades!** Tu aplicación ha sido implementada y está lista para usar.