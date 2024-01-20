# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:34:30 2024

@author: USER
"""

import tkinter as tk

def FunA():
    
    user_input = entry.get()
    print(user_input)
    
    tk.messagebox.showinfo(title="提示",message="click")
    tk.messagebox.showinfo(title="提示",message=f"你輸入的文字(user_input)")

window = tk.Tk()

window.title("123123123")

window.geometry('300x300')

label = tk.Label(window,text="test")
label.pack()

entry = tk.Entry(window,width = 20)
entry.pack()

button = tk.Button(window,text= "按鈕")
button.pack()

window.mainloop()