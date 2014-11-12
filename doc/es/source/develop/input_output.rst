Entrada / Salida
================

En este bloque se tratan los casos de estudio relacionados con la entrada / salida de información

* Generar de informes: Word, Excel...
* Exportación / importación de información
* Transformación de datos
* Exportar información de forma portable: XML, JSON, YAML...

.. _io-001:

IO-001 - Envío de información por múltiples canales
---------------------------------------------------

Problema
********

Mi aplicación muestra información por pantalla pero he de cambiar mucho código cuando, posteriormente, quiero añadir nuevas funciones en esos mismos puntos nuevas acciones como:

* Añadir niveles de logging.
* Volcar esa misma información a un fichero.
* Enviar esa información a más de una ubicación.

`Ejemplo IO-001.P01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/io/001/io-001-p1.py>`_

Este es el código normal, con un :samp:`print(...)`:

.. literalinclude:: ../../../../examples/develop/io/001/io-001-p1.py
    :lines: 25-
    :linenos:

`Ejemplo IO-001.P02 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/io/001/io-001-p2.py>`_

Vemos realmente el problema cuando queremos añadir más localizaciones donde enviar el texto:

.. literalinclude:: ../../../../examples/develop/io/001/io-001-p2.py
    :lines: 25-
    :linenos:
    :emphasize-lines: 6-7


`Ejemplo IO-001.P03 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/io/001/io-001-p3.py>`_

Y todavía se complica más si queremos añadir niveles de verbosidad:

.. literalinclude:: ../../../../examples/develop/io/001/io-001-p3.py
    :lines: 25-
    :linenos:
    :emphasize-lines: 2,6-8,10-11,16

Solución
********

Usar un objeto estático y global que será el encargado de mostrar la información y que podremos configurar en función de lo que necesitemos.

Cómo
****

Para ello tenemos que declarar una clase estática global, que siga el patrón `Singleton <http://en.wikipedia.org/wiki/Singleton_pattern>`_ en `Python <http://stackoverflow.com/a/1810367>`_, configurarla y llamarla de forma adecuada:

.. note::

    El patrón Singleton nos asegura que solo haya corriendo una instancia de un determinad objeto a la vez.

    Si se crea otra nueva instancia, internamente no creará un nuevo objeto, sino que "rescatará" de la memoria el primer objeto que se creó y se reutilizará.

`Ejemplo IO-001.S01 <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/io/001/io-001-s1.py>`_

.. literalinclude:: ../../../../examples/develop/io/001/io-001-s1.py
    :lines: 25-
    :linenos:
    :emphasize-lines: 2-39,47-48,50,53,59-62
