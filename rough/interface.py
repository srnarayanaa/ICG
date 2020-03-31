import os
cmd1 = './a.out test1.c'
cmd2 = './a.out test2.c'
cmd3 = './a.out test3.c'
cmd4 = './a.out test4.c'
cmd5 = './a.out test5.c'
cmd6 = './a.out test6.c'

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title('PCD PACKAGE TEST VERSION')
top.geometry("500x350")

def test1():
   os.system(cmd1)

def test2():
   os.system(cmd2)

def test3():
   os.system(cmd3)

def test4():
   os.system(cmd4)

def test5():
   os.system(cmd5)

def test6():
   os.system(cmd6)



B1 = Button(top, text = "Test Case 1", command = test1)
B2 = Button(top, text = "Test Case 2", command = test2)
B3 = Button(top, text = "Test Case 3", command = test3)
B4 = Button(top, text = "Test Case 4", command = test4)
B5 = Button(top, text = "Test Case 5", command = test5)
B6 = Button(top, text = "Test Case 6", command = test6)
B1.place(x = 50,y = 50)
B2.place(x = 50,y = 90)
B3.place(x = 50,y = 130)
B4.place(x = 50,y = 170)
B5.place(x = 50,y = 210)
B6.place(x = 50,y = 250)
top.mainloop()