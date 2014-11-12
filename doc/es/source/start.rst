Inicio
======

.. _start:

Qué es OMSTD
------------

OMSTD (**O** pen **M** ethodology for **S** ecurity **T** ool **D** evelopers) es una propuesta que intenta ser una guía de buenas prácticas fácil, intuitiva y práctica, para el desarrollo de aplicaciones de hacking.

Hacer herramientas de hacking no tiene porque ser tan complicado como puede parecer a priori, tan solo hay que seguir una serie de pautas de forma correcta.

Esta guía surge a partir de mi charla **"El Poder de los reptiles: Cómo hacer herramientas de seguridad en Python"** en `IV Navaja Negra Conference <http://navajanegra.com>`_.

El objetivo de este proyecto es crear una metodología abierta y colaborativa con la que poder servir de apoyo al desarrollo de nuevas herramientas.

Estado actual
-------------

Actualmente esta guía recoje un número bastante limitado de casos. Hay mucho por hacer y muchas ideas por documentar.

Poco a poco, y con la ayuda de todo el que quiera contribuir, espero que el número de casos de estudio y ejemplos crezca.

¡¡Aviso!!
---------

Este texto es fruto de la experiencia, investigación propia y de los errores más comunes que me he encontrado cuando he tratado de desarrollar herramientas de hacking o usar otras en mi propio código.

El objetivo de este texto es ser una pequeña guía de buenas prácticas (y que espero ampliar en un futuro) para la creación de herramientas portables, bien diseñadas y mantenibles.

**Las soluciones presentadas pueden no ser las mejores o más óptimas, son solo mis propuestas**. Cualquier mejora o sugerencia es bienvenida.


Cómo usar esta guía
-------------------

Teoría
++++++

Si es la primera vez que lees esta guía, te recomiendo que la leas los casos de estudio en el orden que están planteados.

Una vez estudiado y familiarizado con ellos tan solo tendrás que buscar el caso específico que necesites.

Ejemplos
++++++++

Todos los ejemplos se encuentran colgando del directorio **examples**. En él podrás encontrar una serie de carpetas que coinciden con los códigos de los bloques (:ref:`mirad más abajo <categories>` ) y una sub-carpeta con valores numéricos de 3 dígitos, que corresponde con un caso de estudio concreto+, por ejemplo:

.. code-block:: bash

    example/bh/001/


Corresponderá con el **caso de estudio 001** del **tipo comportamiento** (BH).

.. _getting-started:

Instrucciones para empezar
--------------------------

Al igual que se explica en esta guía, ella misma está estructurada siguiendo el mismo modelo que plantea.

Tal vez sea adelantar acontecimientos pero, para ponértelo más fácil, estas son las instrucciones que deberías de seguir para poder ejecutar todos los casos de estudio:

1 - Instalar las dependencias de sistema
++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    sudo python3.4 -m pip install virtualenvwrapper

2 - Configurar virtualenvwrapper
++++++++++++++++++++++++++++++++

.. code-block:: bash

    echo "export WORKON_HOME=$HOME/.virtualenvs" > ~/.bashrc
    echo "export PROJECT_HOME=$HOME/Devel" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh"  >> ~/.bashrc

3 - Buscar el intérprete de Python 3.4
++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    locate python3.4 | grep bin/python | grep python3

.. code-block:: console

      ...
      /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4
      /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4-config
      /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4m
      /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4m-config
      /opt/local/bin/python3.4
      /opt/local/bin/python3.4-config
      /opt/local/bin/python3.4m

4 - Crear el entorno virtual (o sandbox) de pruebas
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: bash

    mkvirtualenv -p /opt/local/bin/python3.4 omstd

5 - Instalar las dependencias globales de OMSTD
+++++++++++++++++++++++++++++++++++++++++++++++

Situados en el directorio raiz del proyecto de OMSTD ejecutamos:

.. code-block:: bash

    pip install -r requirements.txt

6 - Instalar las dependencias locales de cada ejemplo
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Cada caso de estudio puede tener su propio fichero **requirements.txt** con sus propias dependencias. Esto es así para no obligar al lector a instalar todas las dependencias del proyecto, ya que puede que no las necesite todas.

Para instalar las dependencias de cada ejemplo ha de proceder como en el punto anterior con cada fichero listado de dependencias.