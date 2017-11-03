# -*- coding: utf-8 -*-

#this program are going to execute the follow statment:
#open file.
#read line.
#organize the information by customer and the visit date. A customer can have done more than one visit.
import datetime
f = open("datasource.txt", "r") #opens file lubrificante.txt
fw = open("newfile.txt","w")
date = ""
datelimit = datetime.date(year=2017,month=6,day=1) #limit date for who need the service.

#lista = [[inf,[],[]],[],[]]
listcustomer = []
for line in f:
    if line[0]  == "/":
        month = line[1:3]        
        #the file don't have the date. Just the month. but is known the month 11 and 12 is from 2016
        if (month == 11) or (month == 12):            
            date = datetime.date(year = 2016, month = int(month), day = 1) #I'm considering every visit the first day of the month
        else:
            date = datetime.date(year = 2017, month = int(month), day = 1)    

    elif date != "": #after date, the next line is the customer
        customer = line[1:29]                
        encontrado = False
        for lista in listcustomer:
            #if the custome in the list, add the new visit date                   
            if lista[0] == customer:                
                lista[1].append(date)
                encontrado = True                   
        if not(encontrado):
            lista = [customer,[date]]
            listcustomer.append(lista)            
        date = ""

customerneed = [] #customer who needs the service.
for customers in listcustomer:
    theyneed = True
    for date in customers[1]:
        if date > datelimit: #customer doesn't need the service.
            theyneed = False
    if theyneed:
        customerneed.append(customers)
        
for customer in customerneed:
    fw.write(str(customer[0]+'\n'))
fw.flush()
fw.close()
f.close()