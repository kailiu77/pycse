# for installing magic IPython stuff
import IPython, os

IPydir = os.path.join(IPython.utils.path.get_ipython_dir(),
                      'profile_default',
                      'startup')
                      
print 'Installing ipython magic to : ',IPydir

if not os.path.exists(IPydir):
    raise Exception('No ipython directory found')

url = 'https://raw.github.com/jkitchin/pycse/master/pycse/00-pycse-magic.py'

import urllib
urllib.urlretrieve (url, os.path.join(IPydir,'00-pycse-magic.py'))

print 'Ipython magic installed now!'

from setuptools.command import easy_install
easy_install.main( ["-U","quantities"] )
easy_install.main( ["-U","uncertainties"] )

package = 'https://github.com/jkitchin/pyreport/archive/master.zip'
easy_install.main( ["-U",package] )

print 'Extra packages now installed.'