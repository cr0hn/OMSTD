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

import argparse


# ----------------------------------------------------------------------
def main():
    from .api import Parameters, run_in_console

    parser = argparse.ArgumentParser(description='YOUR DESCRIPTION') # TODO
    # parser.add_argument("positional", metavar='POSITIONAL', help="HELP", nargs="+")
    parser.add_argument('-v', dest='verbosity', default=0, action="count", help="verbosity level: -v, -vv, -vvv.")
    # parser.add_argument("--open", dest="opt_open", action="store_true", help="HELP", default=False)
    # parser.add_argument("-p", dest="opt_p", help="HELP", default="")

    params = parser.parse_args()

    # Set config
    try:
        input_parameters = Parameters(verbosity=params.verbosity)
    except ValueError as e:
        print(e)
        exit()

    run_in_console(input_parameters)


if __name__ == "__main__" and __package__ is None:
    import sys
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)

    import omstd_st_001  # TODO
    __package__ = str("omstd_st_001")  # TODO
    del sys, os

    main()