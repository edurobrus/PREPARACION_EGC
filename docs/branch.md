# EVOLUCIÓN Y GESTIÓN DE LA CONFIGURACIÓN (24/25)
## P3: GESTIÓN DEL CÓDIGO FUENTE (USUARIO B)

### EJERCICIO 1: QUE TE INVITE EL COMPAÑERO/A (en pareja)
1.1) Para aceptar la invitación, en tu dashboard de GitHub, justo en el icono a la izquierda de tu foto, pon "You have unread notifications". Acepta la invitación.

1.2) Haz clone del proyecto de tu compañero/a en tu equipo.
```bash
git clone <url-del-repositorio>
```

1.3) Comprueba que se ha clonado con el método SSH.
```bash
git remote -v
```

---

### EJERCICIO 2: TRABAJANDO CON RAMAS (en pareja)
2.1) Crea una issue de nombre “Testing file (B)” con la descripción que quieras. Debes añadir el nombre de usuario de tu compañero/a A en “Assignees” en la parte de la derecha.

2.2) Crea una rama local de nombre “feature/practicandogit_b” y sitúate en ella.
```bash
git checkout -b feature/practicandogit_b
```

2.3) Comprueba que estás situado en esa rama.
```bash
git branch
```

2.4) Súbela al repositorio remoto.
```bash
git push origin feature/practicandogit_b
```

2.5) Crea, en la raíz del proyecto, un archivo llamado “practicandogit.txt_b” que contenga una sola línea con tu uvus.
```bash
echo "tu_uvus" > practicandogit.txt_b
```

2.6) Comprueba que ese archivo lo está rastreando git.
```bash
git status
```

2.7) Añade ese archivo en concreto al área de preparación (stage).
```bash
git add practicandogit.txt_b
```

2.8) Comprueba que ese archivo lo está rastreando git y ya está en el área de preparación.
```bash
git status
```

2.9) Crea un commit de nombre “feat: Añade archivo de prueba” pero no lo subas aún al repositorio remoto.
```bash
git commit -m "feat: Añade archivo de prueba"
```

2.10) Cambia el título del commit por “feat: Add testing file” y cierra la issue de tu compañero “Testing file (A)” mediante su ID.
```bash
git commit --amend -m "feat: Add testing file"
```

2.11) Sube el nuevo commit a tu rama remota.
```bash
git push --force
```

---

### EJERCICIO 3: PULL REQUEST (en pareja)
3.1) Ve a la pestaña Pull requests -> New pull request. Asegúrate, a la hora de comparar, que en “base” aparece “main” y que en “compare” aparece “feature/practicandogit_b”.

3.2) Crea una pull request e invita al compañero A a que la revise. Debes añadir su nombre de usuario en “Assignees” en la parte de la derecha.

3.3) En la pestaña Pull requests debería haber una petición de cambio pendiente que tiene que ser aceptada por nosotros. Acéptala con Merge pull request -> Confirm merge.

---

### EJERCICIO 4: CONFLICTOS (en pareja)
4.1) Sitúate en la rama principal.
```bash
git checkout main
```

4.2) Actualiza todos los cambios del repositorio remoto en tu repositorio local.
```bash
git pull origin main
```

4.3) Trae la rama “feature/practicandogit_a” a tu repositorio local.
```bash
git fetch origin feature/practicandogit_a
git checkout feature/practicandogit_a
```

4.4) Actualiza los posibles cambios de esa rama.
```bash
git pull origin feature/practicandogit_a
```

4.5) Modifica la primera y única línea del archivo “practicandogit_a.txt” con “esta es una nueva línea remota”.
```bash
echo "esta es una nueva línea remota" > practicandogit_a.txt
```

4.6) Sube los cambios a la rama remota “feature/practicandogit_a” con el mensaje de commit “fix: Change testing file”.
```bash
git add practicandogit_a.txt
git commit -m "fix: Change testing file"
git push origin feature/practicandogit_a
```

4.7) Sitúate en tu rama “feature/practicandogit_b”.
```bash
git checkout feature/practicandogit_b
```

4.8) Modifica la primera y única línea del archivo “practicandogit_b.txt” con “esta es una nueva linea local”.
```bash
echo "esta es una nueva linea local" > practicandogit_b.txt
```

4.9) Añádelo al área de stage y commitéalo, pero no lo subas aún al remoto.
```bash
git add practicandogit_b.txt
git commit -m "feat: Whatever"
```

4.10) Actualiza tu rama local.
```bash
git pull origin feature/practicandogit_b --no-rebase
```

4.11) ¡Hay un conflicto! Resuelve el conflicto eligiendo el cambio correcto y realiza el commit.
```bash
# Abre el archivo con el conflicto, elige la versión correcta y guarda los cambios.
git add practicandogit_b.txt
git commit -m "fix: Fix conflicts"
git push origin feature/practicandogit_b
```

---

### EJERCICIO 5: CHERRY-PICKING (en pareja)
5.1) Sitúate en la rama “feature/practicandogit_b”.
```bash
git checkout feature/practicandogit_b
```

5.2) Crea el archivo “fix_bug_b.py” con el contenido que quieras.
```bash
echo "contenido del archivo" > fix_bug_b.py
```

5.3) Realiza el commit “fix: Fix important bug (developer B)”.
```bash
git add fix_bug_b.py
git commit -m "fix: Fix important bug (developer B)"
```

5.4) Actualiza los cambios remotos y obtén el hash del commit de tu compañero, es decir, “fix: Fix important bug (developer A)”.
```bash
git fetch origin
git log --oneline
```

5.5) Tráete ese commit a tu rama.
```bash
git cherry-pick <commit-hash-de-tu-compañero>
```

5.6) Sube los cambios.
```bash
git push origin feature/practicandogit_b
```

---

### EJERCICIO 6: STASHING (individual)
6.1) Asegúrate que estás en la rama “feature/practicandogit_b”.
```bash
git checkout feature/practicandogit_b
```

6.2) Crea, en la raíz, un archivo de nombre “estoestasinterminar.txt” con el contenido que quieras.
```bash
echo "blablabla" > estoestasinterminar.txt
```

6.3) Usa la pila stash para guardar los cambios.
```bash
git stash
```

6.4) Cambia a la rama “main”.
```bash
git checkout main
```

6.5) Muestra el contenido de la pila stash.
```bash
git stash list
```

6.6) Aplica el stash guardado sin eliminarlo de la pila.
```bash
git stash apply
```

6.7) El último stash sigue en la pila. Borra el stash.
```bash
git stash drop
```

---

### EJERCICIO 7: REVIRTIENDO CAMBIOS (individual)
7.1) Localiza el hash correspondiente al commit “fix: Fix missing MariaDB port in Docker entrypoints”.
```bash
git log --oneline
```

7.2) Haz un reset de la rama manteniendo los cambios en el área de trabajo.
```bash
git reset --soft <commit-hash>
```

7.3) Elimina los cambios del stage.
```bash
git reset
```

7.4) Actualiza la rama remota.
```bash
git pull origin feature/practicandogit_b
```

7.5) Haz un push forzado para eliminar los commits adicionales del repositorio remoto.
```bash
git push --force
```

7.6) Deshaz los cambios del commit “fix: Change Vagrant box to jammy64”.
```bash
git revert <commit-hash>
```

7.7) Compara el commit de HEAD con ese commit.
```bash
git diff HEAD <commit-hash>
```

---

### EJERCICIO 8: HOOKS (individual)
8.1) Crea en tu rama “feature/practicandogit_b”, en .git/hooks/, un archivo “commit-msg”.
```bash
touch .git/hooks/commit-msg
```

8.2) Añade el siguiente script al archivo commit-msg:
```bash
#!/bin/bash
mensaje_commit=$(cat "$1")
if ! [[ "$mensaje_commit" =~ ^(feat|fix|chore): ]]; then
  echo "ERROR: El mensaje del commit debe comenzar con uno de los siguientes prefijos: feat:, fix:, chore:"
  exit 1
fi
```

8.3) En la raíz, crea un archivo “testing_hook.txt” con el contenido que quieras.
```bash
echo "contenido de prueba" > testing_hook.txt
```

8.4) Crea un commit con el mensaje “Esto es un mensaje inválido”.
```bash
git add testing_hook.txt
git commit -m "Esto es un mensaje inválido"
```

8.5) Cambia el mensaje a uno válido y haz el commit.
```bash
git commit --amend -m "feat: Esto sí un mensaje válido"
```