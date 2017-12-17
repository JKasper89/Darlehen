#!/usr/local/bin/python
# coding: utf-8

"""
program: determine the annuity
author: Jan Kasper
"""

from decimal import *
import locale
import time
import math

""" version info and greeting"""
__infoWidth__ = 80
__version__ = '0.2'
__author__ = 'Jan Kasper'

x = ''.center(80, '*') + "\n" + (' '*76).center(80, '*') + "\n" + \
    'Annuitätisches Darlehen'.center(76, ' ').center(80, '*')\
    + "\n" + (__version__ + ' vom ' + (time.strftime("%d.%m.%y"))).center(76, ' ').center(80, '*')\
    + "\n" + 'Fehler bitte an jankasper@students.tbs1.de'.center(76, ' ').center(80, '*')\
    + "\n" + (' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)

locale.setlocale(locale.LC_ALL, 'german')
"""
"check values"
while True:
    try:
        loanAmount=raw_input("Bitte geben Sie den Darlehensbetrag in Euro ein:")
        loanAmount=Decimal(loanAmount)
        if loanAmount <= 0:
            raise ValueError
        break
    except :
        print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
while True:
    try:
        rateOfInterest=raw_input("Bitte geben Sie den Zinssatz in Prozent ein:")
        rateOfInterest=Decimal(rateOfInterest)*Decimal(0.01)
        "rateOfInterest=rateOfInterest*0.01"
        if rateOfInterest <= 0:
            raise ValueError
        break
    except :
        print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")
while True:
    try:
        runTime=raw_input("Bitte geben Sie die Laufzeit in Jahren ein:")
        runTime=Decimal(runTime)
        if runTime<=0:
            raise ValueError
        break
    except :
        print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")



"""" determing the annuity"""
"""
annuity=Decimal(loanAmount*(((1+rateOfInterest)**runTime)*rateOfInterest/(((1+rateOfInterest)**runTime)-1)))
sumOfInterest=Decimal((annuity*runTime)-loanAmount)

print(locale.currency(annuity,True,True,True))
print(locale.currency(sumOfInterest,True,True,True))

"""

