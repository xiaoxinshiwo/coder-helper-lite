# -- coding:UTF-8 --
# Author:章永新

import logging
import os
import logging.handlers


'''
日志模块
'''
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
LOG_FILENAME='coder-helper.log'


def set_logger():
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    log_file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../logs"))
    if not os.path.exists(log_file_path):
        os.makedirs(log_file_path)
    log_file = os.path.join(log_file_path, LOG_FILENAME)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=52428800, backupCount=5, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


set_logger()