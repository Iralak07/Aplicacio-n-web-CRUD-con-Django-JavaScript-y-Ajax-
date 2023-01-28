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

En este proyecto, nuestro objetivo es poder perzonalizar un panel de administrador a nuestro gusto y necesidades, utilizando varias herramientas.

CUARTA PARTE: Una vez definido nuestro modelo y probado su funcionamiento, nos enfocaremos en los "Views" o "Vistas", el cual es uno de las principales partes de nuestra estructura MVT (models-views-templates).

A continuacion crearemos y usaremos nuestra vista, considerando nuestro proyecto que contiene nuestra aplicacion blog en mi caso, nos vamos dentro de la aplicacion en el archivo core/views.py

Antes que nada desearia hacer un sintesis de lo que es la vista, a fin de tener una comprension mas acabada del mismo, segun la documentacion oficial de django es una funcion de python que toma solicitudes web y devuelve una respuesta web, practicamente puede devolver cualquier cosa (XML, imagen, error 404 etc) y el codigo que lo contiene pude estar ubicado en cualquier parte, pero lo recomendado es hacerlo en un archivo views.py. 
 
En nuestro archivo views.py escribimos el siguiente codigo:

  from django.shortcuts import render
  from .models import Category


  def listCategory(request):
      cat = Category.objects.all()
      return render(request, 'listCategory.html', {'cat':cat})
      
Importamos "render" desde django.shortcuts, este se encarga de renderizar nuestra aplicacion a una plantilla html, para ello necesita necesariamente que se le pase tres argumentos que debe retornar nuestra funcion, 1-) reuqest: El objeto de solicitud utilizado para generar esta respuesta. 2-) template_name: El nombre completo de una plantilla para usar. 3-) Un diccionario de valores para agregar al contexto de la plantilla. Por defecto, este es un diccionario vacío. Si un valor en el diccionario es invocable, el view lo llamará justo antes de renderizar la plantilla, en nuestro caso estamos devolviendo los nombres de categoria existentes en nuestra base de datos.

Es aqui, donde debemos crear una carpeta dentro de nuestra aplicacion a fin de colocar en ellas nuestras plantillas que utilizaremos para nuestro proyecto, para ello vayamos a nuestra aplicacion core, y dentro de ella creemos una carpeta llamada "templates" y dentro de la misma cremos un archivo html, que sera el mismo utilizado en nuestra funcion listCategory creado anteriormente.


    blog
      |
      core
        |
         - templates/listCategory.html
       

Una vez creada nuestra funcion listCategory y nuestra plantilla html, practicamente estamos completando nuestra estructura MVT (models, views, templates), ahora necesitamos manejar la solicitudes, asignando una URL a esta vista para poder llamarlo desde nuestro navegador, para ello crearemos un archivo.py dentro de nuestra plicacion llamado urls.py y dentro del mismo creemos el siguiente codigo.

    from django.urls import path
    from .views import listCategory

    urlpatterns = [
        path('listCategory/',listCategory, name='listCategory'),
    ]

Una vez hecho esto, debemos ir dentor de nuestra carpeta de configuracion, al archivo url.py a fin de incluir nuestro archivo de configuracion urls creado en nuestra aplicacion de la siguiente manera. Obs: a fin de no hacer demasiado extenso doy por sentado que se tiene un conocimiento sobre esta cuestion.

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('core.urls')),

    ]
    

Guardemos, corramos el servidor y vayamos al local host http://localhost:8000/, donde django nos indica que no existe una coincidencia con la url pasada. Si revisamos nuestro archivo url en el directorio de configuracion, vemos que hemos ingresado como primer argumento en el path 'blog/', y como segundo argumento incluimos nuestro archivo urls ubicado en nuestra aplicacion, donde habiamos puesto como primer argumento del path como 'listCategory/', por lo tanto a fin de haya una coincidencia con la url ingresada y django pueda llamar efectivamente a nuestra vista y devolvernos la plantilla html, necesitamos ingresar lo siguiente http://localhost:8000/blog/listCategory, aqui django ha encontrado una coincidencia y ha llamado a nuestra vista "listCategory", el cual nos ha devuelto una plantilla html vacia hasta este momento.

Se acuerdan el tercer argumento de nuestro "return render(request, 'listCategory.html', {'cat':cat})" en el archivo views.py, formado por un diccionario el cual fue renderizado a nuestra plantilla html, el cual no solo tiene la capacidad para mostrar archivos estaticos sino tambien los datos de nuestra base de datos en especifico, a traves de etiquetas o variables dentro de llaves simples o llaves dobles segun sea un condicional, un bucle o una variable. Probemos en nustra plantilla mostrar lo que hay dentro de el diccionario renderizado.

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>List Category</title>
    </head>
    <body>
        
        <p>List category: {{cat}}</p>
    </body>
    </html>


Vayamos a nuestro navegador y actualizemos la pagina, veremos un "<QuerySet []>", que es la consulta que hemos hecho a la base de datos dentro de nuestro archivo views.py, con la siguiente linea "cat = Category.objects.all()", donde en la variable cat guardamos la consulta realizada a la base de datos, en nuestro caso nos ha devuelto un queryset vacio, ya que no hemos registrado ningun nombre de categoria dentro de nuestra base de datos. Vayamos al panel de administrador de Django y carguemos una categoria, luego vayamos a nuevamente a la url http://localhost:8000/blog/listCategory, actualizemos y tenemos un queryset que nos devuelve un objeto del modelo category con el nombre que registramos, si agregamos varios nombres veremos algo asi:
  
    "List category: <QuerySet [<Category: Python y Django>, <Category: JavasScript>, <Category: Ajax>]>" 
    
 Recorramos la lista dentro de nuestro archivo html para ver que informacion nos proporciona cada registro, para asi poder trabajarlo seguidamente.
 
       <ul>
      {% for categoria in cat %}
          <li>Id: {{categoria.id}} Name: {{categoria.name}}</li>
      {% endfor %}
      </ul>

Esto nos da como resultado lo siguiente: 
  
      Id: 2 Name: Python y Django
      Id: 3 Name: JavasScript
      Id: 4 Name: Ajax
      
Vemos que nos arroja un id y un nombre de la categoria, en  la siguiente parte arreglaremos esto para que podamos ver de una forma ordenada, utilizando una herramienta que es muy util para mostrar datos y poder manipular esos datos desde el front-end.

QUINTA PARTE: En esta parte, trabajaremos nuestro archivo html a fin de mostrar nuestros datos, para ello utilizaremos una herramienta muy util llamada datatable, consistente en una extensión de jQuery que nos permite pintar tablas con paginado, búsqueda, ordenar por columnas, etc, lo pueden encontrar en https://datatables.net/.

DataTables solo tiene una dependencia de biblioteca (otro software en el que se basa para funcionar): jQuery, para ello vayamos a la pagina oficial, descarguemos y guardemoslo, a modo de referencia., que es jquery?, segun la documentacion oficial: es una biblioteca de JavaScript rápida, pequeña y rica en funciones. Hace cosas como recorrido y manipulación de documentos HTML, manejo de eventos, animación y Ajax mucho más simple con una API fácil de usar que funciona en multitud de navegadores. 

Creemos un direcotrio nuevo llamado static en nuestro directorio raiz, a fin de que contenga las librerias y herramientas que utilizaremos en nuestra aplicacion, luego vayamos a nuestro archivo de configuracion, y agreguemos STATICFILES_DIRS, esto a modo de contener nuestos archivos estaticos dentro de un solo directorio para todas nuestras aplicaciones que utilicemos en nuestro proyecto.

    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]
  
Luego dentro de nuestro archivo html, utilicemos la etiqueta "static" para construir la URL para la ruta relativa de nuestro archivo que contiene el jquery descargado.

    {% load static %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>List Category</title>
        <!-- Jquery -->
        <script src="{% static 'lib/jquery-3.6.3.min.js'%}"></script>
    </head>

Creemos una tabla, cuyo codigo se encuentra en https://datatables.net/manual/installation. 

      <table id="table_id" class="display">
          <thead>
              <tr>
                  <th>Column 1</th>
                  <th>Column 2</th>
              </tr>
          </thead>
          <tbody>
            {% for category in cat %}
              <tr>
                  <td>{{ category.id} }</td>
                  <td>{{ category.name }}</td>
              </tr>
             {% endfor %}
          </tbody>
      </table>

Actualicemos nuestra pagina y veremos nuestra tabla con los datos existentes en nuestra base de datos.

      Id 	Name
      2 	Python y Django
      3 	JavasScript
      4 	Ajax
      
Tenemos una tabla valida, ahora nos queda implementar DataTable, primeramente debemos incluir los archivos fuentes en nuestra pagina, para ello vayamos a https://datatables.net/download/ y descarguemos, luego incluye el archivo dentor del directorio static creado anteriormente.

    <!-- DataTable -->
    <link rel="stylesheet" type="text/css" href="{% static 'lib/DataTables/datatables.min.css'%}"/>
    <script type="text/javascript" src="{% static 'lib/DataTables/datatables.min.js"'%}></script>
    
 Incluyamos las rutas para que pueda cargarse junto con nuestro archivo html, una vez hecho esto, nuestra cabecera dentro de nuestro archivo html deberia de lucir de la siguiente manera.
 
     <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>List Category</title
        
        <!-- Jquery -->
        <script type="text/javascript" src="{% static 'lib/jquery-3.6.3.min.js'%}"></script>

        <!-- DataTable -->
        <link rel="stylesheet" type="text/css" href="{% static 'lib/DataTables/datatables.min.css'%}"/>
        <script type="text/javascript" src="{% static 'lib/DataTables/datatables.min.js'%}"></script>
     </head>
     
 Ahora iniciemos nuestra tabla de datos con DataTable, para ello dentro de nuestro documento, luego del body, creemos unas lineas de JavaScript y actulicemos.
 
    <script type="application/javascript">
        $(document).ready( function () {
           $('#table_id').DataTable();
        });
    </script>
 
 
![datatable_1](https://user-images.githubusercontent.com/99599597/214352417-a52f0d72-7360-4035-b4ef-a017c6613518.png)

¡Eso es todo! DataTables agregará ordenamiento, búsqueda, paginación e información a su tabla de manera predeterminada, brindando la capacidad de encontrar la información que desean lo más rápido posible. FUENTE: https://datatables.net/manual/installation. 

SEXTA PARTE: en este apartado utilizaremos Ajax para recuperar nuestros datos desde la base de datos, primeramente, creare un archivo javascript llamado funciones, donde incluire nuestro codigo apartado del archivo html, para organizarnos mejor. Como es una funcion propia, lo incluire dentro del directorio static creado previamente dentro de nuestra aplicacion y agreguemos el directorio en nuestro archivo settings

    STATICFILES_DIRS = [
        BASE_DIR / "static",
        BASE_DIR / "core/static"
    ]
    
Ahora vayamos a nuestro archivo funciones y creemos la solicitud de datos con Ajax para ser cargados directamente a nuestra tabla. Los datos de Ajax son cargados por DataTables simplemente usando las opciones que nos proporciona ajax, para esto nuestro codigo tanto en el archivo js funciones, listCategory.html y el views.py queda de la siguiente manera, luego pasare a explicar punto por punto que fue lo que hicimos.

 1.- Archivo listCategory.html dentro de nuestro directorio templates.
  
        <body>
            {% csrf_token %}
            <table id="table_id" class="display">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>Name</th>
                    </tr>
                </thead>
            </table>
        </body>
Aqui, lo primero que hicimos fue usar la proteccion CSRF de django, ya que realizaremos la solicitud de los datos a traves del metodo POST, para ello usamos la etiqueta {% csrf_token %}, el cual sera enviado junto con la solicitud de Ajax.
        
2.- Archivo funciones.js dentro del directorio static de nuestra aplicacion.
    
          $(document).ready( function () {
          var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
          $('#table_id').DataTable( {
              ajax:{
                  headers: {'X-CSRFToken': csrftoken},
                  url: window.location.pathname,
                  type: 'POST',
                  data: {
                      action: 'search',
                  },
                  dataSrc = ''
              },
              columns: [
                  {"data": [0]},
                  {"data": [1]},
              ]
          } );
      });

Aqui, utilizamos primeramente  $(document).ready(), a fin de poder manipular correctamente nuestra pagina html hasta que el documento se haya cargado completamente, luego creo una variable csrftoken que es igual al valor que contiene nuestro {% csrf_token %}. Una vez hecho esto llamamos a DataTable y cuyos datos son recuperados a traves de una solicitud ajax, como se puede observar precedentemente.
2.1 - headers = en cada XMLHttpRequest, personalizamos el encabezado X-CSRFToken con el valor del token que obtuvimos con la variable csrftoken.
2.2 - url: window.location.pathname, nos devuelve la ruta y el nombre del archivo de la pagina actual, al cual realizara la peticion.
2.3 - data = son los datos que enviamos junto a la peticion, en este caso he enviado un action con el valor 'search', a fin de poder trabajarlo dentro de nuestro archivo views.py, que lo veremos mas claramente a medida que vayamos termianado nuestra aplicacion. 
2.4 - dataSrc = se usa para decirle a DataTables donde esta la matriz de datos en la escructura JSON. En nuestro caso le hemos colocado una cadena vacia como caso especial que le dice a DataTables que espere una matriz. En este caso no requiere configurar los datos de la columnas, esto se debe a que el valor predeterminado para las columnas es el indice las las columnas columns: [ {"data": [0]}, {"data": [1]},], en nuestro caso solo nos devolver una matriz con dos datos que se ubican en la posicion 0 y 1.

3.- Archivo views.py dentro de nuestra aplicacion.
 
    from django.shortcuts import render
    from .models import Category

    from django.http import JsonResponse

      def listCategory(request):
          data = {}
          if request.method == 'GET':
              template_name = 'listCategory.html'
              cat = Category.objects.all()
              return render(request, template_name)
          if request.method == "POST":
              try:
                  action = request.POST['action']
                  if action == 'search':
                      data = list(Category.objects.all().values_list())
                      return JsonResponse(data, safe=False)
              except Exception as e:
                  data['error'] = str(e)
                  return JsonResponse(data, safe=False)
                  
Aqui, lo primero que realizamos es comparar las solicitudes realizadas a nuestra vista, comprobamos si el reques.method corresponde a 'GET' o 'POST', al acceder a nuestra url listCategory/ a traves del metodo 'GET' nos renderiza a nuestro teamplate_name. Anteriormente hablamos sobre  $(document).ready(), una vez cargado completamente nuestra pagina, se llama a DataTable y se realiza la peticion 'POST' con Ajax, esto llama nuevamente a nuestra vista, en donde lo manejamos con los condicionales, en este caso ingresa al segundo condicional, realizamos un try que nos permite probar el bloque de codigo y manejar cualquier tipo de error que pudiera suceder al tratar de obtener el valor de request.POST['action'] o al momento de hacer la consulta con Category.objects.all(). Luego volvemos a agregar un condicional en donde prueba si la variable action es igual a 'search', si esto es true entonces ingresa sobre el bloque y dentro de la variable data obtiene las categorias existentes, pero sin antes convertir los datos y enviarlos con JsonResponse que transforma los datos que le pasa en una cadena JSON y establece el encabezado HTTP del tipo de contenido en application/json.

Luego en caso de que ocurra algun error dentro del codigo try, controlamos el error con except Exception as e, que nos devolverna un mensaje con el tipo de error ocurrido, lo agregamos a data['error] y lo retornamos con JsonResponse. 

Ahora bien, hagamos correr nuestro servidor y verificar que todo salio bien.

![Captura de pantalla 2023-01-25 a la(s) 19 55 11](https://user-images.githubusercontent.com/99599597/214711883-c4254244-d817-4d3c-a020-75612f53ca1d.png)

En esta caputra se puede observar, que se ha cargado correctamente el DataTables, aqui vemos al inspeccionar el documento html, que se ha enviado en la solicitud el dato que le hemos pasado con "action" y su valor 'search'.

![admin_carga_categorias](https://user-images.githubusercontent.com/99599597/215278681-a06e7596-3573-4159-9c0c-83822b60b376.png)


![Captura de pantalla 2023-01-25 a la(s) 20 07 56](https://user-images.githubusercontent.com/99599597/214712476-30108edd-eb71-445b-af6c-6d7481ffd7d2.png)

Y como respuesta una matriz con los datos provenientes de nuestra base de datos, cargado previamente a traves del administrador predeterminado de Django.


 





