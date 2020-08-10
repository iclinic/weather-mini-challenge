#
# Copyright (c) 2020 Murilo Ijanc' <mbsd@m0x.ru>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
"""
setup script for the iclinic-challenge project
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONF = {
	'description':    	'iclinic weather',
    'author':           'Murilo Ijanc',
    'url':              '',
    'download_url':     '',
    'author_email':     'mbsd@m0x.ru',
    'version':          '0.0.1',
    'install_requires': [ ],
    'packages':         [],
    'scripts':          ['iclinic_wea.py'],
    'name':             'iclinic-wea'
}

setup(**CONF)
