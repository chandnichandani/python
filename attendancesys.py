#import module as m
from Tkinter import * #tkinter is a module use for GUI in python
import time
import datetime
from xlutils.copy import copy 
from xlrd import open_workbook
import xlwt
import os

print "Current date and time: " , datetime.datetime.now()
window = Tk() #window is a variable and Tk() is a class constructor
window.title("Attendance System")
window.geometry('1200x480')


enterPrompt = Label(window, text="Enter your Roll no : ")
# label in GUI takes two arguments one is Tk() variable i.e. window and
# second is text of label

enterPrompt.grid(column=0, row=0) # defines position of label
# for more options in grid : print dir(Label)

rolllabel= Entry(window,width=10)
rolllabel.grid(column=1, row=0)
rolllabel.focus() #focuses the input label


Yourname = Label(window, text="enter your name :")
Yourname.grid(column=0, row=2)

namelabel= Entry(window,width=10)
namelabel.grid(column=1, row=2)
namelabel.focus()

Yourage = Label(window, text="enter your age :")
Yourage.grid(column=0, row=3)

agelabel= Entry(window,width=10)
agelabel.grid(column=1, row=3)
agelabel.focus()

x=str(datetime.datetime.now()).split(" ")[0]
tym=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)
"""
if(os.path.isfile("first.xls")=='false'):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("sheet1")
    sheet1.write(0,0,"roll no")
    sheet1.write(0,1,"name")
    sheet1.write(0,2,"age")
    sheet1.write(0,3,x)   
    book.save("first.xls")
    """

def clicked():
    if(os.path.isfile("first.xls")==False):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet("sheet1")
        sheet1.write(0,0,"roll no")
        sheet1.write(0,1,"name")
        sheet1.write(0,2,"age")
        sheet1.write(0,3,x)   
        book.save("first.xls")
    book_ro = open_workbook("first.xls","r")
    ll=book_ro.sheet_by_index(0)
    book = copy(book_ro)  # creates a writeable copy
    sheet = book.get_sheet(0)
    i=ll.nrows
    a=rolllabel.get()
    b=namelabel.get()
    c=agelabel.get()
    sheet.write(i, 0, a)
    sheet.write(i, 1, b)
    sheet.write(i, 2, c)
    book.save("first.xls")    
btn = Button(window, text="Add to list", bg='#2196F3', command=clicked)
#button create
btn.grid(column=3, row=5)
entt= Label(window, text="ATTENDANCE", width="10")
entt.grid(column=1, row=6)

ent= Label(window, text="Enter your Roll no : ")
ent.grid(column=0, row=7) 

rol= Entry(window,width=10)
rol.grid(column=1, row=7)
rol.focus()


def add():
    book_ro = open_workbook("first.xls","r")
    ll=book_ro.sheet_by_index(0)
    book = copy(book_ro)  # creates a writeable copy
    sheet = book.get_sheet(0)
    i=ll.nrows
    q=ll.ncols
    hit=rol.get()
    rr=0
    flag=0
    for n in range(i):
        vaa=ll.cell(n, 0).value
        print vaa
        if(vaa == hit):
            rr=n
            break
    print rr
    for w in range(q):
        if(ll.cell(0, w).value==x):
            sheet.write(rr,w,x)
            sheet.write(rr,w,tym)
            book.save("first.xls")
            flag=1
    if(flag==0):
        sheet.write(0,q,x)
        sheet.write(rr,q,'1')
        book.save("first.xls")
        

btnn = Button(window, text="Add attendance", bg='#2196F3', command=add)
#button create
btnn.grid(column=5, row=8)
window.mainloop() #mainloop function for displaying window
