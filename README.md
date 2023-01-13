# CRUD-con-Django-JavaScript-y-Ajax

He decidido crear este repositorio, con el objetivo de poder ayudar a las personas que se encuentran aprendiendo Django y JavaScript, a crear una aplicación CRUD con estas dos herramientas de una forma sencilla y bien explicada.

Que realizaremos dentro de este proyecto principalmente:
- Crearemos un proyecto en django, este proyecto tendra una aplicacion que se encargara de CREAR, RECUPERAR, ACTUALIZAR Y ELIMINAR registro de una base de datos, a esto se lo denomina CRUD, y con la ayuda de JavaScript procesaremos todos los datos en el  lado del cliente para luego enviarlo a traves de solicitudes HTTP a nuestro servidor para que la aplicacion lo procese, valide y en su caso realice la accion solicitada, devolviendo una respuesta. Tambien utilizaremos DataTable para mostrar nuestros datos de una forma ordenada y legible. 

Django se basa en la arquitectura  MVT (Model-View-Template), y su estructura tiene las siguitnes partes, el 'modelo' que va actuar como la interfaz de sus datos, la 'vista' que actuara como la interfaz de usuario, lo que se ve en el navegador cuando representa un sitio web y por ultimo las plantillas que consta de partes estaticas de la salida HTML, asi como su propia sintaxis que describe como se insertara el contenido dinamico.

PRIMERA PARTE: 

  1 - Comencemos creando un proyecto nuevo en django en el directorio que desea y el nombre que le parezca mas conveniente, una vez hecho esto, si estamos en mac hacemos un "ls" o en windows con "dir", para ver que nos ha creado con el comando.
      
      # django-admin startproject config .
      
      #(env) bash-3.2$ django-admin startproject config .
      #(env) bash-3.2$ ls
        config          manage.py
      
      
  2 - Una vez creado el proyecto, crea una aplicacion dentro del mismo, que sera el encargado de gestionar las funcionalidades necesarias para tu proyecto
  
      # python manage.py startapp core
      
  3 - Agregamos nuestra aplicacion al proyecto, luego probemos si todo anda bien en nustro servidor local
  
      En el archivo Settings # INSTALLED_APPS = [
              'core',
          ]
          
      _____________________________
      
      # python manage.py runserver
      
  4 - Paremos el servidor, y centremonos primeramente en el archvo models, donde definiremos la estructura de los datos que almacenaremos en nuestra base de datos (por cierto, utilizaremos la base de datos predeterminada de django). Obs: este proyecto es a efecto educativo y por lo tanto decidi hacerlo con un solo campo, el cual es el nombre de la categoria, sobre este campo es lo que aplicare el CRUD, es decir Creare categorias, Recuperare esas categorias, Actualizare esas categoria y finalmente lo eliminare. Creo conveniente esto en razon de que el las operaciones realizas sobre este campo, practicamente seran las mismas para todos los demas, salvo ciertas excepciones, y para no trabjar con demasiados campos que lo unico que logra muchas veces al momento de estudiar es complicar las cosas. 
  
      from django.db import models


      class Category(models.Model):
          name = models.CharField(max_length=200, verbose_name='name', unique=True)

          def __str__(self) -> str:
              return self.name

  4.1 - models: es una clase que esta incorporada en django y que utiliza  para crear, recuperar, actualizar y eliminar datos de la base de datos.
  4.2 - primeramente lo que hacemos es importarlo en nustro archivo models.py
  4.3 - Luego creamos una clase Category, que se implementa como una subclase de models.Model, y que puede incluir compos, metodos y metadatos. 
  4.4 - Pasamos a definir posteriormente nuestro campo "name", el cual representara una columna dentro de nuestra tabla en la base de datos. Nuestro unico campo es de tipo models.CharField (lo que significa que contendra una cadena de texto, "caracteres alfanumericos")
  4.5 - A nuestro campo "name", le pusimos tres agrumentos, los cuales especifican a demas del tipo, como se guarda o como se puede usar.
  4.6 - max_length, el cual establece la longitud maxima de caracteres que podemos ingresar dentro de ese campo, en nuestro caso lo pusimos en 200.
  4.7 - verbose_name, es la etiqueta que le especificamos. 
  4.8 -  unique, como tercer argumento con el estado true, esto indica que el campo debe ser unico en toda la tabla. En el caso que ingresemos un valor duplicado en un unique=true, este al intentar guardar en la base de datos nos arrojaria un error, que lo veremos mas adelante.
  4.9 - por ultimo respecto a los modelos, escribimos un metodo __str__(self), que indica como mostrar el objeto representado en un "string", es decir si no lo implementamos al momento de instanciar el objeto y devolver el mismo la representacion del mismo seria <__main__.Category object at 0x0000020B0787CA20>, en cambio si lo implementamos, como en este caso, nos devolveria el nombre que ingresamos en el campo. Ejemplo "Django" en vez de lo anterior.
  

SEGUNDA PARTE: Una vez creado nuestro modelo, necesitamos ejecutar dos comandos necesarios el "makemigrations" y el "migrate".

    # python manage.py makemigrations
    
    # python manage.py migrate
 
 El makemigrations es el encargado de generar los comandos SQL para la aplicacion preinstalada, mientras que el migrate, ejecuta esos comandos SQL en el archivo de la base de datos en nuestro caso el archivo predeterminado ubicado en la raiz de nuestro proyecto. Una vez ejecutado ambos comandos, en ese orden, se habra creado una nueva tabla en la base de datos. Puedes comprabar yendo a tu proyecto > app > makemigrations -> 0001_initial.py. -
 
TERCERA PARTE: Vamos a renderizar nuestro modelo en el administrador predeterminado de Django, para ello vayamos a app/admin.py y coloquemos el siguiente codigo.
 
  from django.contrib import admin
  from .models import Category
   
  admin.site.register(Category)
  

Esto nos permitira interactuar con nuestro modelo de la base de datos, es decir, crear, recuperar, actualizar y eliminar datos del mismo. Para ello creemos un password para poder acceder al panel de administracion de Django. 

Aclaro que solo utilizaremos el administrador de Django, a manera de vizualizar que nuestro modelo ha sido agregado correctamente, y en el que podemos realizar ciertas acciones para comprobarlo. 

Este proyecto, nuestro objetivo es poder perzonalizar un panel de administrador a nuestro gusto. -

CUARTA PARTE: Una vez definido nuestro modelo y probado su funcionamiento, nos enfocaremos en los "Views" o "Vistas", el cual es uno de las principales partes de nuestra estructura MVT (models-views-templates).

A continuacion crearemos y usaremos nuestra vista, considerando nuestro proyecto que contiene nuestra aplicacion blog en mi caso, nos vamos dentro de la aplicacion en el archivo miAplicacion/views.py

Antes que nada desearia hacer un sintesis de lo que es la vista, a fin de tener una comprension mas acabada del mismo, segun la documentacion oficial de django es una funcion de python que toma solicitudes web y devuelve una respuesta web, practicamente puede devolver cualquier cosa (XML, imagen, error 404 etc) y el codigo que lo contiene pude estar ubicado en cualquier parte, pero lo recomendado es hacerlo en un archivo views.py. 
 

Vayamos a nuestro archivo views.py, en nuestro caso, a fin de ordenar las vistas lo creamos dentro de una carpeta llamada adminviews/views.py, en el mismo primeramente realizamos una funcion que toma como primer parametro un objeto HttpRequest y dicha funcion dev

 
  




