import configparser
import os
import sys

_fname = 'config.ini'
config = configparser.ConfigParser()

_bname = 'config.ini'
if not os.path.isfile(_bname):
    _bname = os.path.join('D:\Python\gitrepo',_fname)

print(_bname)
config.read(_bname)
environment = config.get('APP','ENVIRONMENT')
platfrom = config.get('APP','PLATFORM')

def setEnvironment(env):
    config.set('APP','ENVIRONMENT',env)

    if env =='DEV':
        config.set('APP','BCP_ENVIRONMENT','WQA2')

    if env == 'QA':
        config.set('APP', 'BCP_ENVIRONMENT', 'WQA2')

    if env == 'PROD':
        config.set('APP', 'BCP_ENVIRONMENT', 'DEV')
