import tkinter  as tk 
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

my_w = tk.Tk()
my_w.geometry("380x200")  
sel=tk.StringVar() # declaring string variable 

cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.grid(row=1,column=1,padx=20)

def my_upd(*args): # triggered when value of string varaible changes
    if(len(sel.get())>4):
        l1.config(text=sel.get()) # read and display date
        dob = datetime.strptime(sel.get(),'%m/%d/%y')
        dt=date.today()
        dt3=relativedelta(dt,dob)
        l2.config(text="Dayes:" + str(dt3.days) +"\n Months:"+ str(dt3.months) + "\n Years:"+ str(dt3.years) )
        print("Dayes:",dt3.days," Months:",dt3.months," Years:", dt3.years)
l1=tk.Label(my_w,bg='yellow')  # Label to display date 
l1.grid(row=1,column=2)

l2=tk.Label(my_w)  # Label to display date 
l2.grid(row=1,column=3,padx=10)

sel.trace('w',my_upd) # on change of string variable 
my_w.mainloop()