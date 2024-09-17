from tkinter import *

tk=Tk()
#named parameters where the order of the parameters does not matter now 
canvas=Canvas(tk,width=500,height=500) 
canvas.pack()
# canvas.create_line(0,0,500,500)
# canvas.create_rectangle(10,10,100,100)
#canvas.create_polygon(10,10,100,10,100,110,fill="",outline='black')
my_image=PhotoImage(file='photo.png')
canvas.create_image(0,0,anchor="nw",image=my_image)
tk.mainloop()