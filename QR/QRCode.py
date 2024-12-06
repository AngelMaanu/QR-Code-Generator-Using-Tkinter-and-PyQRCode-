import tkinter as tk
from tkinter import messagebox
import pyqrcode as py

tab = tk.Tk()

tab.title('Qr_Code Generator')
tab.geometry('600x500')
tab.configure(background='yellow')

a = tk.StringVar()
b = tk.DoubleVar()
c = tk.StringVar()

l1 = tk.Label(tab, text="Enter your name", font=('times new roman', 20, 'italic',), bg='gray')
l1.place(x=50, y=50)
e1 = tk.Entry(tab, textvariable=a, font=('times new roman', 20, 'italic'))
e1.place(x=300, y=50)

l2 = tk.Label(tab, text="Enter your mark: ", font=('times new roman', 20, 'italic',), bg='gray')
l2.place(x=50, y=100)
e2 = tk.Entry(tab, textvariable=b, font=('times new roman', 20, 'italic'))
e2.place(x=300, y=100)

l3 = tk.Label(tab, text="Enter your Dept", font=('times new roman', 20, 'bold'), bg='#1fd400')
l3.place(x=50, y=150)
e3 = tk.Entry(tab, textvariable=c, font=('times new roman', 20, 'italic'))
e3.place(x=300, y=150)


def add():
    name = a.get()
    mark = b.get()
    dept = c.get()
    data = py.create(f"My name is:{name}\nMy Mark:{mark}\nDepartmet:{dept}")
    data.svg('qr.svg', scale=10)
    # os.startfile('qr.svg')
    messagebox.showinfo(title="QrCode", message='Qr Code Generate Successfully')


def cancel():
    a.set('')
    b.set('')
    c.set('')


b1 = tk.Button(tab, text='QR', font=('times new roman', 20, 'bold'), bg='pink', command=add)
b1.place(x=80, y=200)
b2 = tk.Button(tab, text='Clear', font=('times new roman', 20, 'bold'), bg='green', command=cancel)
b2.place(x=200, y=200)
tab.mainloop()
