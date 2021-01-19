from tkinter import *
from tkinter import messagebox
from todoModel import *

def donothing():
   x = 0

def newTask():
    task = my_entry.get()
    if task != "":
        action(task)
        my_list.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please some enter task.")

def searchTask():
    pass

def deleteTask():
    my_list.delete(ANCHOR)

def loadTask():
    tsk = loadingTask()
    my_list.delete(0, "end")
    my_list.insert(END, tsk)
    


   
ws = Tk()
ws.geometry('500x400')
ws.title('ToDo Application')

mb = Menu(ws)
opt = Menu(mb, tearoff=0)
opt.add_command(label="New Task", command=donothing)
opt.add_command(label="View Tasks", command=donothing)
opt.add_command(label="Exit", command=ws.quit)

mb.add_cascade(label="Menu", menu=opt)
ws.config(menu=mb)

frame = Frame(ws)
frame.pack()

my_list = Listbox(
    frame,
    width=25,
    height=5,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"
)
my_list.pack(side=LEFT, fill=BOTH)

stuff = ['Eat apple', 'drink water', 'go gym', 'write software', 'write documentation', 'take a nap']

for item in stuff:
    my_list.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=sb.set)
sb.config(command=my_list.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

btn1 = Button(
    button_frame,
    text='Add Task',
    command=newTask
)
btn1.pack(fill=BOTH, expand=True, side=LEFT)

btn2 = Button(
    button_frame,
    text='Delete Task',
    command=deleteTask
)
btn2.pack(fill=BOTH, expand=True, side=LEFT)

btn3 = Button(
    button_frame,
    text='Search Task',
    command=searchTask
)
btn3.pack(fill=BOTH, expand=True, side=LEFT)

btn4 = Button(
    button_frame,
    text='Load Task',
    command=loadTask
)
btn4.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()