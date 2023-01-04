# CRUD-con-Django-JavaScript-y-Ajax

He decidido crear este repositorio, con el objetivo de poder ayudar a las personas que se encuentran aprendiendo Django y JavaScript, a crear una aplicación CRUD con estas dos herramientas de una forma sencilla y bien explicada.

Que realizaremos dentro de este proyecto principalmente:
- Crearemos un proyecto en django, este proyecto tendra una aplicacion que se encargara de CREAR, RECUPERAR, ACTUALIZAR Y ELIMINAR registro de una base de datos, a esto se lo denomina CRUD, y con la ayuda de JavaScript procesaremos todos los datos del lado del cliente para luego enviarlo a traves de solicitudes HTTP a nuestro servidor para que la aplicacion lo procese, valide y en su caso realice la accion solicitada, devolviendo una respuesta. Tambien utilizaremos DataTable para mostrar nuestros datos de una forma ordenada y legible. 


  1 - Comencemos creando un proyecto nuevo en django en el directorio que desea y el nombre que le parezca mas conveniente.
      
      # django-admin startproject nombre_proyecto
      
      
  2 - Una vez creado el proyecto, crea una aplicacion dentro del mismo, que sera el encargado de gestionar las funcionalidades necesarias para tu proyecto
  
      # python manage.py startapp core
      
  3 - Agregamos nuestra aplicacion al proyecto, luego probemos si todo anda bien en nustro servidor local
  
      Settings # INSTALLED_APPS = [
              'app',
          ]
          
      _____________________________
      
      # python manage.py runserver
      
  4 - 



