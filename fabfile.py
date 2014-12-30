from fabric.api import *

def setup(index_url=None):
    """creates the virtual environments and installs the requirements"""
    local('python virtualenv.py env')
    pypi_url = '-i %s' % index_url if index_url else ''
    _virtualenv('pip install setuptools --upgrade %s' % pypi_url)
    _virtualenv('pip install -r requirements.txt %s' % pypi_url)

def _virtualenv(command, *args):
    return local('. env/bin/activate&& ' + command + ' ' + ' '.join(args), capture=False)
