import tkinter as tk
import tkinter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tracker 
import time

from PIL import ImageTk, Image
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tracker import DATES, PRICES, GOODS_OR_SERVICES, EXPENSE_TYPES, EQUITY, DATES_EQ

def create_df_ex():
   df=tracker.CreateDataFrame_ex()
   df1=pd.DataFrame()
   try:
      df['DATES']=pd.to_datetime(df['DATES'], dayfirst = True , format = '%d/%m/%Y')
      df1=df.sort_values(by='DATES')
   except:
      root = tk.Tk()
      label = tk.Label(root, text='DATE PRICE NOT VALID',
                 font=('Times New Roman','35'), fg='red', bg='white')
      label.pack()
      root.overrideredirect(True)
      root.geometry("+300+400")
      root.wm_attributes("-topmost", True)
      root.wm_attributes("-disabled", True)
      root.wm_attributes("-transparentcolor", "white")

      root.after(1000, root.destroy)

   return df1

def create_df_in():
   df=tracker.CreateDataFrame_in()
   df1=pd.DataFrame()
   try:
      df['DATES_STIP']=pd.to_datetime(df['DATES_STIP'], dayfirst = True , format = '%d/%m/%Y')
      df1=df.sort_values(by='DATES_STIP')
   except:
      root = tk.Tk()
      label = tk.Label(root, text='DATE NOT VALID',
                 font=('Times New Roman','35'), fg='red', bg='white')
      label.pack()
      root.overrideredirect(True)
      root.geometry("+300+400")
      root.wm_attributes("-topmost", True)
      root.wm_attributes("-disabled", True)
      root.wm_attributes("-transparentcolor", "white")

      root.after(1000, root.destroy)

   return df1
#create the section where is possible to see the lasts expenses

def show_df():
   df_table = tk.Frame(root) 
   df_table.place(relwidth= 0.5, relheight =0.8, relx=0.45, rely=0.1)

   #l1 = tk.Label(df_table,text="LAST EXPENSES") 
   #l1.pack()
   df=create_df_ex()
   #df=tracker.CreateDataframe_ex_ex()
   cols = list(df.columns)
   tree = ttk.Treeview(df_table, show='headings', height=15)
   tree.pack()
   tree["columns"] = cols
   for i in cols:
      tree.column(i, anchor="w",width=120)
      tree.heading(i, text=i, anchor='w')

   for index, row in df.iterrows():
      tree.insert("", 0, text=index, values=list(row))

   #label space
   ls = tk.Label(df_table,text=" ")
   ls.pack()
   l5 = tk.Label(df_table,text="ENTER YOUR EQUITY: (€)").pack()
   ls = tk.Label(df_table,text=" ")
   ls.pack()
   e5=tk.Entry(df_table, width=20, borderwidth = 5)
   e5.pack()
   ls = tk.Label(df_table,text=" ")
   ls.pack()
   b1=tk.Button(df_table,text='CONFIRM EQUITY',padx=10, pady=5, fg='white',bg="blue", command= lambda : action_equity_button(e5)).pack()

def action_equity_button(e5):
   equity=e5.get()   
   tracker.setEquity(float(equity),EQUITY,DATES_EQ)
   e5.delete(0,tk.END)



def show_df_in():
   df_table = tk.Frame(root) 
   df_table.place(relwidth= 0.5, relheight =0.8, relx=0.45, rely=0.1)

   #l1 = tk.Label(df_table,text="LAST INCOMES") 
   #l1.pack()
   df=create_df_in()
   #df=tracker.CreateDataframe_ex_ex()
   cols = list(df.columns)
   tree = ttk.Treeview(df_table, show='headings', height=8)
   tree.pack()
   tree["columns"] = cols
   for i in cols:
      tree.column(i, anchor="w",width=150)
      tree.heading(i, text=i, anchor='w')

   for index, row in df.iterrows():
      tree.insert("", 0, text=index, values=list(row))
# when the CONFIRM button is pushed ..

def p1_action_CONFIRMbutton(page,e1,e2,e3,e4):
   goodStr=e1.get()
   priceStr=e2.get()
   dateStr=e3.get()
   typeStr=e4.get()
   try:
      priceStr=float(priceStr)
      tracker.addExpenses(goodStr,priceStr,dateStr,typeStr)
   except:
      root = tk.Tk()
      label = tk.Label(root, text='VALUE PRICE NOT VALID',
                 font=('Times New Roman','35'), fg='red', bg='white')
      label.pack()

      root.overrideredirect(True)
      root.geometry("+300+400")
      root.wm_attributes("-topmost", True)
      root.wm_attributes("-disabled", True)
      root.wm_attributes("-transparentcolor", "white")

      root.after(1000, root.destroy)
      #page.after(1000, lambda: l.delete(0, tk.END))
   
   e1.delete(0,tk.END)
   e2.delete(0,tk.END)
   e3.delete(0,tk.END)
   e4.delete(0,tk.END)

def p1_action_CONFIRMbutton_in(page,e1,e2,e3):
   typestr=e1.get()
   moneystr=e2.get()
   dateStr=e3.get()

   try:
      moneyStr=float(moneyStr)
      tracker.addIncomes(typestr,moneystr,dateStr)
   except:
      root = tk.Tk()
      label = tk.Label(root, text='VALUE MONEY NOT VALID',
                 font=('Times New Roman','35'), fg='red', bg='white')
      label.pack()

      root.overrideredirect(True)
      root.geometry("+300+400")
      root.wm_attributes("-topmost", True)
      root.wm_attributes("-disabled", True)
      root.wm_attributes("-transparentcolor", "white")

      root.after(1000, root.destroy)
      #page.after(1000, lambda: l.delete(0, tk.END))
   
   e1.delete(0,tk.END)
   e2.delete(0,tk.END)
   e3.delete(0,tk.END)


def show_Graphs(page):
   df=tracker.CreateDataFrame_ex()
   fig=tracker.graphs(df)
   figure1 =fig[0]
   page_fig1 = tk.Frame(root)
   page_fig1.place(relwidth= 0.37, relheight =0.37, relx=0, rely=0,anchor="nw")
   canvas1 = FigureCanvasTkAgg(figure1, page_fig1)
   canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

   figure4 =fig[3]
   page_fig4 = tk.Frame(root)
   page_fig4.place(relwidth= 0.37, relheight =0.43, relx=1, rely=0,anchor="ne")
   canvas4 = FigureCanvasTkAgg(figure4, page_fig4)
   canvas4.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

   figure3 =fig[2]
   page_fig3 = tk.Frame(root)
   page_fig3.place(relwidth= 0.37, relheight =0.43, relx=0, rely=0.37,anchor="nw")
   canvas3 = FigureCanvasTkAgg(figure3, page_fig3)
   canvas3.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
"""
   figure2 =fig[1]
   page_fig2 = tk.Frame(root)
   page_fig2.place(relwidth= 0.37, relheight =0.43, relx=0, rely=0.4,anchor="nw")
   canvas2 = FigureCanvasTkAgg(figure2, page_fig2)
   canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
"""
   

   
def delete_EX():
   tracker.deleteLastExpense()
def delete_in():
   tracker.deleteLastIncome()

def page1(root):
   window_width  = 1100
   window_height = 600
   #create the inner canvas 
   canvas = tk.Canvas(root, height= window_height, width=window_width, bg='#263D42')
   canvas.pack()

   page = tk.Frame(root)
   page.place(relwidth= 0.3, relheight =0.85, relx=0.05, rely=0.05)
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

   df_table = tk.Frame(root) 
   df_table.place(relwidth= 0.5, relheight =0.85, relx=0.45, rely=0.05)

   l1 = tk.Label(df_table,text="LAST EXPENSES") 
   l1.pack()
   show_df()
   
   #CONFIRM expense button
   exit_button = tk.Button(page,text='CONFIRM',padx=10, pady=5, fg='white',bg="blue", command= lambda : [p1_action_CONFIRMbutton(page,e1,e2,e3,e4),show_df()])
   exit_button.pack()

  #label space
   ls = tk.Label(page,text=" ")
   ls.pack()
  
   #DELETE LAST EXPENSE
   delete_button = tk.Button(page,text='DELETE LAST EXPENSES',padx=30, pady=5, fg='white',bg="red", command= lambda : [delete_EX(),show_df()])
   delete_button.pack()

   #exit button
   exit_button = tk.Button(page,text='Exit',command=lambda: page.quit(),padx=10, pady=5, fg='white',bg="#263D42")
   exit_button.pack(side = 'bottom',fill=tk.X)

   #SHOW INCOME
   b1=tk.Button(page, text = '-->', command = lambda : [changepage(2),show_df_in()] , padx=10, pady=5,fg='white',bg="#263D42")
   b1.pack(side = 'bottom',fill=tk.X)

   #SHOW GRAPHS
   b1=tk.Button(page, text = '<--', command = lambda : changepage(3),padx=10, pady=5,fg='white',bg="#263D42")
   b1.pack(side = 'bottom',fill=tk.X)

   


def page2(root):
   window_width  = 1100
   window_height = 600
   #create the inner canvas 
   canvas = tk.Canvas(root, height= window_height, width=window_width, bg='#263D42')
   canvas.pack()

   page = tk.Frame(root)
   page.place(relwidth= 0.3, relheight =0.85, relx=0.05, rely=0.05)
   # title
   l=tk.Label(page, text = "INSERT THE INCOMES", fg="green").pack()

   #insert TYPE
   myLabel1 = tk.Label(page,text="TYPE")
   e1=tk.Entry(page, width=20, borderwidth = 5)
   
   myLabel1.pack()
   e1.pack()
   goodStr=e1.get()

   #insert MONEY
   myLabel2 = tk.Label(page,text="MONEY (€)")
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

   #label space
   ls = tk.Label(page,text=" ")
   ls.pack()

   df_table = tk.Frame(root) 
   df_table.place(relwidth= 0.5, relheight =0.85, relx=0.45, rely=0.05)

   l1 = tk.Label(df_table,text="LAST INCOMES") 
   l1.pack()


   #CONFIRM expense button
   exit_button = tk.Button(page,text='CONFIRM',padx=10, pady=5, fg='white',bg="blue", command= lambda : [p1_action_CONFIRMbutton_in(page,e1,e2,e3),show_df_in()])
   exit_button.pack()

  #label space
   ls = tk.Label(page,text=" ")
   ls.pack()
  
   #DELETE LAST EXPENSE
   delete_button = tk.Button(page,text='DELETE LAST INCOMES',padx=30, pady=5, fg='white',bg="green", command= lambda : [delete_in(),show_df_in()])
   delete_button.pack()

   #exit button
   exit_button = tk.Button(page,text='Exit',command=lambda: page.quit(),padx=10, pady=5, fg='white',bg="#263D42")
   exit_button.pack(side = 'bottom',fill=tk.X)

   #SHOW LAST EXPENSES
   #b1=tk.Button(page, text = 'SHOW LAST INCOMES', command = show_df_in, padx=10, pady=5,fg='white',bg="#263D42")
   #b1.pack(side = 'bottom',fill=tk.X)

   #SHOW GRAPHS
   b1=tk.Button(page, text = '-->', command = lambda : changepage(3),padx=10, pady=5,fg='white',bg="#263D42")
   b1.pack(side = 'bottom',fill=tk.X)

   #SHOW INCOME
   b1=tk.Button(page, text = '<--', command =lambda : [changepage(1),show_df()], padx=10, pady=5,fg='white',bg="#263D42")
   b1.pack(side = 'bottom',fill=tk.X)


def page3(root):
   window_width  = 1100
   window_height = 600

   #create the inner canvas 
   canvas = tk.Canvas(root, height= window_height, width=window_width, bg='#263D42')
   canvas.place(relwidth= 1, relheight =1, relx=1, rely=1,anchor="ne")
   page = tk.Frame(root)
   show_Graphs(page)

    # exit button
   exit_button = tk.Button(root,text='Exit',command=lambda: root.quit(),padx=10, pady=5, fg='white',bg="#263D42")
   exit_button.pack(side = 'bottom', fill=tk.X)

   #To page 1
   b1=tk.Button(root, text = '-->', command = lambda : [changepage(1),show_df()],padx=10, pady=5, fg='white',bg="#263D42")
   b1.pack(side = 'bottom', fill=tk.X)

   #SHOW INCOME
   b2=tk.Button(root, text = '<--', command =lambda :[changepage(2),show_df_in()], padx=10, pady=5,fg='white',bg="#263D42")
   b2.pack(side = 'bottom',fill=tk.X)



def changepage(n):
   global pagenum, root
   for widget in root.winfo_children():
      widget.destroy()
   if pagenum == 1 and n==2:
     page2(root)
     pagenum = 3
   if pagenum == 1 and n==3:
     page3(root)
     pagenum = 3

   if pagenum == 2 and n==1:
     page1(root)
     pagenum = 1
   if pagenum == 2 and n==3:
     page3(root)
     pagenum = 3

   if pagenum == 3 and n==1:
     page1(root)
     pagenum = 1
   if pagenum == 3 and n==2:
     page2(root)
     pagenum = 2


pagenum = 1
root = tk.Tk()
root.title('Expense Tracker DEMO')
window_width  = 1100
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
root.resizable(True, True)
root.mainloop()