# -*- coding: utf-8 -*-

"""
Project name: OMSTD
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

import argparse


if __name__ == "__main__":

    footed_description = """

    Usage examples:
        + Basic scan:
            %(name)s 127.0.0.1
        + Specifing port to test:
            %(name)s -p 443 127.0.0.1
        + Only diplay open ports
            %(name)s -p 139 127.0.0.1

    """"" % dict(name="st-005-s1.py")

    parser = argparse.ArgumentParser(description='OMSTD Example', epilog=footed_description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("targets", metavar='TARGETS', help="targets to scan", nargs="+")
    parser.add_argument('-v', dest='verbosity', default=0, action="count",
                        help="verbosity level: -v, -vv, -vvv.")
    parser.add_argument("--open", dest="only_open", action="store_true",
                        help="only display open ports", default=False)
    parser.add_argument("-p", "--ports", dest="port", type=int,
                        help="port to scan. Defaul: 80.", default=80)

    params = parser.parse_args()