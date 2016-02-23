#!/usr/bin/env python
# coding:utf8

INFO = '\033[92m'
WARNING = '\033[1;93m'
ERROR = '\033[91m'
FATAL = '\033[90m'
END = '\033[0m'


def log_info(message):
    print '{0}INFO: {1}{2}'.format(INFO, message, END)


def log_warn(message):
    print '{0}INFO: {1}{2}'.format(WARNING, message, END)


def log_error(message):
    print '{0}INFO: {1}{2}'.format(ERROR, message, END)


def log_fatal(message):
    print '{0}INFO: {1}{2}'.format(FATAL, message, END)

