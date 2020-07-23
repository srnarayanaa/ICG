import os
cmd1 = './a.out simple'
cmd2 = './a.out if'
cmd3 = './a.out ifelse'
cmd4 = './a.out nestedif'
cmd5 = './a.out while'
cmd6 = './a.out whileif'

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title('PCD PACKAGE TEST VERSION')
top.geometry("500x350")

def test1():
	os.system(cmd1)
	file_o=open("output")
	content=file_o.read()  
	print(content)                        
	file_o.close()

def test2():
	os.system(cmd2)
	file_o=open("output")
	content=file_o.read()  
	print(content)                        
	file_o.close()

def test3():
	os.system(cmd3)
	file_o=open("output")
	content=file_o.read()  
	print(content)                        
	file_o.close()

def test4():
	os.system(cmd4)
	file_o=open("output")
	content=file_o.read()  
	print(content)                        
	file_o.close()

def test5():
	os.system(cmd5)
	file_o=open("output")
	content=file_o.read()  
	print(content)                        
	file_o.close()

def test6():
	os.system(cmd6)
	file_o=open("output")
	content=file_o.read()  
	print(content)                        
	file_o.close()



B1 = Button(top, text = "SIMPLE", command = test1)
B2 = Button(top, text = "IF", command = test2)
B3 = Button(top, text = "IF ELSE ", command = test3)
B4 = Button(top, text = "NESTED IF", command = test4)
B5 = Button(top, text = "WHILE", command = test5)
B6 = Button(top, text = "WHILE IF", command = test6)
B1.place(x = 50,y = 50)
B2.place(x = 50,y = 90)
B3.place(x = 50,y = 130)
B4.place(x = 50,y = 170)
B5.place(x = 50,y = 210)
B6.place(x = 50,y = 250)
top.mainloop()
