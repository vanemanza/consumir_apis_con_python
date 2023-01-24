### En Github

1) settings-> developer settings-> OAuth Apps.
2) **Crear nueva aplicacion** (nombre, url, descripcion, url callback autenticacion, puede ser la ruta a mi sitio web)-> REGISTRAR
3) Una vez creada, **obtener el client_id** (copiarlo y guardarlo en un archivo settings.py) y el**client_secret** (generar uno nuevo, lo copiamos y lo agregamos al archivo settings.py) con esto podemos implementar la autenticacion en nuestra aplicacion.
4) La aplicacion creada nos permite q nuestros usuarios puedan autenticarse a nuestro servicio web sin la necesidad de definir usuario y contraseña.
5) **Obtener código de acceso** que nos permitirá obtener el **access token** de nuestro usuario, y a traves de él, conocer mas informacion del usuario autenticado. 
Para hacerlo, nos basamos en la documentación oficial de Github ([docs.github.com](https://docs.github.com/es/developers/apps/building-oauth-apps/authorizing-oauth-apps#:~:text=1.%20Solicitud%20de%20la%20identidad%20de%20un%20usuario%20de%20GitHub))
Realizar una petición a :
**`GET https://github.com/login/oauth/authorize`** 
y enviar como parámetros el client_id y un scope.
6)Crear la url con los parametros:
**https://github.com/login/oauth/authorize?client_id=<client_id>&scope=user** y realizar la petición mediante un navegador, que nos redigirá al sitio web de github, donde confirmamos que queremos autenticarnos con la aplicacion mediante su servicio. Una vez autorizada la operación nos redirije a la url que definimos en el paso 2 cuando creamos la aplicación, y en la URL se muestra el código que usaremos para obtener el access token del cliente. (Por ejemplo: "https://misitio.com/?code=<code>") (Si no queremos hacerlo de forma manual, podemos crear un botón que nos lleve a la página, a la url.) 
El código lo puedo guardar en el archivo main.py en una variable llamada code. 
8) Una vez que tenemos el código de acceso, obtendremos el token del usuario. En el archivo main, creo una variable llamada URL, donde guardo la dirección a la que haré la petición POST, pasandole como parametros (client_id, client_secret y code).  **`POST https://github.com/login/oauth/access_token`** 
(https://docs.github.com/es/developers/apps/building-oauth-apps/authorizing-oauth-apps#:~:text=Intercambie%20este%20valor%20code%20por%20un%20token%20de%20acceso%3A)
9) en main.py defino un diccionario con los parámetros y con los encabezados, y realizamos la petición, almacenandola en la variable response, condicionamos la respuesta y la imprimimos.
10) cuando ejecutamos el archivos main, obtenemos un objeto donde podemos ver el token del usuario para obtener su información.Podemos copiarlo y almacenarlo en una variable.
11) Si hacemos una peticion al servidor de Github, podremos obtener mas información del usuario.

continuar desde el video de la clase 18