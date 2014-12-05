Específicos del lenguaje
========================

En este bloque se tratan los casos de estudio relacionados con los aspectos específicos del lenguaje Python:

+ Trucos
+ Buenas prácticas
+ Consejos
+ Nuevas características introducidas por Python 3

----

.. _lp-001:

LP-001 - Tareas no bloqueantes
------------------------------

Problema
********


Python es mucho más lento que otros frameworks o lenguajes, como nodejs, que usa conexiones no "bloqueantes" o "corrutinas".

.. note::

    ¿Qué es una **corrutina** (coroutine en inglés)?

    Una `corrutina <http://en.wikipedia.org/wiki/Coroutine#Implementations_for_Python>`_ es una compontente (función, clase o método) capaz de suspender su ejecución hasta recibir un cierto estímulo:

    .. image:: ../../../images/lp-001.01.png


Solución
********

Desde Python 3.4 existen lo que se llaman "corrutinas" a través de la librería, incluida en el framework 3.4, asyncio (también conocido como `Tulip <https://code.google.com/p/tulip/>`_).

Cómo
****

`Ejemplo LP-001.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/001/lp-001-p1.py>`_

Este ejemplo muestra como descargar el contenido de una URL, usando la **librería estándar** de Python 3.4:

.. literalinclude:: ../../../../examples/develop/lp/001/lp-001-p1.py
    :lines: 24-
    :linenos:
    :emphasize-lines: 8

`Ejemplo LP-001.S01 <../../../../../../examples/develop/lp/001/lp-001-s1.py>`_

En el siguiente podemos ver cómo, usando `Tulip <https://code.google.com/p/tulip/>`_ y la librería `aiohttp <https://github.com/KeepSafe/aiohttp>`_, podemos hacer peticiones no bloqueantes muy fácilmente:

.. literalinclude:: ../../../../examples/develop/lp/001/lp-001-s1.py
    :lines: 25-
    :linenos:
    :emphasize-lines: 1,6,8-9,17-18

.. note::

    **aioHTTP** es una librería independiente, construida usando asyncIO a bajo nivel, y que nos facilitará el manejo de conexiones HTTP.

----

.. _lp-002:

LP-002 - Multithreading y procesamiento paralelo
------------------------------------------------

Problema
********


Python no tiene hilos ni multithreads real debido al `GIL <https://wiki.python.org/moin/GlobalInterpreterLock>`_ (Global Interpreter Lock). Éste restringe la ejecución a un único hilo corriendo a la vez. Esto es así porque, cuando se diseñó python, se prefirió que el motor fuera más simple su implementación, a costa de sacrificar la eficiente.

.. note::

    Para entender mejor cómo funciona el GIL, se recomienda al lector las charlas y estudios de `David Beazley <http://www.dabeaz.com/GIL/>`_.

Solución
********

Esto es cierto y no se puede hacer nada a día de hoy. Es el modo de funcionamiento de la VM de Python por defecto, CPython, no se puede lograr, multithreading real.

La solución, para lograr la `ejecución pararela <http://www.haskell.org/haskellwiki/Parallelism_vs._Concurrency>`_ en Python, es usar multiprocessing.

.. note::

    Existen otras implementaciones de la máquina virtual de Python: `Diferentes implementaciones de la máquina virtual de PYthon <http://en.wikipedia.org/wiki/Python_(programming_language)#Implementations>`_

    En el resto de implementaciones SI que existe el mutithread real, pero **tienen multitud de incompatibilidades** y no es recomendable su uso para propósito general.

Cómo
****

`Ejemplo LP-002.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/002/lp-002-p1.py>`_

El siguiente código muestra un ejemplo típico de multithreading en Python, en el que solo puede haber **10 threads** en ejecución concurrente (que no paralela) a la vez:

.. literalinclude:: ../../../../examples/develop/lp/002/lp-002-p1.py
    :lines: 23-
    :linenos:
    :emphasize-lines: 3

`Ejemplo LP-002.S01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/002/lp-002-s1.py>`_

El siguiente ejemplo muestra el mismo resultado, pero con multiprocessing:


.. literalinclude:: ../../../../examples/develop/lp/002/lp-002-s1.py
    :lines: 25-
    :linenos:
    :emphasize-lines: 1,11


.. note::

    El código anterior, además de ser multiproceso real, tiene las ventajas:

    * Al usar CTRL+C funcionará correctamente.
    * Usar una librería del framework, que gestiona internamente, un pool de procesos. Con esto evitamos tener que llevar el control manual del número de procesos concurrentes que pueden ejecutarse.


----

.. _lp-003:

LP-003 - Callback, número de parámetros y partials
--------------------------------------------------

Problema
********

Cuando usamos librerías externas o de terceros, tenemos que adaptarnos a su API, pero no siempre es fácil. Supongamos la siguiente situación:

Tenemos una función que ha de invocarse con 3 parámetros a través de un callback externo, pero este callback solo pasa uno de los parámetros requeridos por nuestra función. Con un ejemplo se verá mejor:

#. Tenemos una librería, llamada :samp:`external.api`, de la que queremos ejecutar una función :samp:`action_with_callback` y cuyo código es:

    `external/api.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/003/external/api.py>`_

    .. literalinclude:: ../../../../examples/develop/lp/003/external/api.py
        :linenos:
        :lines: 25-
        :emphasize-lines: 1,8

#. En nuestro código queremos ejecutar diferentes acciones, en función lo que el usuario indice en la linea de comandos, pero no podemos por el modo de funcionamiento del API externo: No podemos pasar como parámetro la operación y el primer dato:

    `lp-003-p1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/003/lp-003-p1.py>`_

    .. literalinclude:: ../../../../examples/develop/lp/003/lp-003-p1.py
        :linenos:
        :lines: 24-
        :emphasize-lines: 18,19,21

Solución
********

Usar los `partials <https://docs.python.org/2/library/functools.html#functools.partial>`_ de Python.

Un *partial* en una función que se puede construida por partes, dejando una parte fija y otra variable. Siguiendo con el ejemplo anterior:

    #. deberíamos dejar como parte "fija":

        + La operación a realizar
        + El primer dato

    #. Y como parte variable, el valor que devuelva el callback.

Es decir, que a partir de la primera función :samp:`actions(operation, data1, data2)`, tenemos que generar una segunda con un solo parámetro:

:samp:`actions(operation, data1, data2)` -> TRANSFORM -> :samp:`new_actions(data2)`

Cómo
****

Para construir un *partial* en Python es muy sencillo, para ello debemos usar la librería :samp:`functools`:

`lp-003-s1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/003/lp-003-s1.py>`_

.. literalinclude:: ../../../../examples/develop/lp/003/lp-003-s1.py
    :linenos:
    :lines: 24-
    :emphasize-lines: 1,3,23,25


----

.. _lp-004:

LP-004 - "__main__" y ejecuciones accidentales
----------------------------------------------

Problema
********

Cuando Python se invoca, por como está concebido, lee y ejecuta todas los los ficheros y dependencias.

Esto puede implicar:

+ Llamadas accidentales a métodos, funciones o variables.
+ Al no saber el orden exacto de carga de cada fichero, puede provocar errores muy difíciles de detectar.

Por ejemplo:

`lp-004-p1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/004/lp-004-p1.py>`_

.. literalinclude:: ../../../../examples/develop/lp/004/lp-004-p1.py
    :linenos:
    :lines: 27-
    :emphasize-lines: 10,17

Como podemos ver en el ejemplo, la clase con el listado de números debería de ejecutarse y cargarse antes, pero no podemos estar seguros. Ello depende de la implementación de la máquina virtual de Python.

Es sencillo imaginar por el lector que ocurriría si el orden de carga no fuera el "natural": Se produciría una condición de carrera y nuestro código fallaría. Las condiciones de carrera son sumamente complicadas de detectar.

Solución
********

Usar la "etiqueta" :samp:`__name__` para indicar que dicha sección contiene el punto de entrada principal, o función *main*, a nuestra aplicación.

Cómo
****

En el siguiente código podemos apreciar que el cambio es mínimo. Con este sencillo cambio nos ahorraremos multitud de problemas:

`lp-004-s1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/004/lp-004-s1.py>`_

.. literalinclude:: ../../../../examples/develop/lp/004/lp-004-s1.py
    :linenos:
    :lines: 27-
    :emphasize-lines: 17


.. _lp-005:

LP-005 - Apertura, cierre y olvidos en descriptores
---------------------------------------------------

Problema
********

Cuando trabajamos con *handlers* (o descriptores) ya sean de archivo, red o de cualquier otro tipo, sobre ellos hay 3 acciones que siempre llevaremos a cabo:

#. Apertura del descriptor.
#. Uso del descriptor
#. Cierre del descriptor.

El paso 3, *cierre del descriptor*, es uno de los grandes olvidados por:

+ Se omite por descuido del programador.
+ No se cierra adecuadamente: a causa de algún problema y errores.

Esto dejará descriptores de sistema abiertos y huérfanos, ocupando recursos del sistema operativo y degradando el rendimiento

El siguiente ejemplo ilustra esta situación:

`lp-005-p1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/005/lp-005-p1.py>`_

.. literalinclude:: ../../../../examples/develop/lp/005/lp-005-p1.py
    :linenos:
    :lines: 25-
    :emphasize-lines: 9,10

Como se puede ver, en el ejemplo se crean 100 archivos temporales pero no se cierran.


Solución
********

Python dispone de la palabra reservada :samp:`with` que se asegurará de:

+ Garantizar una sintaxis sencilla y legible.
+ Cerrar el descriptor, y re-intentando o forzando su cierre cuando sea necesario.

:samp:`with` **funciona también con sockets, acceso a bases de datos, o cualquier** `estructura compatible <https://docs.python.org/3.4/library/contextlib.html#contextlib.ContextDecorator>`_.

Cómo
****

Para usar :samp:`with` tan solo tendremos usar la sintaxis:

.. code-block:: python
    :linenos:

    with open("...", ".") as f:
        # ACTIONS
        f.write("my text")

Donde:

+ "**f**"  será el descriptor de fichero que usaremos en nuestro código.
+ Cualquier acceso que tengamos que hacer sobre el fichero solo podremos hacerlo debajo del bloque del :samp:`with`.

**En el momento que la ejecución del bloque finalice, el descriptor se cerrará automáticamente por la VM de Python**

Aquí podemos ver el ejemplo anterior usando :samp:`with`:

`lp-005-s1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/005/lp-005-s1.py>`_

.. literalinclude:: ../../../../examples/develop/lp/005/lp-005-s1.py
    :linenos:
    :lines: 25-
    :emphasize-lines: 9,10

----

.. _lp-006:

LP-006 - import relativos, absolutos, paquetes y demás hierbas
--------------------------------------------------------------

Problema
********

Cuando desarrollamos en Python es muy habitual toparnos rápidamentente con mensajes como:

.. code-block:: bash

    ...
    ValueError: Attempted relative import in non-package

.. code-block:: bash

    ...
    SystemError: Parent module '' not loaded, cannot perform relative import

Estos errores son muy abituales en Python 3.x. Esto es debido a que se está tratando de hacer un :samp:`import` cómo si se tratara de un paquete. Pero... ¿Qué significa esto?


.. note::

    Python 3.4 introdujo cambios en comportamiento interno cuando importa módulos y dependencias.

    Puede leer más sobre este tema consultando el `PEP-0366 <https://www.python.org/dev/peps/pep-0366/>`_.

    Se recomienda la lectura del post de `taherh <http://stackoverflow.com/users/811556/taherh>`_ en StackOverFlow: http://stackoverflow.com/a/6655098 , sobre este tema.


Un par de conceptos:

Concepto: Paquete
+++++++++++++++++

En Python es un proyecto que puede ser importado, para ser usado como librería.

Éstos deberían tener :samp:`import` relativos, para asegurarse que la librería importada es del propio paquete, y no otra del sistema que tenga el mismo nombre.

Podemos ver la importancia de las rutas relativas en el siguiente ejemplo:

Supongamos que nuestra aplicación de ejemplo `lp-006-p1.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/006/lp-006-p1.py>`_

.. literalinclude:: ../../../../examples/develop/lp/006/lp-006-p1.py
    :linenos:
    :lines: 24-

El ejemplo tiene la estrutura:

.. _lp-006-structure:

.. code-block:: text
    :linenos:
    :emphasize-lines: 2

    lp_006_p1
        \__ random
            \__ __init__.py
        \__ __init__.py
        \__ bad.py
        \__ good.py
    \__ lp-006-p1.py

El paquete random tiene el mismo nombre que el incluido en Python, por lo que si escribimos el siguiente código:

`lp-006-p1/bad.py <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/lp/006/lp-006-p1/bad.py>`_

.. literalinclude:: ../../../../examples/develop/lp/006/lp_006_p1/bad.py
    :linenos:
    :lines: 24-
    :emphasize-lines: 1, 6

Cuantro se trata de mostrar la variable :samp:`HELLO_VAR`, no será encontrada porque realmente estamos importando es el paquete global de Python, y éste no contiene dicha variable. Por tanto se nos mostrará el siguiente error:

.. code-block:: bash

    Traceback (most recent call last):
      File "lp-006-p1.py", line 26, in <module>
        lp_006_p1_fn()
      File "examples/develop/lp/006/lp_006_p1/bad.py", line 30, in lp_006_p1_fn

        print(HELLO_VAR)
    NameError: name 'HELLO_VAR' is not defined


Concepto: Aplicación
++++++++++++++++++++

Una definición informa de aplicación de Python es aquella que usa como programa independiente y que tiene como finalidad ser importado por una aplicación externa.

El fichero que contiene el punto de entrada a la aplicación, o **main**, *no puede usar rutas relativas*.

¿Por qué sucede esto?

Porque el uso de :samp:`import` relativos solo está permitido para paquetes y *han de ser llamados* desde paquetes externos, *no pueden ser lanzados desde el propio paquete* (por defecto).

Es decir, que si tenemos la :ref:`estructura de directorios usada más arriba <lp-006-structure>`, el siguiente código no funcionará:

.. literalinclude:: ../../../../examples/develop/lp/006/lp-006-p1.py
    :linenos:
    :lines: 25-
    :emphasize-lines: 1, 6

Y nos devolverá el error:

.. code-block:: bash

    File "lp-006-p2.py", line 24, in <module>
       from .lp_006_p1.good import *
    SystemError: Parent module '' not loaded, cannot perform relative import

A modo de resumen: **No funciona porque se está usando una aplicación como un paquete**.


Solución
********

Por su puesto existen soluciones para ambos casos. A modo de conceptual son los siguientes:

Paquetes
++++++++

Usar :samp:`import` relativos, en lugar de absolutos, cuando queramos importar paquetes locales y que éstos no se confundan con los globales u otros que podamos tener instalados.

Aplicación
++++++++++

Hay ocasiones en los que querremos usar una aplicación como un paquete como, por ejemplo:

Cuando queramos crear un paquete que, además, pueda ser usado como aplicación.

La solución: **forzar la aplicación a que se comporte como un paquete**.

Cómo
****


Paquetes
++++++++

La solución es la impotanción relativa o, lo que es lo mismo, **indicar a Python que use el paquete local en lugar del global del sistema**:

.. literalinclude:: ../../../../examples/develop/lp/006/lp_006_p1/good.py
    :linenos:
    :lines: 25-
    :emphasize-lines: 1, 6

.. code-block:: bash

    hello!

Aplicación
++++++++++

Transformar una aplicación en un paquete no es nada intuitivo ni trivial. Tendremos que tener controlar:

+ Detectar si la aplicación es parte de un paquete o no.
+ Mover los :samp:`import` de la parte global al ámbido de la función que haga de punto de entrada. Es ha de ser así para que, cuando el intérprete de Python importe todo el código no ejecute ni cargue ninguna librería hasta que no hayamos transformado la aplicación en paquete.

El siguiente código solucionará nuestro problema:

.. literalinclude:: ../../../../examples/develop/lp/006/lp-006-s2.py
    :linenos:
    :lines: 24-
    :emphasize-lines: 2,7-8,11,14,18,20

Explicación line a linea:

+ **1**: Detectamos si el fichero es el punto de entrada a la aplicación (:samp:`main`) y si es un paquete.
+ **7-8**: Cargamos el directorio desde el que es llamado el programa en la lista de paquetes disponibles de Python.
+ **11**: Una vez añadido en el entorno de Python el directorio donde se encuentra nuestro fichero, cargamos el paquete padre, el que contiene el ejecutable, o .py.
+ **14**: Establecemos la variable de entorno :samp:`__package__`, indicándole a Python que si que existe un paquete.
+ **18**: Cargamos nuestra librerías con :samp:`import` relativos. Ahora ya no tendremos problemas.
+ **20**: Continuamos la ejecución de nuestro código, como lo haríamos normalmente.


