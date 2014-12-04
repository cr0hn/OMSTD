.. OMSTD documentation master file, created by
   sphinx-quickstart on Mon Oct 13 22:59:01 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenido a OMSTD (Open Methodology for Security Tool Developers)
==================================================================


.. figure:: ../../images/logo_200x200.png
    :align: left

OMSTD (Open Methodology for Security Tool Developers) es una serie de casos de estudio, agrupados y categorizados a modo de guía, con los que lograr desarrollar herramientas bien construidas.

Aunque puede ser usada para crear cualquier tipo de herramientas y en cualquier lenguaje, se centra principalmente en el desarrollo de herramientas de hacking escritas en Python.

Sería muy recomendable para el lector **leer detenidamente la sección** :ref:`Qué es OMSTD <start>` **, ya que le ayudará a comprender esta guía**.

Autor
-----

Esta guía ha sido escrita e ideada por `Daniel García (A.K.A. cr0hn) <http://cr0hn.com/me/>`_.

Web oficial y Twitter
---------------------

Esta guía, así como su código de ejemplo y presentaciones están publicadas de forma **gratuita** en su repositorio de Github: 

  `https://github.com/cr0hn/omstd <https://github.com/cr0hn/omstd>`_

Puedes seguir los avances, novedades y noticias de esta guía en nuestra cuenta de twitter:

  `@OMSTD_project <https://twitter.com/OMSTD_project>`_

Licencias
---------

Código
++++++

Todo el código aquí expuesto se distribuye bajo `licencia BSD 3-clausule <http://opensource.org/licenses/BSD-3-Clause>`_. Puedes copiarlo y redistribuirlo sin restricción, conservando la autoría del mismo y sin obtener beneficio económico directo del mismo.

Texto
+++++

Esta guía, y todo el texto que la contiene, se distribuye bajo la licencia: `Creative Commons 4.0 - Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) <http://creativecommons.org/licenses/by-nc/4.0/>`_.

Colaborar con OMSTD
-------------------

Cualquier idea, crítica (constructiva, por favor) o colaboración es muy bienvenida. Puedes ponerte en contacto por las vías:

+ Correo electrónico (cr0hn<<--AT-->>.cr0hn.com).
+ Usando los issues de github.
+ Haciendo un fork de proyecto y enviando un parche.

Si estás interesado en ayudar, puedes echar un vistazo a `TODO.rst <https://github.com/cr0hn/OMSTD/blob/master/TODO.rst>`_ y ver las ideas pendientes de implementar.

Una de las finalidades es portar esta guía a otros idiomas. **SI DOMINAS CUALQUIER OTRO IDIOMA ADEMÁS DEL ESPAÑOL, ANÍMATE A ECHAR UNA MANO**.

¿A quién va dirigida esta guía?
-------------------------------

Esta guía está dirigida a auditores de seguridad y *pentesters* que necesitan desarrollar sus propias herramientas (muchas veces *on-the-fly*) y quieren que éstas sean algo más que un simple script.

Un *pentester* puede ser muy bueno en tareas de hacking, pero no tiene porque tener tanto conocimiento en desarrollo, buenas prácticas, patrones de diseño, etc.

**Para poder usar esta guía se recomienda:**

+ Tener conocimientos básicos de programación en Python 3 (**Si solo sabes Python 2, también podrás seguir la guía**, no te preocupes).
+ Tener conocimientos básicos de seguridad informática


Organización de la guía
-----------------------

Bloques
+++++++

Los casos de estudio se dividen en los siguientes bloques:

.. _categories:

+ Desarrollo

  + **Organización y estructura (ST)**: Cómo se organizan los proyectos.
  + **Comportamiento (BH)**: Forma de interactuar con diferentes frameworks.
  + **Interacción (IT)**: Interacción de usuario, con otros sistemas o con otros entornos.
  + **Específico de lenguaje (LS)**: Trucos, buenas prácticas y usos concretos del lenguaje de desarrollo. Python en este caso.
  + **Entrada/salida de información (IO)**: Generar de informes (Word, Excel...), exportar datos, importar información externa de XML/JSON...
  + **Redistribución (RD)**: Crear de paquetes, redistribuirlos, compilarlos para varios sistemas, portarlos a varios entornos, uso correcto de sistemas de control de versiones, etc.
  + **Despliegue (DP)**: Cómo poner en producción de forma correcta nuestra aplicación.

+ **Hacking** (HH): Ejemplos de casos concretos de hacking.
+ **Cracking** (CH): Ejemplos de casos concretos de cracking.
+ **Malware** (MH): Ejemplos de casos concretos de malware.
+ **Forensic** (FH): Ejemplos de casos concretos de forensic.
+ **Hardening** (DH): Ejemplos de casos concretos de hardening.

Identificación de los casos
+++++++++++++++++++++++++++

A fin de hacer más re-usable este texto, se identificarán los casos de la siguiente forma:

    + XX[-EX]-YYY

      + **Problema**: Presentación y descripción del caso de estudio.
      + **Solución**: Solución propuesta.
      + **Cómo**: Cómo llevar a cabo la solución.
      + **Anexo**: Esta sección puede estar disponible o no. En ella se aclararán cuestiones muy concretas del caso de estudio.

Donde:
    + **XX** : Identificador de bloque.
    + YYY: Valor numérico con el formato: 001, 002, 003...
    + EX: Si el identificador tiene este sufijo, significa que se trata de un ejemplo completo o mini proyecto.

Índice
------

.. toctree::
   :glob:
   :maxdepth: 2

   start
   develop/index
   hacking/index
   cracking/index
   malware/index
   forensic/index
   hardening/index