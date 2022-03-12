#!/usr/bin/python3
from hashlib import new
import tkinter as tk, os
from tkinter import *
class launcher(tk.Tk):
    def __init__(self, parent = None):
        super().__init__()
        self.title("PCL工具箱")
        self.setup_UI()
#组件对应逻辑
    def goto_cave(self):
        os.popen('python cave.py')
    def goto_help(self):
        os.popen('python helps.py')
#GUI
    def setup_UI(self):
        but1 = Button(self, text = "回声洞快速提交", command = self.goto_cave)
        but1.grid(row = 0, column = 0, columnspan = 6, ipadx = 60, ipady = 10, padx = 30, pady = 15)
        but2 = Button(self, text = "帮助文档", command = self.goto_help)
        but2.grid(row = 1, column = 0, columnspan = 6, ipadx = 60, ipady = 10, padx = 30, pady = 15)
if __name__ == '__main__':
    launcher().mainloop()
