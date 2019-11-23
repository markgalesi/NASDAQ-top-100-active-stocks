import sys
import xml.dom.minidom
import mysql.connector

def insert(cursor):
    query = 'INSERT INTO Nasdaq(timeCheck, exchangee,symbol,company,volume,price,changee) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(query, (time, 'nasdaq',newsymbol,newcomp,newvolume,price,change))


def update(cursor):
    query = 'DELETE FROM Nasdaq WHERE timeCheck != %s'
    cursor.execute(query , (time,))

doc = xml.dom.minidom.parse(sys.argv[1])
data=[]
for tr in doc.getElementsByTagName('table'):
    for td in tr.getElementsByTagName('td'):
        for node in td.childNodes:
            if node.nodeType == node.TEXT_NODE:
                data.append(node.nodeValue)
            for name in node.childNodes:
                if name.nodeType == name.TEXT_NODE:
                    if name.nodeValue[0].isalpha():
                        data.append(name.nodeValue)
   

for i in data:
    i.strip()
    if i=='\n':
        data.remove(i)
f=sys.argv[1][:-6] + ".csv"
time = sys.argv[1][:-6]

#print(time)

data=data[11:]
symbolling=0
symbol=""
company=""
volume=""
price=""
change=""
phrase=""
for i in range(len(data)-10):
    entry=[]
    company=""
    symbol=""
    volume=""
    if i%6==0:
        volume=data[i+1]
        price=data[i+2]
        change=data[i+3]
        for j in data[i]:
            if j =='(':
                symbolling=1
            if symbolling:
                symbol+=j
            else:
                company+=j
        newsymbol = symbol[1:-2]
        newcomp = company[:-1]
        volume = volume.replace(',', '')
        newvolume=int(volume,10)
        try:
        	cnx = mysql.connector.connect(host='localhost', user='root', password='password', database='demo', auth_plugin='mysql_native_password')
        	cursor = cnx.cursor()
        	
        	update(cursor)
        	cnx.commit()
        	
        	insert(cursor)
        	cnx.commit()
        	
        	cursor.close()
        except mysql.connector.Error as err:
        	print(err)
        finally:
        	try:
        		cnx
        	except NameError:
        		pass
        	else:
        		cnx.close()
    symbolling=0