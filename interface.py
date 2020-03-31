import tkinter as tk
import subprocess
import os
root= tk.Tk()
root.title('ICG Generator-PCD Package')
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, width=300, height=200, window=entry1)

def run ():
    x1 = entry1.get()
    print(x1)
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(600, 230, window=label1)
    
button1 = tk.Button(text='Get the ICG', command=run).pack()
canvas1.create_window(200, 500, width=454, height=20, window=button1)

root.mainloop()
