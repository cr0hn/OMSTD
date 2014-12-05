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

PASSWORD_MD5_CRACKING_PROVIDERS = [
    'md5cracker.org',
    'tmto',
    'md5.net',
    'md5online.net',
    'md5.my-addr.com',
    'md5decryption.com',
    'md5crack',
    'authsecu',
    'netmd5crack',
    'md5pass',
    'i337.net'
]


class InvalidHashFormat(Exception):
    pass


class HashNotFound(Exception):
    pass


# --------------------------------------------------------------------------
class Parameters:
    """Program parameters"""

    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
        :param md5_hash: MD5 Hash to looking for plain text 
        :type md5_hash: str
        
        :param verbosity: verbosity level 
        :type verbosity: int
        
        :param provider: provider name. Default 'all'. 
        :type provider: str

        :param proxy: URL with proxy info
        :type proxy: str

        :raises: ValueError
        """
        self.md5_hash = kwargs.get("md5_hash")
        self.verbosity = kwargs.get("verbosity")
        self.provider = kwargs.get("provider", "all").lower()
        self.proxy = kwargs.get("proxy", None)
        self.proxy_user = kwargs.get("proxy_user", None)
        self.proxy_pass = kwargs.get("proxy_pass", None)

        if self.provider != "all" and self.provider not in PASSWORD_MD5_CRACKING_PROVIDERS:
            raise ValueError("Selected provider is not a valid provider")

        if self.proxy is not None:
            from urllib.parse import urlparse

            _scheme = "http" if self.proxy.startswith("http://") or self.proxy.startswith("https://") else ""
            self.proxy = urlparse(self.proxy, scheme=_scheme)


# --------------------------------------------------------------------------
class Results:
    """Program results"""

    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        self.plain_password = kwargs.get("plain_password", None)
        self.is_hash_found = kwargs.get("is_hash_found", False)


__all__ = ["Results", "Parameters", "PASSWORD_MD5_CRACKING_PROVIDERS", "InvalidHashFormat","HashNotFound"]