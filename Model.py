from tkinter import *
from tkinter.messagebox import *
import sqlite3

con=sqlite3.Connection('BUS')
cur= con.cursor()
cur.execute('create table if not exists details (bus_id int primary key, bus_type varchar(25), capa int, fare int,  op_id int ,  route_id int, foreign key (op_id) references operator(Op_id))')
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
def p1():
    root.destroy()
    import Main_Menu
def p2():
    if bus_id.get=='':
        showerror('Error','Please enter bus id')
    elif bus_type.get()=='Bus type':
        showerror('Error', 'Please enter bus type')
    elif capa.get()=='':
        showerror('Error', 'Please enter capacity')
    elif fare.get()=='':
        showerror('Error', 'Please enter fare')
    elif op_id.get()=='':
        showerror('Error', 'Please enter operator id')
    elif route_id.get()=='':
        showerror('Error', 'Please enter Route id')
    else:
       cur.execute('insert into details (bus_id , bus_type, capa, fare, op_id, route_id ) values (?,?,?,?,?,?)', (bus_id.get(), bus_type.get(), capa.get(), fare.get(), op_id.get(), route_id.get()))
       con.commit()
       cur.execute('select * from details')
       res=cur.fetchall() 
       print(res)
       showinfo("online bus booking", "Bus Added")
def p3():
    if bus_id.get=='':
        showerror('Error','Please enter bus id')
    elif bus_type.get()=='Bus type':
        showerror('Error', 'Please enter bus type')
    elif capa.get()=='':
        showerror('Error', 'Please enter capacity')
    elif fare.get()=='':
        showerror('Error', 'Please enter fare')
    elif op_id.get()=='':
        showerror('Error', 'Please enter operator id')
    elif route_id.get()=='':
        showerror('Error', 'Please enter Route id')
    else:
        showinfo("online bus booking system", "Bus Updated")
img =PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root, image=img).grid(row=0,columnspan=11)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=1, padx=700,columnspan=10)
Label(root, text='Add bus details', font='Arial 15 bold',bg='Blue', fg='white').grid(row=2,column=1, pady=10, columnspan=10)
Label(root, text = 'Bus ID', font = 'calibre 10 bold').grid(row=3,column=1, pady=10, columnspan=9) 
bus_id=Entry(root)
bus_id.grid(row=3,column=2, columnspan=10)
Label(root, text = 'BUS TYPE', font = 'calibre 10 bold').grid(row=4,column=1, pady=5, columnspan=9) 
bus_type= StringVar()
types = ('AC 2x2', 'AC 3x2', 'Non AC 2x2', 'Non AC 3x2', 'AC Sleeper 2x1','Non AC Sleeper 2x1')
bus_type.set('Bus type')
menu= OptionMenu(root, bus_type, *types)
menu.config(font='calibri 14 bold')
menu["menu"].config(bg='SteelBlue1', font= 'Arial 20')
menu.grid(row=4,column=2, columnspan=10)
Label(root, text = 'Capacity', font = 'calibre 10 bold').grid(row=5,column=1, pady=5, columnspan=9) 
capa=Entry(root)
capa.grid(row=5,column=2, columnspan=10)
Label(root, text = 'Fare', font = 'calibre 10 bold').grid(row=6,column=1, pady=5, columnspan=9) 
fare=Entry(root)
fare.grid(row=6,column=2, columnspan=10)
Label(root, text = 'Operator Id', font = 'calibre 10 bold').grid(row=7,column=1, pady=5, columnspan=9) 
op_id=Entry(root)
op_id.grid(row=7,column=2, columnspan=10)
Label(root, text = 'Route Id', font = 'calibre 10 bold').grid(row=8,column=1, pady=5, columnspan=9) 
route_id=Entry(root)
route_id.grid(row=8,column=2, columnspan=10)
Button(root, text='Add',font='Arial 10 bold', bg='green', fg='white', command=p2).grid(row=9, column =1, pady=10, columnspan=10)
Button(root, text='Edit',font='Arial 10 bold', bg='red', fg='white', command=p3).grid(row=9, column =2, pady=10,columnspan=10)
Button(root, text='Home',font='Arial 10 bold', bg='purple', fg='white', command=p1).grid(row=9, column=3, pady=10,columnspan=10)
root.mainloop()
