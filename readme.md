<h1>API WEB DE UNA BIBLIOTECA</h1>

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


<p>Esta Api trabaja en formato ".json", a continuación vamos a explicar los endpoint del proyecto:</p>

<p>Las peticiones han sido realizadas en Insomnia, asegurarse que los <em>"headers"</em> sean <code>Content-Type: application/json</code>.</p>


<h2>AGREGAR UN NUEVO CLIENTE</h2>

<p>La ruta para este enpoint es la siguiente: "/guardar-cliente"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "dni": "0xxxxxxxR",
  "nombre": "Test",
  "telefono": 6xxxxxxxx
}</code></pre>

<p>Esto agregará un nuevo cliente a la tabla "Crear Cliente"</p>


<h2>BUSCAR CLIENTES</h2>

<p>La ruta para este enpoint es la siguiente: "/buscar-clientes"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "dni": "5xxxxxxxC",
  "id": 2,
  "nombre": "Test",
  "telefono": 6xxxxxxxx
}</code></pre>

<p>Esto buscará un cliente según su "id", "dni", "nombre" y/o "teléfono" en la tabla "Buscar Clientes"</p>


<h2>BORRAR CLIENTE</h2>

<p>La ruta para este endpoint es la siguiente: "/borrar-cliente"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "id": 4
}</code></pre>

<p>Esto borrará el cliente con ese id asignado, en la tabla "Borrar Cliente"</p>


<h2>ACTUALIZAR CLIENTE</h2>

<p>La ruta para este endpoint es la siguiente: "/actualizar-cliente"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "dni": "5XXXXXXXB",
  "id": 2,
  "nombre": "Test",
  "telefono": 6xxxxxxxx
}</code></pre>

<p>Se podrá modificar cualquiera de estos campos por la información correcta o nueva, quedando así actualizada en la tabla "Actualizar Cliente". El id es obligatorio y no se puede modificar.</p>


<h2>GUARDAR LIBRO</h2>

<p>La ruta para este endpoint es la siguiente: "/guardar-libro"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "autor": "Stephanie Meyer",
  "año": 2006,
  "genero": "Fantasía, Juvenil",
  "titulo": "Crepúsculo"
}</code></pre>

<p>Esto agregará un nuevo libro a la tabla "Guardar Libro"</p>


<h2>BUSCAR LIBROS</h2>

<p>La ruta para este endpoint es la siguiente: "/buscar-libros"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "autor": "Stephen King",
  "año": 1986,
  "genero": "Terror",
  "id": 6,
  "titulo": "It"
}</code></pre>

<p>Se puede realizar la búsqueda por cualquiera de esos campos en la tabla "Buscar Libro"</p>


<h2>BORRAR LIBRO</h2>

<p>La ruta para este endpoint es la siguiente: "/borrar-libro"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "id": 8
}</code></pre>

<p>Esto borrará el libro con ese id asignado, en la tabla "Borrar Libro"</p>


<h2>ACTUALIZAR LIBRO</h2>

<p>La ruta para este endpoint es la siguiente: "/actualizar-libro"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "id": 1,
  "titulo": "Harry Potter y La Piedra Filosofal",
  "genero": "Fantasía",
  "autor": "J.K.Rowling",
  "año": 1997
}</code></pre>

<p>Se podrá modificar cualquiera de estos campos por la información correcta o nueva, quedando así actualizada en la tabla "Actualizar Libro". El id es obligatorio y no puede modificarse.</p>


<h2>AGREGAR UN NUEVO PRÉSTAMO</h2>

<p>La ruta para este endpoint es la siguiente: "/nuevo-prestamo"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "id_cliente": 3,
  "id_libro": 8
}</code></pre>

<p>Con estos dos datos quedará registrado el préstamo del libro, con los datos de ese cliente y durante cuántos días se mantendrá activo, en la tabla "Nuevo Préstamo"</p>


<h2>BUSCAR PRÉSTAMO</h2>

<p>La ruta para este endpoint es la siguiente: "/buscar-prestamos"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "dni": "5XXXXXXXB"
}</code></pre>

<p>La búsqueda sólo puede ser realizada con el dni del cliente, donde después se verá reflejada toda la información del préstamo realizado por cliente, en la tabla "Buscar Préstamo"</p>


<h2>BORRAR PRÉSTAMO</h2>

<p>La ruta para este endpoint es la siguiente: "/borrar-prestamo"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "id": 1
}</code></pre>

<p>En este caso, se debe anular el préstamo con el id del mismo.</p>


<h2>DEVOLVER PRÉSTAMO</h2>

<p>La ruta para este endpoint es la siguiente: "/devolver-prestamo"</p>
<p>La petición para este endpoint tiene la siguiente forma:</p>
<pre><code>{
  "id": 3
}</code></pre>

<p>Con el id del préstamo podemos darlo por finalizado, y en la tabla "Préstamos" la columna devuelto quedará a True, quedando reflejados los datos del cliente, del libro y el contador de días restante se quedará a cero.</p>


