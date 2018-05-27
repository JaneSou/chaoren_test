# -*- coding: utf-8-*-
import os
# Dingdang main directory
APP_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))

DATA_PATH = os.path.join(APP_PATH, "data")
LIB_PATH = os.path.join(APP_PATH, "chaoren")
TEMP_PATH = os.path.join(DATA_PATH, "temp")
LOG_PATH = os.path.join(DATA_PATH,"logs")
STATIC_PATH = os.path.join(DATA_PATH, "static")
PLUGIN_PATH = os.path.join(LIB_PATH, "plugins")
LOGIN_PATH = os.path.join(DATA_PATH, "login")

CONFIG_PATH = os.path.expanduser(
    os.getenv('DINGDANG_CONFIG', '~/.chaoren')
)
CONTRIB_PATH = os.path.expanduser(
    os.getenv('DINGDANG_CONFIG', '~/.chaoren/contrib')
)
CUSTOM_PATH = os.path.expanduser(
    os.getenv('DINGDANG_CONFIG', '~/.chaoren/custom')
)


def config(*fname):
    return os.path.join(CONFIG_PATH, *fname)


def data(*fname):
    return os.path.join(DATA_PATH, *fname)
