Tema 1 ·El patrón Repository

1. ¿Qué es el patrón Repository (o DAO) y qué problema resuelve?

= El patrón Repository es una clase que se encarga únicamente de comunicarse con la base de datos guarda,  busca, actualiza y borra 	 datos. En el RPG Manager sería PersonajeRepository, con métodos como guardar(guerrero) y buscarPorId(id). Resuelve el problema de tener el código de la base de datos mezclado por todo el programa. Al estar en un solo lugar, si se cambia de MariaDB a MongoDB solo hay que modificar esa clase y el resto del proyecto sigue funcionando igual. DAO es otro nombre para la misma idea.

2. ¿Qué diferencia hay entre la capa de negocio (Service) y la capa de datos
(Repository)? Den un ejemplo con una regla del RPG Manager.

=El Service contiene las reglas del juego y decide si una acción se puede hacer. El Repository solo guarda y busca datos, sin conocer las reglas. En el RPG Manager, al crear un Guerrero, el PersonajeService primero revisa que su vida no sea negativa. Si cumple la regla, le pide al PersonajeRepository que lo guarde. Si no la cumple, el Service lo rechaza y el Repository nunca se entera. Es decir, el Service decide y el Repository ejecuta.

3. ¿Por qué se dice que un Repository no debe validar reglas de negocio?

=Porque su única responsabilidad es manejar los datos. Si la regla de la vida del Guerrero estuviera dentro del Repository de MariaDB, al crear uno nuevo para MongoDB habría que repetir la regla, y si se olvida, el juego aceptaría Guerreros con vida negativa. Además, tener todas las reglas en el Service facilita encontrar y corregir errores, porque siempre se sabe dónde están.

Fuentes

https://platzi.com/blog/patron-repository/


Tema 2 · Contratos en Java y Python

1. ¿Qué es una interface en Java? ¿Qué pasa si una clase que la implementa olvida un
método?

=Una interface en Java es como una plantilla donde se escribe qué funciones tiene que tener una clase, pero sin programarlas. En nuestro RPG Manager, la interface PersonajeRepository solo dice que tiene que existir una función para guardar y otra para buscar personajes. Luego otra clase, como MariaDBPersonajeRepository, usa esa plantilla y programa lo que hace cada función. Si a esa clase le falta una de las funciones, Java marca error y el programa no se puede ejecutar hasta que la agreguemos.

2. ¿Qué es una clase abstracta con ABC y @abstractmethod en Python? ¿Qué pasa si
intentan crear un objeto de esa clase?

=Es lo mismo que la interface, pero hecho en Python. Es una clase “molde” que solo dice qué funciones se necesitan, sin programarlas. Se escribe ABC para decir que es un molde, y @abstractmethod encima de cada función que es obligatoria. En el RPG Manager, PersonajeRepository sería el molde con guardar y buscar_por_id, y MongoPersonajeRepository sería la clase que las programa de verdad. Si tratamos de crear un objeto directo del molde, Python da un error (TypeError), porque el molde está incompleto.

3. ¿En qué se parecen y en qué se diferencian las dos formas?

=Las dos sirven para lo mismo: obligar a que las clases tengan las mismas funciones. Así, el repositorio de MariaDB y el de MongoDB del RPG Manager se pueden usar igual. La diferencia es que Java nos avisa del error antes de ejecutar el programa, y Python nos avisa hasta que intentamos crear el objeto. Además, se escriben distinto: en Java se usa interface, y en Python se usa ABC.

Fuentes

https://docs.python.org/es/3.10/library/abc.html
https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html

Uso de IA

Se usó Claude para entender la diferencia entre una interface de Java y una clase abstracta de Python.

Tema 3 ·Inyección de dependencias por constructor

1. ¿Qué significa "programar contra una interfaz y no contra una implementación"?

=Significa que el código se apoya en la lista de funciones (la interface) y no en una clase en particular. En el RPG Manager, el PersonajeService solo sabe que tiene un PersonajeRepository que puede guardar y buscar personajes. No le importa si ese repositorio usa MariaDB o MongoDB. Por eso, si cambiamos de base de datos, el Service queda igual.

2. ¿Qué es la inyección de dependencias por constructor? Explíquenlo con un
PersonajeService que necesita guardar personajes.

=Es cuando una clase recibe lo que necesita desde afuera, en vez de crearlo ella misma. El PersonajeService necesita un repositorio para guardar personajes. Entonces, cuando lo creamos, le pasamos el repositorio dentro del paréntesis, que es el constructor:
PersonajeService service = new PersonajeService(repositorio);

3. ¿Qué ventaja tiene que el Service reciba el repositorio en vez de crearlo él mismo?
=Que se puede cambiar de base de datos fácil. Si el Service creara el repositorio de MariaDB por su cuenta, habría que abrir el Service y modificarlo para usar MongoDB. Como lo recibe, solo cambiamos cuál le damos desde el main y el Service no se toca.

Uso de IA

Se usó Claude para entender la diferencia entre crear el repositorio dentro del Service y recibirlo por el constructor.

Tema 4 · Configuración y secretos

1. ¿Cómo se lee un archivo .properties en Java y un archivo .ini en Python? Nombren la clase o el módulo que se usa.

= Un archivo de configuración es un archivo aparte donde guardamos datos como el host, el usuario y la contraseña de MariaDB, para no escribirlos directamente dentro del código. Así, el PersonajeRepository del RPG Manager no tiene la contraseña escrita en sus líneas: la lee desde ese archivo cuando la necesita, y si algún día cambia la contraseña, solo se edita el archivo y no el código.

En Java, esos datos se guardan en un archivo config.properties y se leen con la clase Properties (del paquete java.util). Primero se abre el archivo con un FileInputStream, luego se llama al método load() para cargarlo, y finalmente se pide cada dato por su nombre, por ejemplo getProperty("db.password"), que devuelve la contraseña.

En Python, los datos se guardan en un archivo config.ini, dividido en secciones como [mariadb], y se leen con el módulo configparser. Se crea un ConfigParser(), se lee el archivo con config.read("config.ini") y se obtiene el dato con config["mariadb"]["password"].


2. ¿Para qué sirve .gitignore y qué pasa si un archivo ya se subió antes de ignorarlo?

= El .gitignore es un archivo donde escribimos qué cosas Git no debe subir al repositorio. En nuestro RPG Manager ya ignora __pycache__/, *.pyc y .venv/.

Si el archivo ya se había subido antes, agregarlo al .gitignore no sirve, porque Git ya lo está siguiendo y el .gitignore solo funciona con archivos que Git todavía no conoce. Hay que dejar de seguirlo con git rm --cached config.ini y hacer commit. 

3. Busquen un caso real de contraseñas o llaves filtradas en GitHub: qué pasó y qué consecuencias tuvo.

= Toyota (2022). Un contratista que trabajaba en el sitio web de T-Connect subió parte del código a un repositorio público de GitHub en diciembre de 2017, y dentro del código iba una llave de acceso al servidor donde estaban los datos de los clientes. casi cinco años después,quedaron expuestos los correos y números de gestión de 296.019 clientes (no estaban nombres, teléfonos ni tarjetas). Toyota cerró el acceso, cambió la llave. En nuestro caso sería como subir la contraseña de MariaDB a un repo público: cualquiera podría borrar o cambiar a Ragnor, Isolde, Lyra y todos sus inventarios.

Fuentes

https://blog.gitguardian.com/toyota-accidently-exposed-a-secret-key-publicly-on-github-for-five-years/
https://www.infosecurity-magazine.com/news/toyota-data-leak-customers/

Uso de IA

Se usó Claude para reescribir las respuestas con un lenguaje más sencillo y para entender qué pasa con el historial de Git cuando un archivo ya se subió antes de ponerlo en el .gitignore.


Tema 5 · MariaDB desde el código

1. ¿Qué es JDBC y qué hace un driver? ¿Qué librería cumple ese papel en Python para MariaDB?

= JDBC (Java Database Connectivity) es la forma estándar que tiene Java para conectarse a una base de datos y mandarle consultas SQL desde el código. 

El driver es como un traductor: JDBC solo define cómo se piden las cosas, y el driver de cada base de datos convierte esas peticiones al idioma que entiende esa base de datos. Sin el driver, Java no podría hablar con MariaDB. 

En Python ese papel lo cumple PyMySQL, que sería la librería que usaría nuestro PersonajeRepository para guardar y buscar personajes en la tabla personaje.

2. ¿Qué es la inyección SQL? Muestren un ejemplo con el nombre de un personaje y expliquen por qué PreparedStatement (Java) o los parámetros %s (Python) la evitan.

= Es cuando alguien escribe SQL dentro de un campo del formulario y la base de datos lo ejecuta como si fuera parte de la consulta. 

Si armamos la consulta pegando textos: "SELECT * FROM personaje WHERE nombre = '" + nombre + "'", y alguien escribe como nombre Ragnor' OR '1'='1, la condición queda siempre verdadera y la consulta devuelve todos los personajes. Incluso un nombre normal como O'Brien rompería la consulta, porque la comilla del apellido cierra el texto antes de tiempo. 

Con PreparedStatement (nombre = ?) o con %s en Python (WHERE nombre = %s) la consulta y el dato viajan por separado, así que lo que escriba el usuario siempre se trata como un nombre y nunca como código SQL.

3. ¿Qué es una transacción y qué hace commit()? ¿Qué pasa en PyMySQL si no se llama?

= Una transacción es un grupo de operaciones que se tratan como una sola: o se hacen todas o no se hace ninguna. Por ejemplo, al registrar a Lyra se requieren dos: una en la tabla personaje y otra en la tabla inventario (Arco Élfico y Flechas de Plata). Si la segunda falla, la primera debe revertirse para no dejar a Lyra registrada sin su equipamiento, lo que dejaría los datos inconsistentes. La instrucción commit() confirma los cambios y los hace permanentes, mientras que rollback() los descarta.

En PyMySQL si no se invoca commit(), el INSERT parece ejecutarse correctamente, pero al cerrar la conexión los cambios se pierden y no quedan almacenados en la base de datos.

4. ¿Por qué hay que cerrar las conexiones? ¿Qué es try-with-resources en Java y with en Python?

= Abrir una conexión con MariaDB es como abrir una llamada telefónica con la base de datos: mientras la llamada siga abierta, ocupa una línea del servidor, y MariaDB solo permite cierto número de líneas al mismo tiempo. Si cada vez que guardamos o buscamos un personaje (por ejemplo, a Ragnor) dejamos la conexión abierta, las líneas se acaban y nadie más puede conectarse. Por eso siempre hay que cerrarla cuando terminamos.

Como es fácil olvidarlo, en Java se llama try-with-resources: los recursos se abren dentro de los paréntesis del try, por ejemplo try (Connection con = ...) { ... guardar a Ragnor ... }, y Java los cierra solo cuando el bloque termina, incluso si hubo un error. 

En Python se usa with, por ejemplo with conexion.cursor() as cursor:, y el cursor se cierra solo al salir del bloque. La conexión se cierra con conexion.close(), y lo mejor es ponerlo dentro de un finally, que es un bloque que siempre se ejecuta, haya error o no. Así la conexión queda cerrada aunque algo falle al guardar al personaje.


Uso de IA

Se usó Claude para reescribir las respuestas en un lenguaje más claro y para entender por qué PyMySQL no guarda los cambios si no se llama a commit(). Tambien se hizo uso para buscar try-with-resources en Java y with en Python.


Tema 6 · MongoDB desde el código

1. ¿Qué es un ObjectId y qué información guarda por dentro?

= Es el identificador único que MongoDB le pone por defecto al campo _id de cada documento. Por ejemplo, cuando insertamos a Aether Noctis, MongoDB le crea un ObjectId sin que nosotros hagamos nada. ( Mide 12 bytes y se muestra como 24 caracteres hexadecimales. Por dentro guarda 4 bytes con la fecha de creación (segundos desde 1970), 5 bytes con un valor aleatorio y 3 bytes de un contador que va subiendo)

Por eso, solo con el ObjectId de un personaje se puede saber cuándo fue creado.

2. ¿En qué se parece un documento de MongoDB a un HashMap de Java o a un dict de Python?

= Los tres guardan pares clave-valor. El documento de Lyra { nombre: "Lyra", clase: "Arquero", nivel: 19, precision: 97 } es casi igual a un dict de Python o a un HashMap<String, Object> de Java. 
Los tres también pueden tener listas y datos anidados, como el inventario de Lyra con el Arco Élfico y las 40 Flechas de Plata. Además, cada documento puede tener campos distintos.

3. ¿Qué diferencia hay entre MongoDB local, MongoDB Atlas y mongoplayground.net? ¿Cuál de los tres puede usar un programa en Java o Python?

= MongoDB local es la base de datos instalada en nuestro propio computador, y el programa se conecta a ella por localhost. 

MongoDB Atlas es MongoDB en la nube: los datos están en servidores de internet y el programa se conecta con una cadena de conexión que lleva usuario y contraseña

mongoplayground.net es solo una página web para probar consultas con datos de ejemplo; no es una base de datos real y no se puede conectar desde un programa. Entonces, nuestro RPG Manager en Java o Python puede guardar a Ragnor y a Morgath en el MongoDB local o en Atlas, pero no en el playground.

Fuentes

https://www.mongodb.com/docs/manual/core/object-id
https://www.mongodb.com/docs/atlas/
https://mongoplayground.net/

Uso de IA

Se usó Claude para reescribir las respuestas con un lenguaje más sencillo y para entender qué guarda por dentro un ObjectId y la diferencia entre MongoDB local, Atlas y el playground.


Tema 7 · ORM

1. ¿Qué es un ORM?

= ORM significa Object-Relational Mapping (mapeo objeto-relacional). Es una herramienta que conecta las clases del programa con las tablas de la base de datos, para que trabajemos con objetos y no tengamos que escribir el SQL a mano. 
En el RPG Manager, nuestra clase Personaje (con nombre, clase, nivel y vida) quedaría conectada con la tabla personaje, y cada objeto, como Ragnor nivel 16, sería una fila de esa tabla. Cuando le decimos al ORM que guarde el objeto, él genera el INSERT por nosotros.

2. Nombren uno de Java y uno de Python.

= En Java, Hibernate, que sigue el estándar JPA. En Python, SQLAlchemy.

3. Den una ventaja y una desventaja de usar un ORM en lugar de escribir el SQL a mano.

= Ventaja: se escribe menos código repetido, porque no hay que armar a mano cada INSERT y SELECT del PersonajeRepository, y además cambiar de base de datos es más fácil porque el ORM se encarga de las diferencias del SQL. 

Desventaja: perdemos control sobre el SQL que realmente se ejecuta, y a veces el ORM hace consultas lentas(por ejemplo cargar el inventario de cada personaje con una consulta aparte por cada uno. También toca aprender cómo funciona la herramienta, y cuando algo falla es más difícil saber dónde está el problema)


Uso de IA

Se usó Claude para reescribir las respuestas en un lenguaje más claro y para entender la diferencia entre escribir el SQL a mano y usar un ORM.

