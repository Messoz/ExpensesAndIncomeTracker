import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
import tracker 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tracker import DATES, PRICES, GOODS_OR_SERVICES, EXPENSE_TYPES

def show_df():
   page2 = tk.Frame(root)
   page2.place(relwidth= 0.5, relheight =0.8, relx=0.45, rely=0.1)
   myLabel1 = tk.Label(page2,text="LAST EXPENSES")
   myLabel1.pack()
   df=tracker.CreateDataFrame()
   cols = list(df.columns)
   tree = ttk.Treeview(page2, show='headings', height=8)
   tree.pack()
   tree["columns"] = cols
   for i in cols:
      tree.column(i, anchor="w",width=100)
      tree.heading(i, text=i, anchor='w')

   for index, row in df.iterrows():
      tree.insert("",0,text=index,values=list(row))

def p1_action_CONFIRMbutton(e1,e2,e3,e4):
   goodStr=e1.get()
   priceStr=e2.get()
   dateStr=e3.get()
   typeStr=e4.get()
   tracker.addExpenses(goodStr,float(priceStr),dateStr,typeStr)
   e1.delete(0,tk.END)
   e2.delete(0,tk.END)
   e3.delete(0,tk.END)
   e4.delete(0,tk.END)

def show_Expenses(page):
   df=tracker.CreateDataFrame()
   fig=tracker.graphs(df)
   figure1 =fig[0]
   page_fig1 = tk.Frame(root)
   page_fig1.place(relwidth= 0.3, relheight =0.3, relx=0.1, rely=0.1,anchor="nw")
   canvas1 = FigureCanvasTkAgg(figure1, page_fig1)
   canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

   figure2 =fig[1]
   page_fig2 = tk.Frame(root)
   page_fig2.place(relwidth= 0.3, relheight =0.3, relx=0.1, rely=0.4,anchor="nw")
   canvas2 = FigureCanvasTkAgg(figure2, page_fig2)
   canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
   

"""
   
"""


def page1(root):

   window_width  = 1000
   window_height = 600
   #create the inner canvas 
   canvas = tk.Canvas(root, height= window_height, width=window_width, bg='#263D42')
   canvas.pack()

   page = tk.Frame(root)
   page.place(relwidth= 0.3, relheight =0.8, relx=0.1, rely=0.1)
   # title
   l=tk.Label(page, text = "INSERT THE EXPENSES", fg="red").pack()

   #insert GOOD
   myLabel1 = tk.Label(page,text="GOOD")
   e1=tk.Entry(page, width=20, borderwidth = 5)
   

   myLabel1.pack()
   e1.pack()
   goodStr=e1.get()

   #insert PRICE
   myLabel2 = tk.Label(page,text="PRICE (€)")
   e2=tk.Entry(page, width=20, borderwidth = 5)
   
   myLabel2.pack()
   e2.pack()
   priceStr=e2.get()

   #insert DATE
   myLabel3 = tk.Label(page,text="DATE (dd/mm/yyyy)")
   e3=tk.Entry(page, width=20, borderwidth = 5)

   myLabel3.pack()
   e3.pack()
   dateStr=e3.get()
   

   #insert TYPE
   myLabel4 = tk.Label(page,text="TYPE")
   e4=tk.Entry(page, width=20, borderwidth = 5)

   myLabel4.pack()
   e4.pack()
   typeStr=e4.get()

   #label space
   ls = tk.Label(page,text=" ")
   ls.pack()

   #CONFIRM expense button
   exit_button = tk.Button(page,text='CONFIRM',padx=10, pady=5, fg='white',bg="blue", command= lambda : [p1_action_CONFIRMbutton(e1,e2,e3,e4),show_df()])
   exit_button.pack()
  

   #exit button
   exit_button = tk.Button(page,text='Exit',command=lambda: page.quit(),padx=10, pady=5, fg='white',bg="#263D42")
   exit_button.pack(side = 'bottom',fill=tk.X)

   #SHOW LAST EXPENSES
   b1=tk.Button(page, text = 'SHOW LAST EXPENSES', command = show_df, padx=10, pady=5,fg='white',bg="#263D42")
   b1.pack(side = 'bottom',fill=tk.X)

   #SHOW GRAPHS
   b1=tk.Button(page, text = 'SHOW GRAPHS', command = changepage,padx=10, pady=5,fg='white',bg="#263D42")
   b1.pack(side = 'bottom',fill=tk.X)

   

   



def page2(root):
   window_width  = 1000
   window_height = 600

   #create the inner canvas 
   canvas = tk.Canvas(root, height= window_height, width=window_width, bg='#263D42')
   canvas.pack()

   page = tk.Frame(root)
   page.place(relwidth= 0.8, relheight =0.8, relx=0.1, rely=0.1)

   # title
   #l=tk.Label(page, text = "GRAPHS", fg="red")
   #l.pack()

   # exit button
   refresh_button = tk.Button(page,text='Refresh',command=show_Expenses(page),padx=10, pady=5, fg='white',bg="#263D42")
   refresh_button.pack()

   # exit button
   exit_button = tk.Button(page,text='Exit',command=lambda: root.quit(),padx=10, pady=5, fg='white',bg="#263D42")
   exit_button.pack(side = 'bottom', fill=tk.X)

   #To page 1
   b1=tk.Button(page, text = 'INSERT EXPENSES', command = changepage,padx=10, pady=5, fg='white',bg="#263D42")
   b1.pack(side = 'bottom', fill=tk.X)


def changepage():
    global pagenum, root
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2(root)
        pagenum = 2
    else:
        page1(root)
        pagenum = 1


pagenum = 1
root = tk.Tk()
root.title('Expense Tracker DEMO')
window_width  = 1000
window_height = 600
#root.geometry( str(window_width) + 'x' + str(window_height))
#root.resizable(0, 0)

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = tk.Canvas(root, height= window_height, width=window_width, bg='#263D42')

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('C:/Users/messo/Documents/MyProject_Tracker2/Salaryico.ico')

page1(root)
root.mainloop()