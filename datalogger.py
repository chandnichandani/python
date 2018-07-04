#import module as m
from Tkinter import * #tkinter is a module use for GUI in python
import time
import datetime
from xlutils.copy import copy 
from xlrd import open_workbook
import xlwt
import os

#print "Current date and time: " , datetime.datetime.now()
window = Tk() #window is a variable and Tk() is a class constructor
window.title("DATA LOGGER")
window.geometry('1200x480')


enterPrompt=Label(window, text="ultrasonic val")
enterPrompt.grid(column=0, row=0)

show=Label(window)
show.grid(column=1, row=0)

def clicked():
    import requests
    import RPi.GPIO as io
    import time
    from time import sleep

    io.setwarnings(False)

    io.setmode(io.BCM)

    TRIG=27
    ECHO=22
    

    io.setup(TRIG,io.OUT)
    io.setup(ECHO,io.IN)

    def ultra():
             
            io.output(TRIG,False)
            sleep(0.2)

            io.output(TRIG,True)
            sleep(0.00001)

            io.output(TRIG,False)
            
                
            while io.input(ECHO)==0:
                pulse_start=time.time()
            

            while io.input(ECHO)==1:
                pulse_end=time.time()

            t=pulse_end-pulse_start

            d= t * 17150
            
            d= round(d, 2)

            print "d:",d,"cm"
            sleep(0.5)
            return str(d)
    value = ultra()
    print value
    show.configure(text=value+"cm")
    window.configure(background = 'red')
    window.title("calculated")
            #also change other attributes
            #h.sw calculator like windows
def led_on():
    import RPi.GPIO as io
    import time
    from time import sleep
    io.setwarnings(False)

    io.setmode(io.BCM)
    LED=26
    io.setup(LED,io.OUT)
    io.output(LED,True)

def led_off():
    import RPi.GPIO as io
    import time
    from time import sleep
    io.setwarnings(False)

    io.setmode(io.BCM)
    LED=26
    io.setup(LED,io.OUT)
    io.output(LED,False)
    
    
    
btn_ultrasonic = Button(window, text="Enter", bg = "#2196F3", command=clicked)
btn_ultrasonic.grid(column=36, row=360)

btnon = Button(window, text="ON", bg = "#2196F3", command=led_on)
btnon.grid(column=38, row=361)

btnoff = Button(window, text="OFF", bg = "#2196F3", command=led_off)
btnoff.grid(column=38, row=362)



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
    if(os.path.isfile("logger.xls")==False):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet("sheet1")
        sheet1.write(0,0,"Distance")
        #sheet1.write(0,1,"name")
        #sheet1.write(0,2,"age")
        sheet1.write(0,1,x)   
        book.save("logger.xls")
    book_ro = open_workbook("logger.xls","r")
    ll=book_ro.sheet_by_index(0)
    book = copy(book_ro)  # creates a writeable copy
    sheet = book.get_sheet(0)
    i=ll.nrows
    a=show.get()
    #b=namelabel.get()
    #c=agelabel.get()
    sheet.write(i, 0, a)
    book.save("logger.xls")    
btn = Button(window, text="upload data", bg='#2196F3', command=clicked)
#button create
btn.grid(column=3, row=5)
"""
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
        sheet.write(rr,q,tym)
        book.save("first.xls")
        

btnn = Button(window, text="Add attendance", bg='#2196F3', command=add)
#button create
btnn.grid(column=5, row=8)
"""
window.mainloop() #mainloop function for displaying window
