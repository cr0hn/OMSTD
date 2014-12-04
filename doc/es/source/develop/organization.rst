Organización y estructura
=========================

En este bloque se tratan los casos de estudio relacionados con la organización y estructura de proyectos.

----

.. _st-001:

ST-001 - Estructura de proyecto
-------------------------------

Problema
********


Muchas herramientas no contemplan la opción de ser usadas como librería (con un "import") además de por linea de comandos, o la interfaz que tengan definida.

Su uso puede ser complicado y, muchas veces, tan solo pueden ser usadas por linea de comandos, lo que implica llamar a un proceso externo del sistema y parsear su salida.

Solución
********

Una estructura correcta en la organización de archivos, pensada para ser re-utilizable.

Cómo
****

En la imagen se puede ver la estructura propuesta:

.. image:: ../../../images/st-001.01.png

Donde:

+ **LICENCE**: Fichero de licencia. Contiene el texto legal con el que queremos redistribuir nuestro código.
+ **README.rst**: Fichero índice de documentación del proyecto. Será el primero en mostrarse y leerse por defecto.
+ **requirements.txt**: Contiene las dependencias de librerías externas de nuestro proyecto.
+ **setup.py**: Contiene información para la instalación, configuración y redistribución de nuestro software.
+ **TODO.rst**: Ideas futuras a implementar en nuestro proyecto. Es buena idea tenerlo por si alguien quiere colaborar con nuestro proyecto, ya que podrá encontrar tareas e ideas por hacer.
+ **app_name**: Carpeta, que actúa como paquete Python, con el nombre de nuestra aplicación.
+ **app_name/bin**: Ejecutables disponibles en nuestra aplicación.
+ **app_name/doc**: Archivos de documentación, usualmente escrita con `Shpinx <http://sphinx-doc.org>`_. Esta guía es un ejemplo de su uso.
+ **app_name/lib**: Librerías propias que genere nuestra aplicación.
+ **app_name/test**: Contiene los diferentes test de la aplicación: Unitarios, de integración, rendimiento...

----

.. _st-002:

ST-002 - Entrada de parámetros globales
---------------------------------------

Problema
********


Una vez preparada la estructura para nuestra aplicación, ahora queremos "llamar" o ejecutar el programa en cuestión. Problemas:

* Añadir nuevos parámetros de entrada al programa, requiere muchos cambios.
* El código se hace cada vez más enrevesado e inmanejable.
* Cambios de versiones de un mismos programas son incompatibles.

`Ejemplo ST-002.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/002/st-002-p1.py>`_

Este ejemplo de programa que divide dos números. Acepta 2 parámetros por linea de comandos:

* Nominado
* Denominador

Si ocurre una división por 0 devuelve -1:

.. literalinclude:: ../../../../examples/develop/st/002/st-002-p1.py
    :lines: 25-
    :linenos:

`Ejemplo ST-002.P02 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/002/st-002-p2.py>`_

Ahora queremos añadir otro parámetro, "verbosity", como opción a nuestro programa.

Vemos que hay que modificar el código en 2 sitios diferentes. En todos aquellos donde se tenga que pasar información de las opciones de ejecución:

.. literalinclude:: ../../../../examples/develop/st/002/st-002-p2.py
    :lines: 25-
    :linenos:
    :emphasize-lines: 6,7,16

Solución
********

Hacer un objeto global que sea el que contenga los parámetros globales de ejecución (proyectos grandes, como nmap, proyecto lo hacen de esta forma):

Cómo
****

`Ejemplo ST-002.S01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/002/st-002-s1.py>`_

.. literalinclude:: ../../../../examples/develop/st/002/st-002-s1.py
    :lines: 26-
    :linenos:
    :emphasize-lines: 2-9,31-35


----

.. _st-003:

ST-003 - Gestión de resultados
------------------------------

Problema
********


Recuperar la información de salida de una aplicación es muy complicado:

* No está estandarizada
* Hay que parsear muchos XML/JSON.
* La herramienta solo reporta resultados por consola.

Usando el mismo ejemplo que en el anterior caso:

`Ejemplo ST-003.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/003/st-003-p1.py>`_

.. literalinclude:: ../../../../examples/develop/st/003/st-003-p1.py
    :lines: 25-
    :linenos:

Cuando queremos añadir un parámetro nuevo en la devolución, vemos que hay que modificar varias lineas de código:

`Ejemplo ST-003.P02 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/003/st-003-p2.py>`_

.. literalinclude:: ../../../../examples/develop/st/003/st-003-p2.py
    :lines: 26-
    :linenos:
    :emphasize-lines: 4-5,7,9,20,22

Solución
********

Usar objetos genéricos que contengan la información resultante de la ejecución del a herramienta.

Además, estos objetos, nos permiten abstraer el almacenamiento de información, de cómo ésta es exportada o transformada: XML, JSON, HTML, PDF ...

Cómo
****

`Ejemplo ST-003.S01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/003/st-003-s1.py>`_

.. literalinclude:: ../../../../examples/develop/st/003/st-003-s1.py
    :lines: 26-
    :linenos:
    :emphasize-lines: 2-8,14-15,17-18,20,32,34


----

.. _st-004:

ST-004 - Unificar puntos de entrada
-----------------------------------

Problema
********


Tengo que cambiar mucho código y rehacer gran parte de mi aplicación, cada vez que quiero hacer una nueva UI (User Interface):

* Linea de comandos.
* Interfaz gráfica.
* Web.
* Que se use como librería.


.. image:: ../../../images/st-004.01.png

Solución
********

Centralizar el punto de entrada a la ejecución de tu aplicación en un único punto y que todas las UI usen el mismo.

.. image:: ../../../images/st-004.02.png

Cómo
****

Incluir el concepto de api.py y enseñar como el command line y el import funcionan igual.

.. image:: ../../../images/st-004.03.png

`Ejemplo ST-004.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/004/>`_

Tras incluir el fichero "api.py", la UI de linea de comandos (`st-004-s1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/004/st-004-s1.py>`_) nos quedará como sigue:

.. literalinclude:: ../../../../examples/develop/st/004/st-004-s1.py
    :lines: 26-
    :linenos:
    :emphasize-lines: 1,16


Si echamos un vistazo a `api.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/004/api.py>`_, podemos observar que este fichera centraliza las llamadas al resto de librerías:

.. literalinclude:: ../../../../examples/develop/st/004/api.py
    :lines: 28-
    :linenos:
    :emphasize-lines: 2,5-6


----

.. _st-005:

ST-005 - La linea de comandos
-----------------------------

Problema
********

Crear una linea de comandos avanzada puede no resultar sencilla, y mucho menos intutiva.

Estos son algunos de los problemas más comunes que podemos encontrarnos:

+ Crear opciones posicionales: :samp:`main.py -n -i 9 POSITIONAL_PARAM`.
+ Crear una ayuda personalizada, cuando se ejecute la opción *-h*: :samp:`main.py -h`.
+ Los tipos de datos recogidos por la linea de comandos son incorrectos: :samp:`main.py -t 4`, por defecto *4* será tratado como un string, no como un :samp:`int`.
+ Ausencia de opciones por defecto.
+ Establecer ciertas opciones como obligatorios.
+ Establecer un opciones y una versión abreviada de las mismas: :samp:`main.py -t 8` equivalente a :samp:`main.py --threads 8`.
+ Opciones sin parámetros, tratados como :samp:`bool`: :samp:`main.py -j`.
+ Opciones que puedan usarse como acumuladores: :samp:`main.py -v` -> :samp:`main.py -vv` -> :samp:`main.py -vvv`.


Solución
********

En este caso de prueba la solución no es otra que usar correctamente la libraría de Python :samp:`argparse`

Cómo
****

Para que sea más ilustrativo, vamos a partir de una linea de comandos básica y vamos ir mejorándola poco a poco.

La linea de comandos de la que partiremos la que sigue, de un posible escaneador de puertos:

`Ejemplo ST-005.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/st/005/st-005-p1.py>`_

.. literalinclude:: ../../../../examples/develop/st/005/st-005-p1.py
    :lines: 26-
    :linenos:

Que mostrará el siguiente resultado por consola, cuando ejecutamos :samp:`st-005-p1.py -h`:

.. code-block:: bash

    usage: st-005-p1.py [-h] [-t TARGETS] [-v VERBOSITY LEVEL] [--open ONLY_OPEN]
                    [-p PORTS_RANGE]

    OMSTD Example

    optional arguments:
      -h, --help          show this help message and exit
      -t TARGETS          target
      -v VERBOSITY LEVEL
      --open ONLY_OPEN    only display open ports
      --port PORT

.. note::

    Nótese que se puede ejecutar sin parámetros y no se devolvería ningún error a pesar de que, por razones obvias, necesitamos como mínimo un parámetros: *targets*.


1 - Opciones obligatorios
+++++++++++++++++++++++++

En primer lugar vamos a solventar el problema del parámetro obligatorio y vamos a obligar a especificar un *target*:

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-t", dest="targets", help="target", required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level', type=int)
    parser.add_argument("--open", dest="only_open", help="only display open ports", default=0)
    parser.add_argument("--port", dest="port", type=int, help="port to scan")

    params = parser.parse_args()

Vemos cómo, tras en cambio, se obliga al usuario a especificar un *target*:

.. code-block:: bash

    usage: st-005-p1.py [-h] -t TARGETS [-v VERBOSITY LEVEL] [--open ONLY_OPEN]
                        [-p PORTS_RANGE]
    st-005-p1.py: error: the following arguments are required: -t

2 - Tipos de datos
++++++++++++++++++

Vemos que las opciones *verbosity* (0-2) y *port* son tratadas como *string* (por defecto), pero realmente son del tipo :samp:`int`.

Añadimos la mejora:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-t", dest="targets", help="target", required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level', type=int)
    parser.add_argument("--open", dest="only_open", help="only display open ports", default=0)
    parser.add_argument("--port", dest="port", type=int, help="port to scan")

    params = parser.parse_args()

3 - Valores por defecto
+++++++++++++++++++++++

Sería interesante contar con valores por defecto para cada tipo de parámetro.

De esta forma evitaremos errores, por ausencia de dichos valores por parte del usuarios, e introduciremos configuración predeterminada, lo que hará el uso de la herramienta más fácil:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3-6

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-t", dest="targets", help="target", required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level', type=int, default=0)
    parser.add_argument("--open", dest="only_open", help="only display open ports", default=0)
    parser.add_argument("--port", dest="port", type=int, default=80,
        help="port to scan. Default: 80.")

    params = parser.parse_args()

4 - Opciones sin parámetros
+++++++++++++++++++++++++++

Si observamos, la opción *--open*, es realmente un booleano. Es decir, que solo necesitamos saber si está a :samp:`True` o a :samp:`False`.

Actualizamos para que dicha opción sea tratada como un booleano.

.. code-block:: python
    :linenos:
    :emphasize-lines: 4,5

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-t", dest="targets", help="target", required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level', type=int, default=0)
    parser.add_argument("--open", dest="only_open", action="store_true",
        help="only display open ports", default=False)
    parser.add_argument("--port", dest="port", type=int, default=80,
        help="port to scan. Default: 80.")

    params = parser.parse_args()

.. note::

    Los datos booleanos no necesitan indicarles el tipo, cuando se usan con la opción :samp:`action="store_{true|false}`. El tipo está implícido cuando usamos el parámetro de configuración :samp:`action="store_XXXX"`.


5 - Opciones abreviadas
+++++++++++++++++++++++

Cuando tenemos muchas opciones en la linea de comandos, es intersante poder poner la opciones en formato más abrevidado.

Para nuestro ejemplo, cuando indicamos del puerto, podríamos crear la opción abreviada :samp:`-p`, además de :samp:`--port` como sigue:

.. code-block:: python
    :linenos:
    :emphasize-lines: 5,6

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-t", dest="targets", help="target", required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level', type=int, default=0)
    parser.add_argument("--open", dest="only_open", action="store_true",
        help="only display open ports", default=False)
    parser.add_argument("-p", "--port", dest="port", type=int, default=80,
        help="port to scan. Default: 80.")

    params = parser.parse_args()

6 - Opciones auto-incrementales
+++++++++++++++++++++++++++++++

Existen ciertas opciones que tienen más sentido que su valor vaya incrementando en función de las veces que se repite. Por ejemplo:

+ :samp:`-v` en lugar de *0*.
+ :samp:`-vv` en lugar de *1*.
+ :samp:`-vvv` en lugar de *2*.

En nuestro ejemplo, dicho comportamiento es perfecto para el opación *verbosity*:


.. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-t", dest="targets", help="target", required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level: -v, -vv, -vvv.',
        action="count", type=int, default=0)
    parser.add_argument("--open", dest="only_open", action="store_true",
        help="only display open ports", default=False)
    parser.add_argument("-p", "--port", dest="port", type=int, default=80,
        help="port to scan. Default: 80.")

    params = parser.parse_args()

7 - Opciones posicionales
+++++++++++++++++++++++++

Por último, puede que nos interese tener parámetro qeu no van precedidos de ninguna opción que empiece por *-*. Por ejemplo:

+ :samp:`main.py 127.0.0.1` en lugar de :samp:`main.py -t 127.0.0.1`.

Esta forma de configurar las opciones de la linea de comandos se conoce como *opciones posicionales*.

Entenderemos mejor esto con un ejemplo:

.. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("targets", metavar='TARGETS', help="targets to scan", nargs="+",
        required=True)
    parser.add_argument('-v', dest='verbosity' help='verbosity level: -v, -vv, -vvv.',
        action="count", type=int, default=0)
    parser.add_argument("--open", dest="only_open", action="store_true",
        help="only display open ports", default=False)
    parser.add_argument("-p", "--port", dest="port", type=int, default=80,
        help="port to scan. Default: 80.")

    params = parser.parse_args()

La linea de comando ahora se verá así:

.. code-block:: bash

    usage: st-005-s1.py [-h] [-v] [--open] [-p PORT] TARGETS [TARGETS ...]

    OMSTD Example

    positional arguments:
      TARGETS               targets to scan

    optional arguments:
      -h, --help            show this help message and exit
      -v                    verbosity level: -v, -vv, -vvv.
      --open                only display open ports
      -p PORT, --ports PORT
                            port to scan. Defaul: 80.

Una ver parseada la linea de comandos, en el objeto :samp:`params`, podremos obtener la lista de los parámetros posicionales leyendo el parámetro :samp:`params.targets`.

8 - Documentación extendida
+++++++++++++++++++++++++++

Suele ser muy útil para nuestros programas poner pequeños ejemplos al final de la ayuda que nos proporciona la opción *-h*. Para esto, usamos el parámetro *epilog*, del módulo :samp:`argparse`:

`st-005-s1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/005/st-005-s1.py>`_:

.. literalinclude:: ../../../../examples/develop/st/005/st-005-s1.py
    :linenos:
    :lines: 29-
    :emphasize-lines: 13-14

Este es el aspecto que tendría al ejecutar :samp:`st-005-s1.py -h`:

.. code-block:: bash

    usage: st-005-s1.py [-h] [-v] [--open] [-p PORT] TARGETS [TARGETS ...]

    OMSTD Example

    positional arguments:
      TARGETS               targets to scan

    optional arguments:
      -h, --help            show this help message and exit
      -v                    verbosity level: -v, -vv, -vvv.
      --open                only display open ports
      -p PORT, --ports PORT
                            port to scan. Defaul: 80.

    Usage examples:
        + Basic scan:
            st-005-s1.py 127.0.0.1
        + Specifing port to test:
            st-005-s1.py -p 443 127.0.0.1
        + Only diplay open ports
            st-005-s1.py -p 139 127.0.0.1
