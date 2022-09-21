from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title('Expenses Tracker')
root.iconbitmap('C:/Users/messo/Documents/MyProject_Tracker2')
root.geometry('600x400+50+50')

myLabel1 = Label(root,text="GOOD")
myLabel1.grid(row=0,column=0)
e1=Entry(root, width=20, borderwidth = 5)
e1.grid(row=1,column=0)

myLabel2 = Label(root,text="PRICE ($)")
myLabel2.grid(row=0,column=21)
e2=Entry(root, width=20, borderwidth = 5)
e2.grid(row=1,column=21)

myLabel3 = Label(root,text="DATE (dd/mm/yyyy)")
myLabel3.grid(row=0,column=41)
e2=Entry(root, width=20, borderwidth = 5)
e2.grid(row=1,column=41)

myLabel4 = Label(root,text="TYPE")
myLabel4.grid(row=0,column=61)
e2=Entry(root, width=20, borderwidth = 5)
e2.grid(row=1,column=61)
"""
my_img = ImageTk.PhotoImage(Image.open("salary.png"))
my_label = Label(image=my_img)
my_label.pack()
"""
#e=Entry(root, width=50, borderwidth = 5)
#e.pack()

button_quit = Button(root, text = "Quit", command = root.quit)
button_quit.grid(row=3,column=40)

"""
def myClick():
	myLabel=Label(root, text=e.get())
	myLabel.pack()

# creating a label widget
myLabel1 = Label(root,text="Hello World")
myLabel2 = Label(root,text="Hello World")

#create entry

e=Entry(root, width=50, borderwidth = 5)
e.pack()


# crete button
button = Button(root, text = "Enter name",padx=50,pady=20, command=myClick, fg="blue",bg="yellow")
#Showing it onto screen
#myLabel1.grid(row=0,column=0)
button.pack()
"""
def graphs():
   car_prices=np.random.normal(100000, 5000, 1000)
   plt.hist(car_prices, 20)
   plt.show()

#Create a button to show the plot
button_graph=Button(root, text= "Show Graph", command= graph)
button_graph.grid(row=2,column=40)
root.mainloop()