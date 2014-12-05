What's this project?
====================

This project is a basic MD5 searcher, using http://md5cracker.org webservice. It belongs to OMSTD Project (https://github.com/cr0hn/OMSTD).

Licence
=======

This project is **BSD**... Copy it! And, if you remember, please mention me in credits :)

How to install
==============

.. code-block:: bash

    sudo python3.4 -m pip install OMSTD-ch-001

How use it?
===========

You can use this project as a command line tool or as a library, as part of your Python projects.

As a tool
---------

You can display all options to run as command line running command :samp:`omstd-ch-001 -h`:

.. code-block:: bash

    usage: omstd-ch-001 [-h] -m PASSWORD [-v VERBOSITY] [-p PROVIDER]
                        [--proxy PROXY] [--list-providers]

    OMSTD Example

    optional arguments:
      -h, --help            show this help message and exit
      -m PASSWORD, --md5 PASSWORD
                            MD5 hashed value to test
      -v VERBOSITY          verbosity level
      -p PROVIDER           select provider used to get cracked MD5 hash. Defaul:
                            all.
      --proxy PROXY         proxy in format: http://USER:PASS@IP:PORT
      --list-providers      list password providers

Providers are the repositories that contains the MD5 <-> plain text information. By default it has the value 'all', but you can list available list running :samp:`omstd-ch-001 --list-providers`:

.. code-block:: bash

    Cracking providers:
      - all (special case. Select all providers)
      - md5cracker.org
      - tmto
      - md5.net
      - md5online.net
      - md5.my-addr.com
      - md5decryption.com
      - md5crack
      - authsecu
      - netmd5crack
      - md5pass
      - i337.net

A complete run: :samp:`omstd-ch-001 -m 5eb63bbbe01eeed093cb22bb8f5acdc3`:

.. code-block:: bash

    [**] Plain text FOUND!!!. Decoded password is ----> hello world <----.

As a library
------------

.. code-block:: python

    from omstd_ch_001.api import Parameters, run_check_md5_hash

    if __name__ == "__main__":

        # Set config
        try:
            input_parameters = Parameters(md5_hash=params.password,
                                          verbosity=params.verbosity,
                                          provider=params.provider,
                                          proxy=params.proxy)
        except ValueError as e:
            print(e)
            exit()

        run_check_md5_hash(input_parameters)

        # Display scan time
        try:
            result = run_check_md5_hash(input_parameters)

            print("[**] Plain text FOUND!!!. Decoded password is ----> %s <----." % result.plain_password)
        except:
            print("[**] Password not found")