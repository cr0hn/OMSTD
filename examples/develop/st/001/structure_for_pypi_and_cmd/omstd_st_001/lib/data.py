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
        :param verbosity: verbosity level
        :type verbosity: int

        :raises: ValueError
        """
        self.verbosity = int(kwargs.get("verbosity", 0))


# --------------------------------------------------------------------------
class Results:
    """Program results"""

    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
        :param execution_time: Time got for scan in miliseconds
        :type execution_time: float

        """
        self.execution_time = kwargs.get("execution_time", 0)


__all__ = ["Results", "Parameters"]