# -*- coding: utf-8 -*-

"""
Project name: OMSTD
Project URL: https://github.com/cr0hn/open_shortener

Copyright (c) 2014, cr0hn<-AT->cr0hn.com
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

__author__ = 'cr0hn - cr0hn<-at->cr0hn.com (@ggdaniel)'

from functools import partial

from externa.api import action_with_callback


def actions(operation, data1, data2):
    if operation == 0:
        return data1 / data2
    elif operation == 1:
        return data1 * data2
    elif operation == 2:
        return data1 % data2

if __name__ == "__main__":
    import sys

    # Get first and second command line parameters:
    # arg 0 -> operation
    # arg 1 -> first value for operation
    operation = sys.argv[0]
    data1 = sys.argv[1]

    new_actions = partial(actions, operation, data1)

    action_with_callback(callback_func=new_actions)  # Well!