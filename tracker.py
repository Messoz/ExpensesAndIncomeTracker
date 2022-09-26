# This projects aim to create an appplication for tracking expenses 
import tkinter as tk
import numpy as np
import datetime as date
import pandas as pd
import matplotlib.pyplot as plt
import random
import matplotlib.dates as mdates
import numpy as np
from time import strftime,localtime
import datetime as dt
from tabulate import tabulate

# I decide to not use objected oriented programming but this could be possible development
# Create empty list where equity is tracked
EQUITY=[]
DATES_EQ=[]
#Create empty lists EXPENSES
GOODS_OR_SERVICES = []
PRICES =[]
DATES =[]
EXPENSE_TYPES = []
#Create empty lists EXPENSES
TYPES_STIP = []
MONEY =[]
DATES_STIP=[]

# def reset EQUITY function
def resetEquity ():
	EQUITY.clear()
	DATES_EQ.clear()
# def set EQUITY function 
def setEquity (equity,EQUITY,DATES_EQ):
	x=dt.datetime.now()
	DATES_EQ.append(x.strftime("%d/%m/%Y"))
	EQUITY.append(float(equity))
	df=CreateDataFrame_EQ()
	EQUITY=df['EQUITY'].values.tolist()
	DATES_EQ=df['DATES_EQ'].values.tolist()
	
# def delete LAST EXPENSE
def deleteLastExpense ():
	GOODS_OR_SERVICES.pop()
	PRICES.pop()
	DATES.pop()
	EXPENSE_TYPES.pop()
	EQUITY.pop()
	DATES_EQ.pop()

def deleteLastIncome ():
	TYPES_STIP.pop()
	MONEY.pop()
	DATES_STIP.pop()
	EQUITY.pop()
	DATES_EQ.pop()

def addExpenses (good_or_service,price,date,expense_type):
	GOODS_OR_SERVICES.append(good_or_service)
	PRICES.append(price)
	DATES.append(date)
	EXPENSE_TYPES.append(expense_type)
	EQUITY.append(float(-price))
	DATES_EQ.append(date)
		
def addIncomes (type_stip,money_stip,date_stip):
	TYPES_STIP.append(type_stip)
	MONEY.append(money_stip)
	DATES_STIP.append(date_stip)
	EQUITY.append(float(money_stip))
	DATES_EQ.append(date_stip)

def CreateDataFrame_ex ():
	expense_report = pd.DataFrame()
	expense_report['GOODS'] = GOODS_OR_SERVICES
	expense_report['PRICES'] = PRICES
	expense_report['DATES'] = DATES
	expense_report['EXPENSE_TYPES'] = EXPENSE_TYPES
	expense_report['DATES']=pd.to_datetime(expense_report['DATES'], dayfirst = True , format = '%d/%m/%Y')
	sorted_expense_report = expense_report.sort_values(by='DATES')
	print(tabulate(sorted_expense_report, headers='keys', tablefmt='psql'))
	return sorted_expense_report

def CreateDataFrame_in ():
	income_report = pd.DataFrame()
	income_report['TYPES'] = TYPES_STIP
	income_report['MONEY'] = MONEY
	income_report['DATES_STIP'] = DATES_STIP
	income_report['DATES_STIP']=pd.to_datetime(income_report['DATES_STIP'], dayfirst = True , format = '%d/%m/%Y')
	sorted_income_report = income_report.sort_values(by='DATES_STIP')
	print(tabulate(sorted_income_report, headers='keys', tablefmt='psql'))
	return sorted_income_report

def CreateDataFrame_EQ ():
	eq_report = pd.DataFrame()
	eq_report['EQUITY'] = EQUITY
	eq_report['DATES_EQ'] = DATES_EQ
	eq_report['DATES_EQ']=pd.to_datetime(eq_report['DATES_EQ'], dayfirst = True,format = '%d/%m/%Y')
	sorted_eq_report = eq_report.sort_values(by='DATES_EQ')
	print(tabulate(sorted_eq_report, headers='keys', tablefmt='psql'))
	return sorted_eq_report

def dataFrameTest_Year_ex():
	num_of_ex = 10
	Goods=["Mela","Pera","Banana","Carne","Acqua","cena","PC","telefono"]
	Price=[5,5,10,15,0.5,40,800,1000]
	Expenses_type=["Alimentari","Tecnologia"]
	for i in range(num_of_ex):
		date=str(random.randint(25,28))+"/"+ str(random.randint(9,12)) + "/"+"2022"
		addExpenses(Goods[random.randint(0,7)],Price[random.randint(0,7)],date,Expenses_type[random.randint(0,1)])
	df = CreateDataFrame_ex()
	CreateDataFrame_EQ ()
	return df

def dataFrameTest_Year_in():
	num_of_ex = 4
	type_stip=["Lavoro","azioni"]
	Money=[1600,400]
	for i in range(num_of_ex):
		date=str(random.randint(1,23))+"/"+ str(random.randint(1,9)) + "/"+"2022"
		addIncomes(type_stip[random.randint(0,1)],Money[random.randint(0,1)],date)
	df = CreateDataFrame_in()
	CreateDataFrame_EQ ()
	return df

def graphs(df):
	fig1=plt.figure(figsize=(3, 3), dpi=100)
	df1=pd.DataFrame()
	df1=df.groupby(["EXPENSE_TYPES"] , as_index=False)['PRICES'].sum()
	plt.pie(df1['PRICES'],labels=df1["EXPENSE_TYPES"], shadow=True, textprops = dict(color ="red"))
	plt.title("EXPENSES TYPES")

	fig2=plt.figure(figsize=(3, 3), dpi=100)
	plt.bar(df['GOODS'],df["PRICES"],color='red')
	plt.title("EXPENSES GOODS")

	fig3=plt.figure(figsize=(7, 5), dpi=100)
	df2=df.tail(20)
	now = dt.datetime.now()
	then = now - dt.timedelta(days=31)
	days = mdates.drange(then,now,dt.timedelta(days=1))
	#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
	#plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))
	df5=CreateDataFrame_in()
	plt.plot(df2['DATES'],df2['PRICES'],'o',color='red')
	plt.plot(df5['DATES_STIP'],df5['MONEY'],'o',color='green')
	plt.gcf().autofmt_xdate()
	plt.title("INCOME-EXPENSES")

	fig4=plt.figure(figsize=(3, 3), dpi=100)
	df1=CreateDataFrame_EQ()
	eq=[]
	eq_sum=[]
	dat=[]
	eq=df1['EQUITY'].values.tolist()
	s=eq[0]
	for i in range(1,len(eq)+1):
		for j in range(0,i):
			s=s+eq[j]
		eq_sum.append(s)
		s=0
	print(eq_sum)
	dat=df1['DATES_EQ'].values.tolist()
	df2=df1.loc[df1['EQUITY'] > 0]
	df3=df1.loc[df1['EQUITY'] < 0]
	plt.bar(df2['DATES_EQ'],df2['EQUITY'],color='green')
	plt.bar(df3['DATES_EQ'],df3['EQUITY'],color='red')
	plt.plot(df1['DATES_EQ'],eq_sum,"blue")
	plt.gcf().autofmt_xdate()
	plt.title("EQUITY")

	return fig1,fig2,fig3,fig4
	
x=[]
table_ex=dataFrameTest_Year_ex()
table_in=dataFrameTest_Year_in()
for i in range(10,210,10):
		x.append(int(i))
print(x)

