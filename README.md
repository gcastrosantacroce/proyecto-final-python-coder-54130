# PROYECTO FINAL CoderHouse Python 54310
### Alumno Castro Santacroce Gonzalo

# Comandos

1. Crear proyecto Django
    ```bash
    django-admin startproject <nombre del proyecto que quieran ustedes>
    ```
    ```bash
    # Otras variantes del comando si falla:
    python -m django startproject nombre_del_proyecto
    # Y si usan python3 como comando:
    python3 -m django startproject nombre_del_proyecto
    ```
2. Testear servidor
    ```bash
    python manage.py runserver
    ```
3. Crear una `application` dentro de mi proyecto:
    ```bash
    python manage.py startapp <nomre de su aplicacion>
    ```
4. Creamos un archivo que se llame urls.py en <nombre_del_proyecto>/<nombre_de_su_aplicacion>/urls.py. En mi caso sería: MeetingRooms/bookings/urls.py

## Templates

1. Crear un template y guardarlo en el lugar adecuado
2. Utilizar la función `render`

## Modelos

Después de agregar o modificar un modelo en `models.py` tenemos que correr 2 comandos:

1. `python manage.py makemigrations`
2. `python manage.py migrate`


