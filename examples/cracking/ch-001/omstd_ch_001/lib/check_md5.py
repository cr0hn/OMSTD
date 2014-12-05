# -*- coding: utf-8 -*-

"""
Project name: hh-001
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


import json
import urllib.request

from random import randint

from .data import Parameters, PASSWORD_MD5_CRACKING_PROVIDERS, InvalidHashFormat, HashNotFound


# ----------------------------------------------------------------------
def check_md5(config):
    """
    Find MD5 hash in providers.

    :param config: Parameters object
    :type config: Parameters

    :return: plain string with text or exception if not found hash
    :rtype: str

    :raises: HashNotFound, InvalidHashFormat
    """
    if not isinstance(config, Parameters):
        raise TypeError("Expected Parameters, got '%s' instead" % type(config))

    providers_to_check = PASSWORD_MD5_CRACKING_PROVIDERS if config.provider == "all" else [config.provider]

    plain_text = None
    for p in providers_to_check:
        # Make URL using md5cracker API
        url = "http://md5cracker.org/api/api.cracker.php?r=%s&database=%s&hash=%s" % (
            randint(500, 10000),
            p,
            config.md5_hash)

        # Proxy setted?
        open_fn = None
        if config.proxy is not None:
            proxy_handler = urllib.request.ProxyHandler({config.proxy.scheme: config.proxy.netloc})

            if config.proxy_user is not None:
                proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
                proxy_auth_handler.add_password('realm', 'host', config.proxy_user, config.proxy_pass)

                opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

            opener = urllib.request.build_opener(proxy_handler)
            # This time, rather than install the OpenerDirector, we use it directly:
            open_fn = opener.open
        else:
            open_fn = urllib.request.urlopen

        # Get remote info
        u = open_fn(url)
        _tmp_results = u.read().decode('utf-8')

        if _tmp_results is None:
            continue

        _json_results = json.loads(_tmp_results)

        # Its fails?
        if _json_results['status'] is False:
            # Check if reason is for not recoverable error
            if 'Invalid hash' in _json_results['message']:
                raise InvalidHashFormat("Invalid Hash Format")

            # It not found hash continue
            continue

        else:
            # Hash found!!!!
            plain_text = _json_results['result']
            break

    if plain_text is None:
        HashNotFound("Plain text not found for hash: '%s'" % config.md5_hash)

    return plain_text