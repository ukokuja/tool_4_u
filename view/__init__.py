#!/usr/bin/env python3

import os 
from consolemenu import *
from consolemenu.items import *

class ViewManager(object):
    def __init__(self, controller):
        self.__controller = controller
