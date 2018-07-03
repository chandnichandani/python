from Tkinter import *
window = Tk()

window.title("Pro")
window.geometry('360x480')
window.configure(background = 'white')

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
    
    
    
btn = Button(window, text="Enter", bg = "#2196F3", command=clicked)
btn.grid(column=36, row=360)

btnon = Button(window, text="ON", bg = "#2196F3", command=led_on)
btnon.grid(column=38, row=361)

btnoff = Button(window, text="OFF", bg = "#2196F3", command=led_off)
btnoff.grid(column=40, row=362)



window.mainloop()
