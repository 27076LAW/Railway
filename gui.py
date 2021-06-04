import tkinter as tk
import os
import simpy
from tkinter import*
#root = Tk()
#root.title("Shell Shop Scheduler")
fields = ('AC_3T', 'Variant 2', 'Variant 3', 'Variant 4')


def makeform(root, fields):
    root.title("Pilot Project on Industry 4.0 implementation for Rail-Coach Manufacturing: MCF Raebareli and IIT Kanpur")
    root.geometry('1000x500')
    root.configure(background='#505160')
    label_0 = Label(root, text="Shell Shop Scheduler", bg='#505160', fg='white', font='Arial 20 bold').pack()
    #label_0 = Label(root, text="Shell Shop Scheduler", padx=5, pady=40, width=20, font=("bold", 20))
    #label_0.place(x=350, y=0)
    entries = {}
    # i = 0
    for field in fields:
        # print(field)
        temp = []
        row = tk.Frame(root)
        #row.configure(background='blue')
        lab = tk.Label(row, width=10, text=field+": ", bg='#336B87', fg='white', font='Arial 16 bold', anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=10)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, 
                 expand=tk.YES, 
                 fill=tk.X)
        temp.append(ent)
        # entries[field] = ent
        label = tk.Label(row, width=10, text="Start Date", bg='#336B87', fg='white', font='Arial 14', anchor='w')
        entry = tk.Entry(row)
        row.configure(background='#336B87')
        label.pack(side=tk.LEFT)
        entry.insert(0,"00-00-0000")
        entry.pack(side=tk.LEFT, 
                 expand=tk.YES,
                 fill=tk.X)

        temp.append(entry)
        label2 = tk.Label(row, width=10, text="Due Date", bg='#336B87', fg='white', font='Arial 14', anchor='w')
        entry2 = tk.Entry(row)
        #entry2.configure(bg='#881000', fg='white', font='Arial 14', anchor='w')
        entry2.insert(0,"00-00-0000")
        label2.pack(side=tk.LEFT)
        entry2.pack(side=tk.LEFT, 
                 expand=tk.YES, 
                 fill=tk.X)
        temp.append(entry2)
        entries[field] = temp
        # start_ = entry.get()
        # print(name)
        # i = i+1
    return entries

def gen_schedule(entries):
    import fact_agent_v2 as fa
    v1 = int(entries['AC_3T'][0].get())
    start_date = entries['AC_3T'][1].get()
    due_date = entries['AC_3T'][2].get()
    fa.order['SWL_AC3T'] = v1
    fa.order['Underframe Complete'] = v1
    #order = {'SWL_AC3T':0, 'Underframe Complete':20, 'EWL_AC3T':0}
    fa.main_loop(start_date,due_date)

def open_distribution():
    os.startfile('distribution_orders.csv')
def open_manufacturing():
    os.startfile('manufacturing_orders.csv')
def open_ac3t():
    os.startfile('Input Data\AC-3T_SW_process final.xlsx')
def open_workstation():
    os.startfile('Input Data\Workstation List.xlsx')
def open_machine_loading():
    os.startfile('machine_loading.html')
def open_gantt_chart():
    os.startfile('gantt_chart.html')

def open_daq_code():
    os.startfile('daqPanel.exe')

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    

    row = tk.Frame(root)
    row.pack(side=tk.TOP,padx=5, pady=5,fill='both')
    row.configure(background='#68829E')
    l0 = tk.Label(row,text="Input Data", bg='#68829E', fg='white', font='Arial 16 bold', anchor='w')
    l0.pack(side=tk.TOP)
    row = tk.Frame(root)
    row.pack(side=tk.TOP,padx=5, pady=5,fill='both')
    row.configure(background='#68829E')
    l0 = tk.Label(row,text="AC_3T", bg='#68829E', fg='white', font='Arial 14', anchor='w')
    l0.pack(side=tk.LEFT)
    b0 = tk.Button(row, text='Process Flow, Operations and Component List', bg='#68829E', fg='white', font='Arial 14', anchor='w', command=(lambda e=ents: open_ac3t()))
    b0.pack(side=tk.LEFT, padx=5, pady=5)
    # b0 = tk.Button(row, text='Operation I/O components',command=(lambda e=ents: open_ac3t()))
    # b0.pack(side=tk.LEFT, padx=5, pady=5)
    b0 = tk.Button(row, text='Machine List', bg='#68829E', fg='white', font='Arial 14', anchor='w', command=(lambda e=ents: open_workstation()))
    b0.pack(side=tk.LEFT, padx=5, pady=5)

    row = tk.Frame(root)
    row.pack(side=tk.TOP)
    b1 = tk.Button(row, text='Generate Schedule', bg='#AEBD38', fg='#598234', font='Arial 16 bold', anchor='w', command=(lambda e=ents: gen_schedule(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)


    row = tk.Frame(root)
    row.pack(side=tk.TOP,padx=5, pady=5,fill='both')
    row.configure(background='#808000')
    l1 = tk.Label(row,text="Outputs", bg='#808080', fg='white', font='Arial 16 bold', anchor='w')
    l1.pack(side=tk.TOP)
    row = tk.Frame(root)
    row.pack(side=tk.TOP,fill=tk.X,padx=5, pady=5)
    # # frame = tk.Frame(root)
    b2 = tk.Button(row, text='Manufacturing Orders', bg='#808000', fg='white', font='Arial 14', anchor='w',command=(lambda e=ents: open_manufacturing()))
    row.configure(background='#808000')
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(row, text='Distribution Orders', bg='#808000', fg='white', font='Arial 14', anchor='w',command=(lambda e=ents: open_distribution()))
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(row, text='Machine Loading Chart', bg='#808000', fg='white', font='Arial 14', anchor='w', command=(lambda e=ents: open_machine_loading()))
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    b4 = tk.Button(row, text='Gantt Chart', bg='#808000', fg='white', font='Arial 14', anchor='w', command=(lambda e=ents: open_gantt_chart()))
    b4.pack(side=tk.LEFT, padx=5, pady=5)

    b5 = tk.Button(row, text='DAQ_Panel', bg='#808000', fg='white', font='Arial 14', anchor='w', command=(lambda e=ents: open_daq_code()))
    b5.pack(side=tk.LEFT, padx=5, pady=5)

    #b2 = tk.Button(root, text='Monthly Payment',
     #      command=(lambda e=ents: monthly_payment(e)))
    #b2.pack(side=tk.LEFT, padx=5, pady=5)
    #b3 = tk.Button(root, text='Quit', command=root.quit)
    #b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
