# GitHub User Activity 

## Descripción 

Este es un script simple que permite conocer la actividad reciente de un usuario en GitHub, utilizando la [GitHub API](https://docs.github.com/en/rest). 
El script consulta eventos como commits, comentarios, creación de issues, pull requests, y más, y los muestra en la consola.

## uso
1. clona este repositorio
```
git clone https://github.com/davidG199/github-user-activity.git
```
2. entra a la carpeta del proyecto
```
cd github-user-activity
```
3. Crea un entorno virtual y lo activas
```
py -m venv .venv
.venv\Scripts\activate
```
4.  instala dependencias
```
pip install -r requirements.txt
```
5. Ejecuta el script
```
python main.py
```
6. Ingresa el nombre de usuario de github

## ejemplo de salida 
```
--BIENVENIDO--
Ingresa el nombre del usuario
usuario
--pushed 3 commits to usuario/Hello-World
--created issue 1347
--comentario en 1347
--starred usuario/Hello-world
```

👌
  


