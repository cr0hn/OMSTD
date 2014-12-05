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
    from .api import Parameters, run_console, PASSWORD_MD5_CRACKING_PROVIDERS
    parser = argparse.ArgumentParser(description='OMSTD Example')
    parser.add_argument("-m", "--md5", dest="password", help="MD5 hashed value to test (mandatory)", default=None)
    parser.add_argument("-v", dest="verbosity", help="verbosity level")
    parser.add_argument("-p", dest="provider", help="select provider used to get cracked MD5 hash. Defaul: all.",
                        default="all")
    parser.add_argument("--proxy", dest="proxy", help="proxy in format: http://USER:PASS@IP:PORT")
    parser.add_argument("--list-providers", dest="list_providers", action="store_true", help="list password providers",
                        default=False)

    params = parser.parse_args()

    # List providers?
    if params.list_providers is True:
        print("\nCracking providers:")
        print("  - all (special case. Select all providers)")
        for x in PASSWORD_MD5_CRACKING_PROVIDERS:
            print("  - %s" % x)
        print()
        exit()

    # Checks if md5 info is set
    if params.password is None:
        print("error: the following arguments are required: -m/--md5")
        exit()

    # Set config
    try:
        input_parameters = Parameters(md5_hash=params.password,
                                      verbosity=params.verbosity,
                                      provider=params.provider,
                                      proxy=params.proxy)
    except ValueError as e:
        print(e)
        exit()

    run_console(input_parameters)


if __name__ == "__main__" and __package__ is None:
    import sys
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import omstd_ch_001
    __package__ = str("omstd_ch_001")
    del sys, os

    main()