#!/usr/bin/python3
from hashlib import new
from tkinter.messagebox import askokcancel, showinfo, showwarning
import webbrowser
from selenium.webdriver.common.by import By
import tkinter as tk, json, os, pyperclip
from tkinter import *
class helps(tk.Tk):
    def __init__(self, parent = None):
        super().__init__()
        self.title("快速帮助中心")
        self.setup_UI()
    def gotowebdriver(self, url):
        webbrowser.open(url)
    def setup_UI(self):
        but1 = Button(self, text = "我要如何领取各项赞助福利?", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-Hd4S"))
        but1.grid(row = 0, column = 0, columnspan = 6, ipadx = 20, ipady = 10, padx = 20, pady = 10)
if __name__ == '__main__':
    helps().mainloop()