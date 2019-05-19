import sys
import xml.dom.minidom
import csv
import mysql.connector

argument = str(sys.argv[1])
file = argument.split(".")[0]
#print(file)
filename = file + ".csv"
#print(filename)
f=open(filename, "a+")

headers=["exchange","symbol","company","volume","price","change"]
for header in headers:
    f.write(header + ",")
f.write("\n")



#print("before")

document = xml.dom.minidom.parse(sys.argv[1])
tableElements = document.getElementsByTagName('table')[2]
for tr in tableElements.getElementsByTagName('tr')[1:]:
    data = []
    for td in tr.getElementsByTagName('td'):
        for node in td.childNodes:
            if node.nodeType == node.TEXT_NODE:
                num = node.nodeValue
                num = num.replace(",","")
                num = num.replace("$","")
                if node.nodeValue != "\n":
                    data.append(num)
            else:
                for a in td.getElementsByTagName('a'):
                    for jesus in a.childNodes:
                        if jesus.nodeValue != "\n":
                            stock=jesus.nodeValue[:len(jesus.nodeValue)]
                            stockinfo=stock.split("(")
                            stockname= stockinfo[0]
                            #print(stockname)
                            stocksymbol = stockinfo[1]
                            #print(stocksymbol)
                            stockname=stockname[:-1]
                            stocksymbol=stocksymbol[:-2]
                            data.append(stocksymbol)
                            data.append(stockname)

    if(len(data)>2):
        del data[0]
        del data[-1]    
    f.write("Nasdaq,"+",".join(data)[:-1]+"\n")

#print("after")

cnx = mysql.connector.connect(host='localhost', user='ananya', password='password', database='test')
cursor = cnx.cursor()

cursor.execute('DELETE FROM test.Stocks1;')
cnx.commit()

with open(filename) as f:
	next(f)
	reader = csv.reader(f)
	for row in reader:
		cursor.execute('INSERT INTO test.Stocks1(exchange ,symbol, company, volume, price, chang)'' VALUES (%s, %s, %s,%s,%s,%s)',row) 

cnx.commit()
cnx.close()
f.close()

