# from tkinter import *
# import time
# tk=Tk()
#named parameters where the order of the parameters does not matter now 
# canvas=Canvas(tk,width=500,height=500) 
# canvas.pack()
# canvas.create_line(0,0,500,500)
# canvas.create_rectangle(10,10,100,100)
# canvas.create_polygon(10,10,100,10,100,110,fill="",outline='black')
# my_image=PhotoImage(file='photo.png')
# canvas.create_image(0,0,anchor="nw",image=my_image)
# for x in range(0,60):
#     canvas.move(2,5,0)
#     tk.update()
#     time.sleep(0.05)


# def moveTriangle(event):
#     canvas.move(1,5,0)
# canvas.bind_all("<KeyPress-Return>",moveTriangle)
# tk.mainloop()



import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=300)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(0.05)
for y in range(0, 40):
    canvas.move(1, 0, 5)
    tk.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(1, -5, 0)
    tk.update()
    time.sleep(0.05)
for y in range(0, 40):
    canvas.move(1, 0, -5)
    tk.update()
    time.sleep(0.05)