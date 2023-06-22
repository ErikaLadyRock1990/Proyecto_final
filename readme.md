<h1>APLICACIÓN WEB DE UNA BIBLIOTECA "BiblioXpert</h1>

<p>Programa hecho en python con el framework flask.</p>
<h2>Descripción de la Api:</h2>

<p>CRUD de clientes: Crea, lee, actualiza y elimina información de tus clientes. Puedes ver su nombre, dirección, número de teléfono y correo electrónico.</p>
<p>CRUD de libros: Crea, lee, actualiza y elimina información sobre los libros de la biblioteca. Puedes ver su título, autor, género y año.</p>
<p>Registro de préstamos y devoluciones: Registra quién tiene prestado qué libro y cuándo debe ser devuelto.</p>
<p>Historial de préstamos: Obtén información acerca de los libros que ha tomado prestados un cliente en el pasado.</p>

<h2>Instalación</h2>
<p>Crear un entorno en python que se llama "entorno_biblioteca" y ejecutar el comando</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Ejecución del programa</h2>
<p>Inicializar el servidor de flask:</p>
<ul>
  <li>En Mac: <code>export FLASK_APP=main.py</code></li>
  <li>En Windows: <code>set FLASK_APP=main.py</code></li>
</ul>
<p>Otra opción de ejecución:</p>
<ol>
  <li>Instalar <code>pip install python-dotenv</code></li>
  <li>Crear un archivo <code>.env</code> y dentro agregar lo siguiente: <code>FLASK_APP=main.py FLASK_DEBUG=True</code></li>
  <li>Luego, para lanzar el programa, en la terminal ejecuta el comando: <code>flask run</code></li>
</ol>

<p>Comando para ejecutar el servidor:</p>
<pre><code>flask --app main run</code></pre>

<p>Comando para ejecutar el servidor en otro puerto (por defecto es el 5000):</p>
<pre><code>flask --app main run -p 5002</code></pre>

<p>Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real:</p>
<pre><code>flask --app main --debug run</code></pre>


<p>Esta Api trabaja en formato ".json", a continuación vamos a explicar como funciona el proyecto:</p>



<h2>AGREGAR UN NUEVO CLIENTE</h2>

<p>La ruta para guardar cliente es la siguiente: "/guardar-cliente"</p>
<p>La petición para este formulario tiene los siguientes parámetros obligatorios:</p>
<pre><code>{
 DNI
 Nombre
 Teléfono

}</code></pre>

<p>Esto agregará un nuevo cliente a la tabla "Cliente"</p>
<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>


<h2>BUSCAR CLIENTES</h2>

<p>La ruta para buscar clientes es la siguiente: "/buscar-clientes"</p>
<p>Se puede realizar la búsqueda de cualquier cliente únicamente pulsando el botón de Buscar, donde aparecerán todos los clientes registrados en la base de datos. También se pude realizar a búsqueda introduciendo un único dato de los anteriores (Dni, nombre y/o teléfono) o varios, para que la búsqueda sea más específica.</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>


<h2>BORRAR CLIENTE</h2>

<p>Para borrar clientes primero es necesario acceder a la ruta: "/buscar-clientes" y darle al botón Buscar. Una vez encontrado el cliente deseado, se hará una llamada al endpoint :"/borrar_cliente", al cual se le pasará el Id del cliente seleccionado y esto lo borrará de la base de datos.</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>



<h2>ACTUALIZAR CLIENTE</h2>

<p>Para actualizar clientes primero es necesario acceder a la ruta: "/buscar-clientes" y darle al botón de Buscar. Una vez encontrado el cliente deseado, se hará una llamada al endpoint :"/actualizar_cliente", esto le llevará a una nueva pantalla donde se pasará el dato que se desee actualizar, pudiendo ser dni, nombre o teléfono.
Esto dejará actualizada la información de los clientes en la tabla "Cliente" </p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>



<h2>GUARDAR LIBRO</h2>

<p>La ruta para guardar libro es la siguiente: "/guardar-libro"</p>
<p>La petición para este formulario tiene los siguientes parámetros obligatorios:</p>
<pre><code>{
 Título
 Autor
 Género
 Año

}</code></pre>

<p>Esto agregará un nuevo libro a la tabla "Libro"</p>
<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>


<h2>BUSCAR LIBROS</h2>

<p>La ruta para buscar libros es la siguiente: "/buscar-libros"</p>
<p>Se puede realizar la búsqueda de cualquier libro únicamente pulsando el botón de Buscar, donde aparecerán todos los ejemplares disponibles en la base de datos. También se pude realizar a búsqueda introduciendo un único dato de los anteriores (Título, autor, género o año) o varios, para que la búsqueda sea más específica.</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>


<h2>BORRAR LIBRO</h2>

<p>Para borrar libros primero es necesario acceder a la ruta: "/buscar-libros" y darle al botón Buscar. Una vez encontrado el libro deseado, se hará una llamada al endpoint :"/borrar_libro", al cual se le pasará el Id del libro seleccionado y esto lo borrará de la base de datos.</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>



<h2>ACTUALIZAR LIBRO</h2>

<p>Para actualizar libros primero es necesario acceder a la ruta: "/buscar-libros" y darle al botón de Buscar. Una vez encontrado el libro deseado, se hará una llamada al endpoint :"/actualizar_libro", esto le llevará a una nueva pantalla donde se pasará el dato o datos que se deseen actualizar, pudiendo ser título, autor, género y/o año </p>

<p>Se podrá modificar cualquiera de estos campos por la información correcta o nueva, quedando así actualizada en la tabla "Libro"</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>



<h2>AGREGAR UN NUEVO PRÉSTAMO</h2>

<p>Para realizar un nuevo préstamo primero es necesario acceder a la ruta: "/buscar-clientes" y darle al botón Buscar. Una vez encontrado el cliente deseado, se hará una llamada al endpoint :"/nuevo-prestamo", esto llevará a una nueva pantalla donde aparecerán los datos del cliente y, debajo, una tabla con todos los libros disponibles para prestar. Una vez seleccionado el libro deseado y pinchando sobre éste, se procederá a pulsar el botón de Realizar Préstamo.Se pueden prestar varios libros a un mismo cliente, que no estén en préstamo en ese momento. </p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>


<h2>BUSCAR PRÉSTAMOS</h2>

<p>La ruta para buscar préstamos es la siguiente: "/buscar-prestamos"</p>
<p>Se puede realizar la búsqueda de cualquier préstamo únicamente pulsando el botón de Buscar, donde aparecerán todos los prestamos realizados hasta la fecha en la base de datos.También aparecerán datos informativos como cúantos días de préstamo le quedan a ese cliente y si ya está devuelto o no.</p>

<p>La búsqueda también puede ser realizada con el dni del cliente, donde después se verá reflejada toda la información del préstamo realizado por cliente, en la tabla "Prestamo"</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>

<h2>BORRAR PRÉSTAMO</h2>

<p>Para borrar prestamos primero es necesario acceder a la ruta: "/buscar-prestamos" y darle al botón Buscar. Una vez encontrado el préstamo deseado, se hará una llamada al endpoint :"/borrar_prestamo", al cual se le pasará el Id del préstamo seleccionado y esto lo borrará de la base de datos.</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>


<h2>DEVOLVER PRÉSTAMO</h2>

<p>Para devolver prestamos primero es necesario acceder a la ruta: "/buscar-prestamos" y darle al botón Buscar. Una vez encontrado el préstamo deseado, se hará una llamada al endpoint :"/devolver_prestamo", al cual se le pasará el Id del préstamo seleccionado y esto lo actualizará de la base de datos.</p>

<p>Con el id del préstamo podemos darlo por finalizado y aparecerá el mensaje de "Se ha devuelto el préstamo correctamente", y en la tabla "Préstamo" la columna devuelto quedará a True, quedando reflejados los datos del cliente, del libro y el contador de días restante se quedará a cero.</p>

<p>Se puede volver a la pantalla principal pulsando "BiblioXpert</p>
