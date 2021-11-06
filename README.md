# pp12021grupo1_a2-pp12021grupo1_a2
pp12021grupo1_a2-pp12021grupo1_a2 created by GitHub Classroom


Este es el inicio del repositorio para el GRUPO 2 AULA 1
Alumnos 
Sebastian Ariel Meragelman
Alejandra Battistoni
Victor Fabian Lifata
Vanesa Marisol Saravia


Al momento de entregar el trabajo tenemos 3 proyectos definidos en github que reflejan la metodología de trabajo que aplicamos.
En primera instancia se nos solicitó la realización de un sistema de web scrapping con programación modular y para ello dividimos el proyecto en 3 milestones con xxx issues , cuando estábamos trabajando en el último milestone se nos requirió modificar el método de trabajo y rediseñar el código con una metodología orientada a objetos. Al momento de este nuevo requerimiento teníamos una versión funcional aunque con muchas mejoras pendientes.  Dicha versión permitía descargar datos de la bolsa de madrid desde la página de dicha bolsa obteniendo una tabla de datos usando la librería beautifulsoup,  si bien se evaluó realizar esa extracción usando la librería de selenium nos encontramos que la misma requería mucho mas tiempo y recursos ya que iniciaba una instancia de un navegador para interpretar el contenido y luego sobre ese navegador realizábamos la descarga de información  con métodos propios de selenium,  lo cual reemplazamos por el método request junto a beautiful soup y obtuvimos los mismos resultados pero en menor tiempo (esta técnica es conveniente para este caso particular, ya que si se quiere realizar en otras paginas el web scrapping resultaba más conveniente el uso de selenium, por ejemplo para obtener desde la página de yahoofinance los datos de todas las acciones en forma de tabla ). 
A su vez usamos un segundo mecanismo de obtención de datos mediante la api de investpy,  decidimos usar dicha api para consultar los datos ya que la misma permite consultar los valores de cotización de la bolsa que elijamos y en La Moneda de dicho pais,  así evitamos los problemas que nos traía la api de yahoofinance que traía los valores de acciones pero de una sola bolsa y en dólares (no podíamos traer la bolsa de madrid en euros).
En el caso de esta api si bien no hay mucha documentación (o más bien la documentación estaba orientada a otro uso de la api) pudimos encontrar dos métodos que nos sirvieron para generar una tabla de información,  en uno generamos una lista de acciones disponibles para consultar y en el segundo realizamos una consulta a cada una de esas acciones para retornar su valor histórico, como para nuestro proyecto el interés era trabajar con la cotización al momento de ejecución entonces trabajamos con un rango de fechas del día de ejecución y un día menos. El problema que nos encontramos fue que tanto feriados como fines de semana la bolsa no abre por lo cual debimos generar un chequeo en el retorno de datos para considerar esta situación. 
Este proyecto permitía descargar datos tabulados de ambos mecanismos y guardarlos en formato csv, trabajamos con un esquema de guardar un archivo principal que era pisado en cada ejecución y una copia del mismo con la fecha de la ejecución para tener histórico del mercado.
Por medio de distintas funciones realizamos el análisis de los resultados obtenidos en una fecha determinada con cada origen de datos (api vs webscrapping) , también evaluamos la acción con máxima ganancia y con mayor pérdida, esto es posible de realizar con distintas fechas gracias al registro que mantenemos en distintos archivos.El análisis de valores de pérdida y ganancia lo realizamos usando la librería pandas, con esta cargamos como un dataframe toda la información que se guardó en los archivos csv, y nos valemos de métodos propios de pandas para obtener los resultados.
Encontraran un diccionario en la función que usamos para comparar los orígenes de datos ya que si bien hay muchas similitudes en los nombres , no era posible realizar una comparación de forma directa.
Por otro lado las funciones que realizan el webscrapping estan definidas con numerosos argumentos con la intención que si se desea cambiar la tabla o la página de donde obtenemos los datos sea más fácil re adaptar el código.
Una observación que hacemos es que las llamadas a la api investpy requieren mucho más tiempo para obtener los datos que usando web scrapping.
Se dejó en github bajo el nombre de release V1 una versión descargable del código pero será necesario instalar las librerías que importa el codigo.

Cuando se nos solicitó mirar el sistema de una programación estructurada a una orientada a objetos inmediatamente identificamos la entidad Acción.
A esta entidad la entendimos como un objeto definido con un nombre,un origen de datos, yuna fecha, si bien usamos otros atributos para definir el objeto entendemos que es información que puede o no estar presente para que una acción exista. 
Nombre: se puede identificar con el nombre que nosotros elijamos, aunque es más útil plantear su denominación de la misma forma en que está en su bolsa/método de origen.
Origen: es un identificador que nos sirve para saber de dónde proviene la información que conforma a la acción, es decir de que bolsa, y como obtuvimos la información. El origen es sumamente importante para mantener la consistencia de los datos, ya que de no tener este dato estaríamos obligados a usar una única fuente para obtener la información sin mezclar datos.
Fecha: las acciones requieren el contexto de cuando se evalúan para poder tener sentido,  es por esto que debemos definir las con una fecha.
La entidad Acción también toma como argumentos : valor,variación,volumen. Todos esos valores sirven para analizar el comportamiento de una determinada acción y se podria, si fuera necesario,para un proyecto posterior agregar más parámetros que caractericen a la acción, como por ejemplo La Moneda en la cual esta valuada, o el nombre completo de la empresa cotizada.
Recomendamos que de agregar el parámetro moneda este se defina como una entidad en si mismo ya que permitiría trabajarlo para hacer conversiones de divisas asociadas al mercado donde se definió la acción y la fecha.

La entidad accion tiene definido métodos que nos permiten mostrar los datos/valores de la acción, guardar la acción y sus valores en un archivo csv, evaluar la máxima ganancia y la máxima pérdida en la fecha definida por el objeto, traer un histórico de la acción según su nombre, generar un gráfico sobre estos históricos.
Tanto los históricos como los gráficos dependen de que se haya realizado un registro de distintas fechas de la acción para así poder comparar.
A diferencia del modelo anterior en el cual realizábamos un archivo csv por consulta,  ahora generamos un archivo por origen de datos, de manera que queda un registro histórico de todas las acciones en cada fecha consultada en cada archivo(origen de datos).
Si bien identificamos otra entidad que es la Bolsa, con posibles métodos para crear una lista de acciones favoritas, acciones con mejor margen de ganancia y más riesgosas,  no avanzamos con el desarrollo de la misma por cuestiones de tiempo y el alcance mismo del proyecto inicial. 

Por último se nos planteó el resolver situaciones problemáticas con bases de datos MySQL y MongoDb , y administrar las consultas mediante python.  Para esto dejamos en ramas separadas archivos html con las soluciones a los ejercicios solicitados.



Observaciones: la api investpy no tiene documentado los límites o frecuencia autorizada para ejecutar una consulta, pero pudimos comprobar que esos limites si existen y devuelven como error un código 429, según un issue en el github del programador de investpy, este error se debe a que la página a la cual ejecuta la consulta bloquea la ip del usuario que realiza la consulta pero no hay mayor información al momento sobre esto, igualmente se procedió a consultar en dicho issue para ver si tenemos novedades. En función de dicha respuesta se podría hacer un control para que no se realicen más de determinada cantidad de consultas por tiempo.
Para mas información sobre este problema se puede seguir el issue: https://github.com/alvarobartt/investpy/issues/149

Se verifico que luego de 48hs el banneo de la ip se levantaba, no podemos aun saber si el mismo puede volverse mas prolongado si vuelve a pasar, recomendamos por lo tanto que si se va a llamar a las acciones de investpy se ejecute la llamada para 1 dia por hora (en nuestra simulacion utilizamos un ciclo for para descargar numerosas fechas de registro)

 
