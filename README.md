# 
# PetApp

red social creada con Flask. Los usuarios pueden publicar comentarios, cargar imágenes, dar me gusta a las publicaciones y comentar las publicaciones.

## Instalación

Antes de comenzar, asegúrese de tener Python y pip instalados en su sistema. Si no los tiene instalados, puede descargar Python [aquí] (https://www.python.org/downloads/) y pip se instalará con Python.

1. Clone este repositorio en su máquina local:

     ```
     git clone https://github.com/sstechdev/PetApp
     ```

2. Navegue al directorio del proyecto:

     ```
     cd PetApp
     ```

3. Instale los paquetes necesarios:

     ```
     pip install flask
     ```

## Ejecutar la aplicación

1. Configure la variable de entorno de la aplicación Flask:

     - En Windows:

         ```
         set FLASK_APP=main.py
         ```

     - En Unix o MacOS:

         ```
         export FLASK_APP=main.py
         ```

2. Ejecute la aplicación Flask:

     ```
     flask run
     ```

3. Abra su navegador web y vaya a `http://127.0.0.1:5000/`.

## Uso

1. Ingrese su nombre de usuario para iniciar sesión.
2. Publique un comentario, cargue una imagen o haga ambas cosas.
3. Dale me gusta a las publicaciones y comenta las publicaciones.
4. La primera publicación se fija en la parte superior de la fuente.

¡Disfruta usando la aplicación!
