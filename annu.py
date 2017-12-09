#!/usr/bin/env phython
# coding: utf8
from decimal import *
import locale

"info and greetings"
x=''.center(80, '*')+"\n"+  (' '*76).center(80, '*')+"\n"+'Annuitaetisches Darlehen'.center(76,' ').center(80, '*')\
+"\n"+'Version 0.1 vom 23.11.2017'.center(76,' ').center(80, '*')+"\n"+'Fehler bitte an itf17a@tbs1.de'.center(76,' ').center(80, '*')\
+"\n"+(' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)

"localization and formatting"
locale.setlocale(locale.LC_ALL,'de_DE')

"initialize variables"
loanAmount=Decimal(0)
rateOfInterest=Decimal(0)
runTime=Decimal(0)

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

annuity=Decimal(loanAmount*(((1+rateOfInterest)**runTime)*rateOfInterest/(((1+rateOfInterest)**runTime)-1)))
sumOfInterest=Decimal((annuity*runTime)-loanAmount)

print(locale.currency(annuity,True,True,True))
print(locale.currency(sumOfInterest,True,True,True))



