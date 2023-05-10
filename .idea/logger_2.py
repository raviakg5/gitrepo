import datetime
import getpass
import logging
import os
import os.path
import sys
from copy import copy
from logging import Formmater ,handlers

import confmod

LOG_FILE = confmod.config.get('APP','LOG_FILE_NAME')
USE_MEMORY_LOGS = confmod.config.get('APP','USE_MEM_LOGS') == 'True'
VERBOSE_MODE = confmod.config.get('APP','VERBOSE_MODE') == 'True'

def init_logger(logger_name='',logger_filter='INFO',run_id =0,file_only=False,account=None,existing_file_path=None):
    print("\n\n----------------init_logger-----------------")
    print(" logger_name = {}\n".format(logger_name))
    if logger_name == '':
        logger = logging.getLogger(name='andrea_logger04')
    else :
        logger = logging.getLogger(name=logger_name)

    if logger_filter == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    if logger_filter == 'INFO':
        logger.setLevel(logging.INFO)
    if logger_filter == 'WARNING':
        logger.setLevel(logging.WARNING)
    else :
        logger.setLevel(logging.ERROR)

    log_file_name = None
    '''if existing_file_path and os.path.exists(existing_file_path):
        print(hello)
        path = existing_file_path
        log_file_name = existing_file_path
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.isdir(path):
        log_file_name = path + '/' + formatted_log_name'''
    log_file_name = existing_file_path

    return log_file_name

logger = init_logger(logger_name='SMAlogger',logger_filter='INFO',existing_file_path='D:\Python\gitrepo')
print(logger)



