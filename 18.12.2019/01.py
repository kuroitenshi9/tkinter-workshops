import tkinter
from tkinter.colorchooser import *

def color_label(lab):
	color = tkinter.colorchooser.askcolor(parent=top)
	print(color)
	lab.configure(bg=color[1])

top = tkinter.Tk()
top.wm_title('Hello...')

#wpływamy na wielkość
# top.resizable(width='true', height='false')
# top.minsize(width=200, height=50)
# top.maxsize(width=200, height=50)

frame1 = tkinter.Frame(top, borderwidth=2, relief='ridge', pady=4, padx=4)
# frame1.pack(fill='y', side='left')
frame1.grid(row=0,column=0, sticky='ns')

frame2 = tkinter.Frame(top, borderwidth=2, relief='groove', pady=4, padx=4)
# frame2.pack(fill='y', side='left')
frame2.grid(row=0,column=1,sticky='ns')


frame3 = tkinter.Frame(top, borderwidth=2, relief='groove', pady=4, padx=4)
# frame3.pack(fill='y', side='left')
frame3.grid(row=1,column=0, sticky='ew', columnspan=2)



label1 = tkinter.Label(frame1, text='Hello world', bg='pink') #co ma być w środku
label1.pack() #wrzuć to do środka

b_close = tkinter.Button(frame2, text="Zamknij", command=top.destroy, bg='pink')
b_close.pack(fill='x')

b_color = tkinter.Button(frame3, text='kolor', command=lambda: color_label(label1))
b_color.pack(fill='x')

top.mainloop()