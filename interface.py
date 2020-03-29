import tkinter as tk
import subprocess
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, width=454, height=200, window=entry1)

def getSquareRoot ():
    x1 = entry1.get()
    print(x1)
    subprocess.run(["ls"])
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(600, 230,width=454, height=20, window=label1)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot).pack()
canvas1.create_window(200, 500, width=454, height=20, window=button1)

    
root.mainloop()
