import tkinter

top = tkinter.Tk()

top.minsize(width=300, height=300)
top.maxsize(width=300, height=300)

button1 = tkinter.Button(top, text="B")
# button1.place(x=30, y=30, anchor="center") #położenie
button1.place(relx=0.5, rely=0.0, anchor="center") #zamiast anchor mogą być strony świata n,s,w,e

button2 = tkinter.Button(top, text="BUTTON")
button2.pack()

top.mainloop()