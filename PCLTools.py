#!/usr/bin/python 3
from tkinter.messagebox import showwarning
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk, json, os
from tkinter import *

#处理所填写的数据
def submit():
    ipt1 = e1.get()
    ipt2 = e2.get()
    ipt3 = e3.get()
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
    #driver.quit()
def save():
    qq = e1.get()
    filen = e2.get()
    jsdata = {"qq": qq, "file": filen}
    with open(os.path.abspath("edata.json"), "w") as dtjs:
        json.dump(jsdata, dtjs)

def usave():
    ipt = e3.get()
    if not ipt:
        showwarning("警告", "请先输入内容")
    else:
        with open(os.path.abspath("edata.json")) as dtjs:
            jsdata = json.load(dtjs)
        if jsdata["qq"] == None or jsdata["file"] == None:
            showwarning("警告", "您还没有保存过")
        else:
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
root = Tk()
root.title("回声洞快速提交")
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

