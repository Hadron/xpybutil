from __future__ import print_function
import sys

from distutils import sysconfig
from distutils.core import setup

try:
    from xpybutil.compat import xproto, xinerama, randr
except:
    print ('')
    print ('xpybutil requires the X Python Binding')
    print ('See: http://cgit.freedesktop.org/xcb/xpyb/')
    print ('More options: xpyb-ng:', 'https://github.com/dequis/xpyb-ng',
           'and xcffib:', 'https://github.com/tych0/xcffib')
    raise

setup(
    name = "xpybutil",
    author = "Andrew Gallant",
    author_email = "andrew@pytyle.com",
    version = "0.0.1",
    license = "WTFPL",
    description = "An incomplete xcb-util port plus some extras",
    long_description = "See README",
    url = "http://pytyle.com",
    platforms = 'POSIX',
    packages = ['xpybutil'],
    data_files = [('share/doc/xpybutil', ['README', 'COPYING'])]
)
