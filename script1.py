#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

from res.res1 import *
from src.src1 import *


def main():
    test = src()
    test.print_helloworld()


if __name__ == '__main__':
    main()
