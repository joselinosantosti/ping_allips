#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import os
db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="base_de_dados")
cursor = db.cursor()

arq = open('ips.txt', 'r')
texto = arq.readlines() 
for ips in texto :
	response = os.system("ping -c 1 " + ips)
	if response == 0:
  		print ips, 'Ligado!'
  		cursor.execute("INSERT into hosts(hos_ip,hos_site)values(%s,%s)",('111','www'))
		db.commit()
		db.close()
	else:
 		 print ips, 'Desligado!' 
	#print(ips) 
arq.close()
