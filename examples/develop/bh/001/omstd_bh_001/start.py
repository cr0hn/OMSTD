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
# import sys
# import os
#
# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# mod = __import__('omstd_bh_001')
# sys.modules["omstd_bh_001"] = mod


__author__ = 'cr0hn - cr0hn<-at->cr0hn.com (@ggdaniel)'


# ----------------------------------------------------------------------
def main():
    from .framework.tasks.main_task import omstd_bh_001_task

    omstd_bh_001_task.delay()

# if __name__ == '__main__':
if __name__ == "__main__" and __package__ is None:
    # import os
    # import sys
    # print(os.getcwd())
    # sys.path.insert(1, os.getcwd())
    # import os
    # import sys
    # from pprint import pprint
    # sys.path.append(os.path.abspath('.'))
    # sys.path.insert(1, os.path.abspath('.'))
    # pprint(sys.modules)
    # __import__("omstd_bh_001")
    # __package__ = "omstd_bh_001"


    import sys, os
    # The following assumes the script is in the top level of the package
    # directory.  We use dirname() to help get the parent directory to add to
    # sys.path, so that we can import the current package.  This is necessary
    # since when invoked directly, the 'current' package is not automatically
    # imported.
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import omstd_bh_001
    __package__ = str("omstd_bh_001")
    del sys, os

    main()