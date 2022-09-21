# This projects aim to create an appplication for tracking expenses 

import numpy as np
import datetime as date
import pandas as pd
import matplotlib.pyplot as plt
import random
from tabulate import tabulate

#Create empty lists
GOODS_OR_SERVICES = []
PRICES =[]
DATES =[]
EXPENSE_TYPES = []

# Create a function to add to list an expenses
def addExpenses (good_or_service,price,date,expense_type):
	GOODS_OR_SERVICES.append(good_or_service)
	PRICES.append(price)
	DATES.append(date)
	EXPENSE_TYPES.append(expense_type)

def CreateDataFrame ():
	expense_report = pd.DataFrame()
	expense_report['GOODS'] = GOODS_OR_SERVICES
	expense_report['PRICE'] = PRICES
	expense_report['DATES'] = DATES
	expense_report['EXPENSE_TYPES'] = EXPENSE_TYPES
	sorted_expense_report = expense_report.sort_values(by='DATE')
	#print(tabulate(expense_report, headers='keys', tablefmt='psql'))
	#print(sum(expense_report.loc[:,'PRICE']))
	return expense_report


def dataFrameTest_Year():
	num_of_ex = 100
	Goods=["Mela","Pera","Banana","Carne","Acqua","cena","PC","telefono"]
	Price=[5,5,10,15,0.5,40,800,1000]
	Expenses_type=["Alimentari","Tecnologia"]
	for i in range(num_of_ex):
		date=str(random.randint(1,28))+"/"+ str(random.randint(1,12)) + "/"+"2022"
		addExpenses(Goods[random.randint(0,7)],Price[random.randint(0,7)],date,Expenses_type[random.randint(0,1)])
	df = CreateDataFrame()
	df['DATES']=pd.to_datetime(df['DATES'], dayfirst = True , format = '%d/%m/%Y', exact=True)
	df1=df.sort_values(by='DATES')
	return df1

def graphs(df):
	df2.plot(kind='bar',x='GOODS',y="PRICES")
	plt.show()





"""
# This function return 1 if date1 in string format dd/mm/yyyy is after date2
#				return 0 if date1 in string format dd/mm/yyyy is equal date2
#				return -1 if date1 in string format dd/mm/yyyy is equal date2
def Date_isgreater(Date1,Date2):
	strDate1= Date1.split("/") #parsing date 1
	strDate2= Date2.split("/") #parsing date 2
	years= int(strDate1[2]) > int(strDate2[2])
	yearsAndMonth = int(strDate1[2]) == int(strDate2[2]) and int(strDate1[1]) > int(strDate2[1])
	yearsAndMonthAndDay = int(strDate1[2]) == int(strDate2[2]) and int(strDate1[1]) == int(strDate2[1]) and int(strDate1[0]) > int(strDate2[0])
	if  years or yearsAndMonth or yearsAndMonthAndDay:
		return 1
	elif (int(strDate1[2]) == int(strDate2[2]) and int(strDate1[1]) == int(strDate2[1]) and int(strDate1[0]) == int(strDate2[0])):
		return 0
	else:
		return -1

def orderDate(DateList):
	for i  in range(len(DateList)-1):
		if Date_isgreater(DateList[i],DateList[i+1]) == 1:
			DateList[i],DateList[i+1] = DateList[i+1],DateList[i]
	return DateList
"""


#todaydate= date.datetime.now()
#addExpenses('Mela',int('1'),todaydate.strftime("%d/%d/%Y"),'Alimentari')
#addExpenses('Banana',int('2'),todaydate.strftime("%d/%d/%Y"),'Alimentari')
#ShowExpenses()
"""
table_ex=dataFrameTest_Year()
print(tabulate(table_ex, headers='keys', tablefmt='psql'))
#order_DATES=orderDate(table_ex.loc[:,"DATE"])
#order_DATES=orderDate(["12/2/2012","19/09/1998","20/09/1998"])
#print(order_DATES)

start_date = "1/1/2022"
end_date = "30/1/2022"
df2=table_ex.loc[(table_ex["DATE"] >= start_date) & (table_ex["DATE"] <= end_date)]
df2['DATE']=pd.to_datetime(df2['DATE'], dayfirst=False, format="%d/%m/%Y")
print(tabulate(df2, headers='keys', tablefmt='psql'))
df2.plot(kind='bar',x='DATE',y="PRICE")
plt.show()
"""

"""

ET_plot0 = table_ex[['EXPENSE_TYPE','PRICE']]

ET_plot=ET_plot0.groupby(['EXPENSE_TYPE']).sum()
print(tabulate(ET_plot, headers='keys', tablefmt='psql'))

ET_plot.plot.bar()
plt.show()
#plt.plot(x='GOODS',y="PRICE")
#plt.show()
# Main program

"""
