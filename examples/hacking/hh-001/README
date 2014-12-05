What's this project?
====================

This project is a basic port scanner. It belongs to OMSTD Project (https://github.com/cr0hn/OMSTD).

Licence
=======

This project is **BSD**... Copy it! And, if you remember, please mention me in credits :)

How to install
==============

.. code-block:: bash

    sudo python3.4 -m pip install OMSTD-hh-001

How use it?
===========

You can use this project as a command line tool or as a library, as part of your Python projects.

As a tool
---------

You can display all options to run as command line running command :samp:`omstd-hh-001 -h`:

.. code-block:: bash

    usage: omstd-hh-001 [-h] [-v VERBOSITY] [--open] [-p PORTS_RANGE] [-r]
                        [--proxy PROXY]
                        TARGETS [TARGETS ...]

    OMSTD Example

    positional arguments:
      TARGETS         targets to scan

    optional arguments:
      -h, --help      show this help message and exit
      -v VERBOSITY    verbosity level
      --open          only display open ports
      -p PORTS_RANGE  port range to scan in format 'X-Y'. Defaul: 1-1024.
      -r              don't randomize ports
      --proxy PROXY   proxy in format: http://USER:PASS@IP:PORT

As a library
------------

.. code-block:: python

    from omstd_hh_001.api import run_scan, Parameters

    if __name__ == "__main__":


        input_parameters = Parameters(ports_range="1-2049",
                                      targets=["127.0.0.1", "127.0.0.2"],
                                      verbosity=2,
                                      random_port_scan=True,
                                      only_open=True,
                                      proxy=None)
        
        results = run_scan(config)

        # Display open ports
        for port, status in results.ports.items():

            # Checks if 'only_open' is set -> Only display port with status 'open'
            if input_parameters.only_open is True and status == "closed":
                continue

            print("%s/tcp %s" % (port, status))
        
        # Display scan time
        print(results.scan_time)