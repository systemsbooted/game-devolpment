from tkinter import *

root = Tk()
root.geometry('1200x2000')
root.title('Data Storage')
root.iconbitmap('server-icon-vector-sign-symbol-isolated-white-background-server-icon-vector-isolated-white-background-your-web-133761922.ico')
root.configure(bg='black')
label=Label(text='Storage Master',font=('calbri',40),fg='white',bg='black')
label.pack()
button=Button(text='save files',font=('calbri',10),width=20,bg='grey',fg='white',padzy=10,relief='grove')
button.pack()
root.mainloop()