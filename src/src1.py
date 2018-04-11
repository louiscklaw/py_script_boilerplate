#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

from res.res1 import *


class src:
    def __init__(self):
        pass

    def print_helloworld(self):
        try:
            print(res.constant.TEXT_HELLOWORLD)

        except Exception as e:
            print(res.error_text.ERROR_DURING_TRY_HELLOWORLD)
            raise e
