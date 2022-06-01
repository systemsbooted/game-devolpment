from tkinter import *

root = Tk()
root.title('name enter')
root.geometry=('600x1000')

e1=Label(text="First Name").grid(row=0)
e2=Label(text="Last Name").grid(row=1)

e1 = Entry()
e2 = Entry()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

myButton=Button(text='submit',width=7,fg='white',bg='green',command='write')
myButton.grid(row=1,column=2)

def write():
	label=Label(text='weel done!')
	label.pack()

root.mainloop()