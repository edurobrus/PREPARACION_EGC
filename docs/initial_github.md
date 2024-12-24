# Comandos para instalar GitHub Desktop

1. Primero, ve a la siguiente URL y descarga el primer archivo `.deb` que veas:

   [https://github.com/shiftkey/desktop/releases](https://github.com/shiftkey/desktop/releases)

2. Me metí en este enlace para que se me descargara el archivo `.deb` directamente:

   [Descargar GitHub Desktop .deb](https://github.com/shiftkey/desktop/releases/download/release-3.4.8-linux1/GitHubDesktop-linux-amd64-3.4.8-linux1.deb)

3. Después de la descarga, abre la terminal y navega a la carpeta donde descargaste el archivo.

4. Ejecuta los siguientes comandos:

   ```bash
   sudo dpkg -i GitHubDesktop-linux-amd64-3.4.8-linux1.deb
   ```

5. Si hay problemas con dependencias faltantes, ejecuta el siguiente comando para corregirlas:

   ```bash
   sudo apt-get install -f
   ```

# Ejercicio práctico: Configurar GitHub y forkear

### 1. Instalar Git

Si no tienes Git instalado, puedes instalarlo con el siguiente comando:

```bash
sudo apt install git
```

### 2. Configurar Git

A continuación, configura tu nombre y correo en Git. Esto es importante porque se asociará con los commits que realices:

```bash
git config --global user.name "Eduardo Robles Russo"
git config --global user.email eduroblesrusso82@gmail.com
```

### 3. Generar una clave SSH

Para autenticarte de manera segura con GitHub, es recomendable usar una clave SSH. Genera una nueva clave SSH con el siguiente comando:

```bash
ssh-keygen -t rsa -b 4096
```

Sigue las instrucciones para completar la creación de la clave SSH.


### 4. Visualizar la clave pública y copiarla

Para visualizar la clave pública que acabas de generar y copiarla, utiliza estos comandos:

1. Navega al directorio donde se almacenan las claves SSH:

   ```bash
   cd ~/.ssh
   ```

2. Visualiza la clave pública con el comando `cat`:

   ```bash
   cat id_rsa.pub
   ```

   Esto imprimirá tu clave pública en la terminal.


### 5. Agregar la clave SSH a GitHub

1. Copia la clave pública (todo el contenido que aparece cuando ejecutas `cat id_rsa.pub`).

2. Ve a tu cuenta de GitHub y accede a **Settings**.

3. En el menú lateral, selecciona **SSH and GPG keys**.

4. Haz clic en **New SSH key**.

5. En el campo **Title**, asigna un nombre a tu clave (por ejemplo, "Mi clave SSH").

6. En el campo **Key**, pega la clave pública que copiaste (desde `id_rsa.pub`).

7. Haz clic en **Add SSH key** para completar el proceso.


# Trabajar con GitHub (Clonar un repositorio y realizar cambios)

### 1. Clonar el repositorio con SSH

Para clonar un repositorio usando SSH, utiliza el siguiente comando (sustituye `url_ssh` con la URL del repositorio que deseas clonar):

```bash
git clone git@github.com:edurobrus/PREPARACION_EGC.git
```

### 2. Inicializar un repositorio local

Si no has clonado un repositorio, puedes inicializar un nuevo repositorio en tu directorio de trabajo:

```bash
git init
```

### 3. Añadir archivos al repositorio

Para añadir los archivos del directorio actual al repositorio:

```bash
git add .
```

### 4. Hacer un commit

Realiza un commit con un mensaje que describa los cambios realizados:

```bash
git commit -m "Add content"
```

### 5. Cambiar a la rama principal (main)

Si aún no tienes una rama principal llamada `main`, puedes renombrar la rama actual a `main`:

```bash
git branch -M main
```

### 6. Agregar el repositorio remoto

Agrega el repositorio remoto (si aún no lo has hecho) para poder subir tus cambios. Asegúrate de usar la URL SSH correcta:

```bash
git remote add origin git@github.com:edurobrus/PREPARACION_EGC.git
```

### 7. Subir los cambios al repositorio remoto

Sube los cambios de la rama `main` al repositorio remoto en GitHub:

```bash
git push -u origin main
```

Con estos pasos, habrás configurado tu entorno de trabajo en Git, creado y añadido tu clave SSH a GitHub, y podrás clonar, modificar y subir repositorios con Git.
