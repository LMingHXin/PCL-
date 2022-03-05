#!/usr/bin/python3
from hashlib import new
from tkinter.messagebox import askokcancel, showinfo, showwarning
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk, json, os
from tkinter import *

#组件对应逻辑
def goto_cave():
    os.popen('python cave.py')

#GUI设计
root = tk.Tk()
root.title("PCL工具箱")
but1 = Button(root, text = "回声洞快速提交", command = goto_cave)
but1.grid(row = 0, column = 0, columnspan = 6, ipadx = 60, ipady = 10, padx = 30, pady = 15)
tk.mainloop()
