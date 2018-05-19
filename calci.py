from Tkinter import * #tkinter is a module use for GUI in python

window = Tk() #window is a variable and Tk() is a class constructor
window.title("Calci")
window.geometry('250x280')
window.configure(background = 'gray')
v=StringVar()

outputlabel= Entry(window, width=30, bg="white", textvariable=v)
outputlabel.grid(column=0, row=0, columnspan=3)
outputlabel.focus()
a= []
b= []
x=0
def clicked1():
    v.set('1')
    x=v.get()
    
    a.append(x)
    print a
    #outputlabel.configure(text=x)
    #val1=outputlabel.get()
def clicked2():
    v.set('2')
    x=v.get()
    
    a.append(x)
    print a
    #x='2'
    #outputlabel.configure(text=x)
   # val2=outputlabel.get()
def clicked3():
    v.set('3')
    x=v.get()
    
    a.append(x)
    print a
    """x='3'
    outputlabel.configure(text=x)"""
def clicked4():
    v.set('4')
    x=v.get()
    
    a.append(x)
    print a
def clicked5():
    v.set('5')
    x=v.get()
    
    a.append(x)
    print a
def clicked6():
    v.set('6')
    x=v.get()
    
    a.append(x)
    print a
def clicked7():
    v.set('7')
    x=v.get()
    
    a.append(x)
    print a
def clicked8():
    v.set('8')
    x=v.get()
    
    a.append(x)
    print a
def clicked9():
    v.set('9')
    x=v.get()
    
    a.append(x)
    print a
def clickeddot():
    v.set('.')
    x=v.get()
    a.append(x)
    print a
def clicked0():
    v.set('0')
    x=v.get()
    a.append(x)
    print a
def clickedhash():
    v.set('#')
    x=v.get()
    a.append(x)
    print a
def clickedplus():
    v.set('+')
    x=v.get()
    a.append(x)
    print a
def clickedminus():
    v.set('-')
    x=v.get()
    a.append(x)
    print a
def clickeddiv():
    v.set('/')
    x=v.get()
    a.append(x)
    print a
def clickedmul():
    v.set('x')
    x=v.get()
    a.append(x)
    print a
def results():
    num= len(a)
    for i in range(num):
        if(a[i]=='+'):
          val1= "".join(a[0:i])
          val1=int(val1)
          print val1
          val2= "".join(a[i+1:])
          val2=int(val2)
          print val2
          c= val1 + val2
          c=str(c)
          break
        if(a[i]=='-'):
          val1= "".join(a[0:i])
          val1=int(val1)
          print val1
          val2= "".join(a[i+1:])
          val2=int(val2)
          print val2
          c= val1 - val2
          c=str(c)
          break
        if(a[i]=='/'):
          val1= "".join(a[0:i])
          val1=int(val1)
          print val1
          val2= "".join(a[i+1:])
          val2=int(val2)
          print val2
          c= val1 / val2
          c=str(c)
          break
        if(a[i]=='x'):
          val1= "".join(a[0:i])
          val1=int(val1)
          print val1
          val2= "".join(a[i+1:])
          val2=int(val2)
          print val2
          c= val1 * val2
          c=str(c)
          break
    v.set(c)
    del a[:]
    #print num
res = Button(window, text="=", width="7", height="3", command=results)
res.grid(column=4, row=0)

valueone = Button(window, text="1", width="7", height="3", command=clicked1)
valueone.grid(column=0, row=4) 

valuesecond = Button(window, text="2", width="7", height="3", command=clicked2)
valuesecond.grid(column=1, row=4)

value3 = Button(window, text="3", width="7", height="3", command=clicked3)
value3.grid(column=2, row=4)

value4 = Button(window, text="4", width="7", height="3", command=clicked4)
value4.grid(column=0, row=5) 

value5 = Button(window, text="5", width="7", height="3", command=clicked5)
value5.grid(column=1, row=5)

value6 = Button(window, text="6", width="7", height="3", command=clicked6)
value6.grid(column=2, row=5)

value7 = Button(window, text="7", width="7", height="3", command=clicked7)
value7.grid(column=0, row=6) 

value8 = Button(window, text="8", width="7", height="3", command=clicked8)
value8.grid(column=1, row=6)

value9 = Button(window, text="9", width="7", height="3", command=clicked9)
value9.grid(column=2, row=6) 

valuestar = Button(window, text=".", width="7", height="3", command=clickeddot)
valuestar.grid(column=0, row=7) 

value0 = Button(window, text="0", width="7", height="3", command=clicked0)
value0.grid(column=1, row=7)

valuehash = Button(window, text="#", width="7", height="3", command=clickedhash)
valuehash.grid(column=2, row=7)

valueadd = Button(window, text="+", width="7", height="3", command=clickedplus)
valueadd.grid(column=4, row=4)
valuesub = Button(window, text="-", width="7", height="3", command=clickedminus)
valuesub.grid(column=4, row=5)
valuediv = Button(window, text="/", width="7", height="3", command=clickeddiv)
valuediv.grid(column=4, row=6)
valuemul = Button(window, text="x", width="7", height="3", command=clickedmul)
valuemul.grid(column=4, row=7) 

window.mainloop() #mainloop function for displaying window
