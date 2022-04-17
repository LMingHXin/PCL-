#!/usr/bin/python 3
#import一大堆(
from selenium.webdriver import Edge 
from tkinter.messagebox import askokcancel, showinfo, showwarning
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk, json, os, pyperclip
from tkinter import *
class cave(tk.Tk):
    def __init__(self, parent = None):
        super().__init__()
        self.title("回声洞快速递交")
        self.setup_UI()

    #处理所填写的数据
    def submit(self):
        showwarning("提示", "按下提交后可能程序会卡顿一段时间,请不要担心,这是正常现象")
        ipt1 = self.e1.get()
        ipt2 = self.e2.get()
        ipt3 = self.e3.get()
        if not ipt1 or not ipt2 or not ipt3:
            showwarning("警告", "你还没有输入内容")
        else:
            if self.rut_var.get == 0:
                option=webdriver.ChromeOptions()
                option.add_argument('headless')
                driver=webdriver.Chrome(chrome_options = option)
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
            elif self.rut_var == 1:
                try:
                    option = webdriver.EdgeOptions()
                    option.add_argument('--headless')
                    driver = Edge("C:/Program Files/EdgeDriver/msedgedriver.exe", options = option)
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
                except:
                    showwarning("错误", "Edge无法使用,请检查您是否安装了Edge,若没有请前往https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/\n链接已经保存至你的剪贴板")
                    fwurl = "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
                    pyperclip.copy(fwurl)
                    pyperclip.paste()

    #保存按钮所对应逻辑
    def save(self):
        qq = self.e1.get()
        filen = self.e2.get()
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
    def usave(self):
        global var
        try:
            showwarning("提示", "按下提交后可能程序会卡顿一段时间,请不要担心,这是正常现象")
            ipt = self.e3.get()
            if not ipt:
                showwarning("警告", "请先输入内容")
            else:
                with open(os.path.abspath("edata.json")) as dtjs:
                    jsdata = json.load(dtjs)
                if jsdata["qq"] == "" or jsdata["file"] == "":
                    showwarning("警告", "您还没有保存过")
                else:
                    ipt1 = jsdata["qq"]
                    ipt2 = jsdata["file"]
                    ipt3 = self.e3.get()
                    if self.rut_var.get() == 0:
                        print(0)
                        option=webdriver.ChromeOptions()
                        option.add_argument('headless')
                        driver=webdriver.Chrome(chrome_options = option)
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
                    elif self.rut_var.get()== 1:
                        print(1)
                        try:
                            option = webdriver.EdgeOptions()
                            option.add_argument('--headless')
                            driver = Edge("C:/Program Files/EdgeDriver/msedgedriver.exe", options = option)
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
                        except:
                            showwarning("错误", "Edge无法使用,请检查您是否安装了Edge,若没有请前往https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/\n链接已经保存至你的剪贴板")
                            fwurl = "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
                            pyperclip.copy(fwurl)
                            pyperclip.paste()
        except FileNotFoundError:
            showwarning("警告", "您还没有保存过预设")

    #上面为GUI按钮+entry组件逻辑
    #下面是菜单系统中的逻辑

    def fdnew(self):
        showinfo("反馈指南", "欢迎您反馈新的功能!\n请前往:https://github.com/LMingHXin/PCL-/upload/main/issues 提交issue!\n(注意issue#2中的内容)\n网址已经在您的剪贴板了~")
        fwurl = "https://github.com/LMingHXin/PCL-/upload/main/issues"
        pyperclip.copy(fwurl)
        pyperclip.paste()
    def bug(self):
            showinfo("反馈指南", "我们将会及时修好bug!\n请前往:https://github.com/LMingHXin/PCL-/upload/main/issues 提交issue\n注意看issue#2的内容\n网址已经在您的剪贴板了~")
            fwurl = "https://github.com/LMingHXin/PCL-/upload/main/issues"
            pyperclip.copy(fwurl)
            pyperclip.paste()

    def helps(self):#对应帮助
        showinfo("帮助", "这是专属于PCL回声洞的提交系统\n你可以填写QQ号与图片路径两行的内容后单击保存\n下次使用时仅需输入回声洞留言内容后单击使用预设即可\n如若使用预设时出现你还没有保存预设,请先使用保存按钮")

    def programmer(self):#对应开发人员
        showinfo("开发人员", "开发者:rminghxin\n协作人员:Ricky89555\n没错只有两个人(")

    def aboutit(self):#对应关于
        showinfo("关于", "回声洞版本:Complete-2.0\n最近更新:2022-4-17")

    #菜单系统
    def mMenu(win, self): 
        root=Menu(win)
        win.config(menu = root)

        feedback = Menu(root, tearoff = False)
        feedback.add_command(label = "反馈新功能", command = self.fdnew, underline = 0)
        feedback.add_command(label = "反馈bug", command = self.bug, underline = 0)
        root.add_cascade(label = "反馈", menu = feedback)

        others = Menu(root, tearoff = False)#更多选项的所有command
        others.add_command(label = '帮助', command = self.helps, underline=1)
        others.add_command(label = "开发人员", command = self.programmer, underline = 1)
        others.add_command(label = "关于", command = self.aboutit, underline = 1)
        root.add_cascade(label = "更多选项", menu = others)

    #GUI视图布局
    def setup_UI(self):
        self.rut_var = IntVar()
        self.mMenu(self)
        but = Button(self, text ='提交', command = self.submit)
        but.grid(row = 7, column = 4,  columnspan = 2, padx = 10, pady = 8, ipadx = 10, ipady = 8)
        but_2 = Button(self, text = '保存', command = self.save)
        but_2.grid(row = 7, column = 2,  columnspan = 2, padx = 10, pady = 8, ipadx = 10, ipady = 8)
        but_3 = Button(self, text = '使用预设', command = self.usave)
        but_3.grid(row = 7, column = 0,  columnspan = 2, padx = 10, pady = 8, ipadx = 10, ipady = 8)
        rut_1 = Radiobutton(self, text = "Chrom浏览器", variable = self.rut_var, value = 0)
        rut_1.grid(row = 0, column = 0, columnspan = 3)
        rut_2 = Radiobutton(self, text = "EDGE浏览器", variable = self.rut_var, value = 1)
        rut_2.grid(row = 0, column = 3, columnspan = 3)
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e1.grid(row = 2, column = 0, columnspan = 6, ipadx = 60)
        self.e2.grid(row = 4, column = 0, columnspan = 6, ipadx = 60)
        self.e3.grid(row = 6, column = 0, ipady = 100, columnspan = 6, ipadx = 60)
        tk.Label(self, text = 'QQ号').grid(row = 1, column = 0, columnspan = 6)
        tk.Label(self, text = '图片路径').grid(row = 3, column = 0, columnspan = 6)
        tk.Label(self, text = '回声洞留言内容').grid(row = 5, column = 0, columnspan = 6)
if __name__ == '__main__':
    cave().mainloop()