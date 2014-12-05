# -*- coding: utf-8 -*-

"""
Project name: hh-001
Project URL: https://github.com/cr0hn/the_open_shortener

Copyright (c) 2014, cr0hn<-AT->cr0hn.com
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

__author__ = 'cr0hn - cr0hn<-at->cr0hn.com (@ggdaniel)'

import asyncio

from random import randint

from .data import Parameters


# ----------------------------------------------------------------------
@asyncio.coroutine
def _scan_tcp_ports(target, input_params, loop, results):
    """
    Routine to scan a targer

    :param target: target system
    :type target: str

    :param input_params: Parameters object
    :type input_params: Parameters

    :param loop: Event loop object
    :type loop: EventLoop

    :param results: Future object to save resutls
    :type results: Future

    """

    ports = {}  # {PORT: STATUS}

    for port in input_params.ports_range:

        # Debug
        if input_params.verbosity > 2:
            input_params.print_function("Trying port %s/tcp on %s" % (port, target))

        writer = None
        try:
            reader, writer = yield from asyncio.open_connection(target, port, loop=loop)
            ports[port] = "open"

            # Debug
            if input_params.verbosity > 2:
                input_params.print_function("Discovered open port %s/tcp on %s" % (port, target))

        except ConnectionRefusedError as e:
            ports[port] = "closed"
        finally:
            if writer:
                writer.close()

    results.set_result(ports)


# ----------------------------------------------------------------------
def scan_tcp_ports(target, config):
    """
    Scan TCP ports

    :param config: Parameters object
    :type config: Parameters

    :return: dictionary with port number and their state: {PORT_NUMBER: STATE}
    :rtype: dict(int: str)

    """
    if not isinstance(config, Parameters):
        raise TypeError("Expected Parameters, got '%s' instead" % type(config))

    try:
        # Set future to get restuls
        results = asyncio.Future()

        # Call scanner
        loop = asyncio.get_event_loop()
        loop.run_until_complete(_scan_tcp_ports(target, config, loop, results))

        return results.result()
    except KeyboardInterrupt:
        config.print_function("[*] shutdowning... ")
        exit()