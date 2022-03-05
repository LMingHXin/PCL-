#!/usr/bin/python 3
#import一大堆(
from hashlib import new
from tkinter.messagebox import askokcancel, showinfo, showwarning
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk, json, os, pyperclip
from tkinter import *

#处理所填写的数据
def submit():
    ipt1 = e1.get()
    ipt2 = e2.get()
    ipt3 = e3.get()
    if not ipt1 or not ipt2 or not ipt3:
        showwarning("警告", "你还没有输入内容")
    else:
        driver = webdriver.Chrome()
        driver.get("https://jinshuju.net/f/esXHQF")#确定网址
        driver.implicitly_wait(10)
        input_1 = driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/input')
        input_1.send_keys(ipt1)
        input_2 = driver.find_element(By.CLASS_NAME, "field_2").find_element(By.TAG_NAME, "input")
        input_2.send_keys(ipt2)
        input_3 = driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[6]/div/div/div[2]/div[1]/div/span/textarea')
        input_3.send_keys(ipt3)
        btn =  driver.find_element_by_xpath('//*[@id="root"]/div/form/div[5]/div[1]/button')
        btn.click()
        driver.quit()

#保存按钮所对应逻辑
def save():
    qq = e1.get()
    filen = e2.get()
    if not qq or not filen:
        showwarning("警告", "请输入内容")
    else:
        jsdata = {"qq": qq, "file": filen}
        if jsdata["qq"] != "" or jsdata["file"] != "":
            ans = askokcancel("确定", "您确定要覆盖已有预设吗")
            if ans:
                with open(os.path.abspath("edata.json"), "w") as dtjs:
                    json.dump(jsdata, dtjs)
                showinfo("提示", "保存成功!")
            else:
                pass
        else:
            with open(os.path.abspath("edata.json"), "w") as dtjs:
                json.dump(jsdata, dtjs)
            showinfo("提示", "保存成功!")

#使用预设按钮所对应逻辑
def usave():
    ipt = e3.get()
    if not ipt:
        showwarning("警告", "请先输入内容")
    else:
        with open(os.path.abspath("edata.json")) as dtjs:
            jsdata = json.load(dtjs)
        if jsdata["qq"] == "" or jsdata["file"] == "":
            showwarning("警告", "您还没有保存过")
        else:
            #这里再写一遍好麻烦qwq
            ipt1 = jsdata["qq"]
            ipt2 = jsdata["file"]
            ipt3 = e3.get()
            driver = webdriver.Chrome()
            driver.get("https://jinshuju.net/f/esXHQF")#确定网址
            driver.implicitly_wait(10)
            input_1 = driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/span/input')
            input_1.send_keys(ipt1)
            input_2 =driver.find_element(By.CLASS_NAME, "field_2").find_element(By.TAG_NAME, "input")
            input_2.send_keys(ipt2)
            input_3 = driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[1]/div[6]/div/div/div[2]/div[1]/div/span/textarea')
            input_3.send_keys(ipt3)
            btn =  driver.find_element_by_xpath('//*[@id="root"]/div/form/div[5]/div[1]/button')
            btn.click()
            driver.quit()

#上面为GUI按钮+entry组件逻辑
#下面是菜单系统中的逻辑

def fdnew():
    showinfo("反馈指南", "欢迎您反馈新的功能!\n请前往:https://github.com/LMingHXin/PCL-/upload/main/issues 提交issue!\n(注意issue#2中的内容)\n网址已经在您的剪贴板了~")
    fwurl = "https://github.com/LMingHXin/PCL-/upload/main/issues"
    pyperclip.copy(fwurl)
    pyperclip.paste()
def bug():
        showinfo("反馈指南", "我们将会及时修好bug!\n请前往:https://github.com/LMingHXin/PCL-/upload/main/issues 提交issue\n注意看issue#2的内容\n网址已经在您的剪贴板了~")
        fwurl = "https://github.com/LMingHXin/PCL-/upload/main/issues"
        pyperclip.copy(fwurl)
        pyperclip.paste()

def helps():#对应帮助
    showinfo("帮助", "这是专属于PCL回声洞的提交系统\n你可以填写QQ号与图片路径两行的内容后单击保存\n下次使用时仅需输入回声洞留言内容后单击使用预设即可")

def programmer():#对应开发人员
    showinfo("开发人员", "开发者:rminghxin\n协作人员:Ricky89555\n没错只有两个人(")

def aboutit():#对应关于
    showinfo("关于", "版本:Dev-0.1.2-22-3-5\n最近更新:2022-3-5")

#累死人的菜单系统
def mMenu(win): 
    root=Menu(win)
    win.config(menu = root)

    feedback = Menu(root, tearoff = False)
    feedback.add_command(label = "反馈新功能", command = fdnew, underline = 0)
    feedback.add_command(label = "反馈bug", command = bug, underline = 0)
    root.add_cascade(label = "反馈", menu = feedback)

    others = Menu(root, tearoff = False)#更多选项的所有command
    others.add_command(label = '帮助', command = helps, underline=1)
    others.add_command(label = "开发人员", command = programmer, underline = 1)
    others.add_command(label = "关于", command = aboutit, underline = 1)
    root.add_cascade(label = "更多选项", menu = others)

#GUI视图布局
root = tk.Tk()
root.title("回声洞快速提交")
mMenu(root)
but = Button(root, text ='提交', command = submit)
but.grid(row = 6, column = 4,  columnspan = 2, padx = 10, pady = 8, ipadx = 10, ipady = 8)
but_2 = Button(root, text = '保存', command = save)
but_2.grid(row = 6, column = 2,  columnspan = 2, padx = 10, pady = 8, ipadx = 10, ipady = 8)
but_3 = Button(root, text = '使用预设', command = usave)
but_3.grid(row = 6, column = 0,  columnspan = 2, padx = 10, pady = 8, ipadx = 10, ipady = 8)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e1.grid(row = 1, column = 0, columnspan = 6, ipadx = 60)
e2.grid(row = 3, column = 0, columnspan = 6, ipadx = 60)
e3.grid(row = 5, column = 0, ipady = 100, columnspan = 6, ipadx = 60)
tk.Label(root, text = 'QQ号').grid(row = 0, column = 0, columnspan = 6)
tk.Label(root, text = '图片路径').grid(row = 2, column = 0, columnspan = 6)
tk.Label(root, text = '回声洞留言内容').grid(row = 4, column = 0, columnspan = 6)
tk.mainloop()
