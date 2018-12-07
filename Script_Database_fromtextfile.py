#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:51:23 2018
This file is used for accessing data from a txt file and then storing it in MYSQL

@author: kavishdoshi
"""

f = open("TextFile.txt", "r")
k = f.readline()
totruntime = float(k)
print(totruntime)

k = f.readline()
truntime = float(k)
print(truntime)

k = f.readline()
tcount = int(k)
print(tcount)

k = f.readline()
msgbsize = int(k)
print(msgbsize)

k = f.readline()
msgbcount = int(k)
print(msgbcount)

k = f.readline()
msgqdelay = float(k)
print(msgqdelay)

k = f.readline()
msgqcount = int(k)
print(msgqcount)

k = f.readline()
msgrtime = float(k)
print(msgrtime)

k = f.readline()
msgrcount = int(k)
print(msgrcount)

k= f.readline()
msgstime = float(k)
print(msgstime)

k = f.readline()
msgscount = int(k) 
print(msgscount)

k = f.readline()
wrkptime = float(k)
print(wrkptime)

k = f.readline()
wrkpcount = int(k)
print(wrkpcount)

from datetime import datetime


epoc = datetime.utcnow()
print(epoc)


import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='your_password',
                             db='temp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `expodb` (`epoc`,`totruntime`,`truntime`,`tcount`,`msgbsize`,`msgbcount`,`msgqdelay`,`msgqcount`,`msgrtime`,`msgrcount`,`msgstime`,`msgscount`,`wrkptime`,`wrkpcount`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(epoc,totruntime,truntime,tcount,msgbsize,msgbcount,msgqdelay,msgqcount,msgrtime,msgrcount,msgstime,msgscount,wrkptime,wrkpcount))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `expodb`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()  



