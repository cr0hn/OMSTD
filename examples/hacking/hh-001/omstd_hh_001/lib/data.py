# -*- coding: utf-8 -*-

"""
Project name: Open Methodology for Security Tool Developers
Project URL: https://github.com/cr0hn/OMSTD

Copyright (c) 2014, cr0hn<-AT->cr0hn.com
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""


__author__ = 'cr0hn - cr0hn<-at->cr0hn.com (@ggdaniel)'


# --------------------------------------------------------------------------
class Parameters:
    """Program parameters"""

    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
        :param ports_range: ports range as string: '1-2000'
        :type ports_range: str
        
        :param targets: list os string with targets 
        :type targets: list(str)

        :param random_port_scan: Select port to scan in random order
        :type random_port_scan: bool

        :param verbosity: verbosity level
        :type verbosity: int

        :param only_open: only manage opened ports
        :type only_open: bool

        :param print_function: function used to display debug info. Default is 'print' call.
        :type print_function: function

        :param proxy: URL with proxy info
        :type proxy: str

        :raises: ValueError
        """
        self.ports_range = kwargs.get("ports_range", "0-1024")
        self.targets = kwargs.get("targets", None)
        self.verbosity = int(kwargs.get("verbosity", 0))
        self.random_port_scan = kwargs.get("random_port_scan", False)
        self.print_function = kwargs.get("print_function", print)
        self.only_open = kwargs.get("only_open", False)

        self.proxy = kwargs.get("proxy", None)
        self.proxy_user = kwargs.get("proxy_user", None)
        self.proxy_pass = kwargs.get("proxy_pass", None)

        if not isinstance(self.ports_range, str):
            raise TypeError("Expected str, got '%s' instead" % type(self.ports_range))
        if not isinstance(self.targets, list):
            raise TypeError("Expected list, got '%s' instead" % type(self.targets))
        else:
            for p in self.targets:
                if not isinstance(p, str):
                    raise TypeError("Expected str, got '%s' instead" % type(p))

        # Remove duplicates
        self.targets = list(set(self.targets))

        # Expand ports
        _total_ports = []
        _parsed_tmp = self.ports_range.strip().split(",")
        for r in _parsed_tmp:
            if "-" in r:
                _parsed_ports = r.strip().split("-")
                if len(_parsed_ports) == 1:
                    _p_start = int(_parsed_ports[0])
                    _p_end = _p_start + 1
                elif len(_parsed_ports) == 2:
                    _p_start = int(_parsed_ports[0])
                    _p_end = int(_parsed_ports[1])
                else:
                    raise ValueError("Port range must be defined as start-end: 1-4025")

                _total_ports.extend(int(x) for x in range(_p_start, _p_end))
            else:
                _total_ports.append(int(r))

        self.ports_range = _total_ports

        if self.proxy is not None:
            from urllib.parse import urlparse

            _scheme = "http" if self.proxy.startswith("http://") or self.proxy.startswith("https://") else ""
            self.proxy = urlparse(self.proxy, scheme=_scheme)


# --------------------------------------------------------------------------
class Results:
    """Program results"""

    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
        :param ports: Port status as format: {PORT_NUMBER: STATUS} 
        :type ports: dict(int: str)
        
        :param scan_time: Time got for scan in miliseconds
        :type scan_time: float

        """
        self.ports = kwargs.get("ports", None)
        self.scan_time = kwargs.get("scan_time", 0)

        # Truncate time
        self.scan_time = '{number:.2f}'.format(number=self.scan_time)
        self.__open_ports = None

    # ----------------------------------------------------------------------
    @property
    def open_ports(self):
        """
        :return: Return only open ports
        :rtype: list(int)
        """
        if self.__open_ports is None:
            self.__open_ports = [x for x, y in self.ports.items() if y.lower() == "open"]

        return self.__open_ports
        
__all__ = ["Results", "Parameters"]