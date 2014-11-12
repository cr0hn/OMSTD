Redistribución
==============

En este bloque se tratan los casos de estudio relacionados con la redistribución del software y las diferentes formas de hacerlo:

* Sistemas de control de versiones y correcto uso.
* Creación de paquetes.
* Inclusión en repositorios públicos.
* Creación de binarios.
* Portabilidad entre sistemas.

----

.. _rd-001:

RD-001 - Inclusión de dependencias externas
-------------------------------------------

Problema
********


Mi proyecto tiene dependencias y no se cómo hacer que sean fácilmente instalables para que se puede redistribuirlos de forma sencilla.

Solución
********

Usar `pip <https://pypi.python.org/pypi>`_ + el fichero `requirements.txt <http://pip.readthedocs.org/en/latest/user_guide.html#requirements-files>`_.

* Pip es un gestor de paquetes Python, al más puro estilo "apt-get" de Debian.
* requirements.txt: Fichero donde se detallan todas las dependencias del proyecto.

Cómo
****

En este link se puede encontrar el ejemplo: `Ejemplo requirements.txt <https://github.com/cr0hn/OMSTD/blob/master/examples/develop/rd/001/requirements.txt>`_

Para instalar todas las dependencias usando pip:

.. code-block:: bash

    pip -r requirements.txt

----

.. _rd-002:

RD-002 - Sandbox y entornos virtuales
-------------------------------------

Problema
********


Las dependencias entre proyectos y tener que instalarlo todo en el sistema lo "ensucia" y hace que todo sea un caos.

Solución
********

Usar `virtualenv <https://virtualenv.pypa.io/en/latest/virtualenv.html>`_:

* Virtualenv: es una "sandbox" donde se instalarán todas las dependencias de tu software.
* Además, podemos usar `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_, para añadir más funcionalidad y utilidades a virtualenv.

Cómo
****

Instalar virtualenwrapper
+++++++++++++++++++++++++

.. note::

    Virtualenvwrapper incluye el paquete "virtualenv"

.. code-block:: bash

    pip install virtualenvwrapper

Crear un virtualenv
+++++++++++++++++++

.. code-block:: bash

    mkvirtualenv tutorial

Crear un virtualenv temporal
++++++++++++++++++++++++++++

.. code-block:: bash

    mktmpenv tutorial_tmp

Salir del virtualenv
++++++++++++++++++++

.. code-block:: bash

    deactivate