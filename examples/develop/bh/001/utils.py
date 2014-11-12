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
def find_tasks_in_project(project_root=None):
    """
    Find all tasks in all files, getting python modules.

    :return: an iterator with python modules
    :rtype: set(str)
    """
    import os
    if project_root is None:
        project_root = os.getcwd()
    else:
        if not os.path.isabs(project_root):
            project_root = os.path.abspath(project_root)
    pkg_path = os.path.abspath(project_root)

    # Find all .py files
    results = set()
    results_add = results.add

    for root, dirs, files in os.walk(pkg_path):
        if "template" in root:
            continue
        for filename in files:
            if filename.endswith(".py") and \
                    not filename.startswith("__") and \
                    not filename.startswith("celery"):
                task = os.path.join(root, filename) \
                    .replace(os.path.dirname(project_root) + '/', '') \
                    .replace(os.path.sep, '.') \
                    .replace('.py', '')

                results_add(task)

    return results
