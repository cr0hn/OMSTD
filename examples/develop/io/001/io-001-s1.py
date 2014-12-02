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


# ----------------------------------------------------------------------
class Displayer:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
            cls.__initialized = False
        return cls.instance

    def config(self, **kwargs):
        self.out_file = kwargs.get("out_file", None)
        self.out_screen = kwargs.get("out_screen", True)
        self.verbosity = kwargs.get("verbosity", 0)

        if self.out_file:
            self.out_file_handler = open(self.out_file, "w")

    def display(self, message):
        if self.verbosity > 0:
            self.__display(message)

    def display_verbosity(self, message):
        if self.verbosity > 1:
            self.__display(message)

    def display_more_verbosity(self, message):
        if self.verbosity > 2:
            self.__display(message)

    def __display(self, message):
        if self.out_screen:
            print(message)
        if self.out_file_handler:
            self.out_file_handler.write(message)

    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            self.out_file = None
            self.out_file_handler = None
            self.out_screen = True
            self.verbosity = 0


# ----------------------------------------------------------------------
def hello():
    """Display a hello world text"""

    # Use displayer
    out = Displayer()
    out.display("hello")

    out.display_verbosity("hello")

    # This will not be displayed by the verbosity level to 1
    out.display_more_verbosity("hello")

# ----------------------------------------------------------------------
if __name__ == '__main__':

    # Config displayer
    d = Displayer()
    d.config(out_screen=True,
             out_file="~/my_log.txt",
             verbosity=1)

    # Call function
    hello(1)
