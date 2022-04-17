#!/usr/bin/python3
import tkinter as tk, os
from tkinter import *
from tkinter.messagebox import showinfo
class launcher(tk.Tk):
    def __init__(self, parent = None):
        super().__init__()
        self.title("PCL工具箱")
        self.setup_UI()
        showinfo("好消息", "Release1.1.0版本发布!\n本版本将回声洞递交模拟的浏览器后台运行,同时支持了EDGE浏览器~")
#组件对应逻辑
    def goto_cave(self):
        os.startfile(os.path.abspath('cave.exe'))
    def goto_help(self):
        os.startfile(os.path.abspath('helps.exe'))

#上为按钮组件逻辑
#下为菜单组件逻辑
    def aboutit(self):
        showinfo("关于我", "目前总版本:Realese-1.1\n回声洞递交版本:Realease-2.0\n帮助版本:Complete-1.0\n帮助版本随文档更新而更新")

#菜单对应逻辑
    def mMenu(win, self):
        root = Menu(win)
        win.config(menu = root)

        about = Menu(root, tearoff= False)
        about.add_command(label = "版本", command = self.aboutit, underline = 0)
        root.add_cascade(label = "关于", menu = about)
#GUI
    def setup_UI(self):
        self.mMenu(self)
        but1 = Button(self, text = "回声洞快速提交", command = self.goto_cave)
        but1.grid(row = 0, column = 0, columnspan = 6, ipadx = 60, ipady = 10, padx = 30, pady = 15)
        but2 = Button(self, text = "快速帮助文档", command = self.goto_help)
        but2.grid(row = 1, column = 0, columnspan = 6, ipadx = 60, ipady = 10, padx = 30, pady = 15)
if __name__ == '__main__':
    launcher().mainloop()
