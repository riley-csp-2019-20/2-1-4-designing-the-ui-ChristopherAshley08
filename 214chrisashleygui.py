import tkinter as tk

#main window
root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

background1 = "blue"
background2 = "green"
background3 = "red"
background4 = "yellow"

p = tk.Canvas(background=background1,height=100,width=100)
p.grid(row=0,column=0)

b = tk.Canvas(background=background2,height=100,width=100)
b.grid(row=0,column=1)

c = tk.Canvas(background=background3,height=100,width=100)
c.grid(row=1,column=0)

d = tk.Canvas(background=background4,height=100,width=100)
d.grid(row=1,column=1)

root.mainloop()