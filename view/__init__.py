#!/usr/bin/env python3

import os
from simple_term_menu import TerminalMenu



class ViewManager(object):
    def __init__(self, controller):
        self.__controller = controller

    def start(self):
        self.show_menu()

    def show_menu(self):
        fruits = ["[a] apple", "[b] banana", "[o] orange"]
        terminal_menu = TerminalMenu(fruits, title="Fruits")
        menu_entry_index = terminal_menu.show()