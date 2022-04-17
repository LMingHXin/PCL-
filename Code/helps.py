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
        but1 = Button(self, text = "如何领取赞助福利", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-Hd4S"))
        but1.grid(row = 0, column = 0, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but2 = Button(self, text = "主题系列问题", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-mNPA"))
        but2.grid(row = 0, column = 4, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but3 = Button(self, text = "获取PCL快照版系列问题", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-MVh3"))
        but3.grid(row = 1, column = 0, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but4 = Button(self, text = "Mod等安装问题", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-4PuC"))
        but4.grid(row = 1, column = 4, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but5 = Button(self, text = "下载出现问题", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-gKra"))
        but5.grid(row = 2, column = 0, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but6 = Button(self, text = "识别/解锁码用法", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-d9kq"))
        but6.grid(row = 2, column = 4, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but7 = Button(self, text = "爱发电主页", command = lambda: self.gotowebdriver("https://afdian.net/@LTCat"))
        but7.grid(row = 3, column = 0, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
        but8 = Button(self, text = "如何找管理", command = lambda: self.gotowebdriver("https://shimo.im/docs/qKPttVvXKqPD8YDC#anchor-ceFU"))
        but8.grid(row = 3, column = 4, columnspan = 3, ipadx = 20, ipady = 10, padx = 20, pady = 10)
if __name__ == '__main__':
    helps().mainloop()