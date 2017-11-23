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

"control user"
while loanAmount != Decimal or loanAmount <= 0:
    try:
        loanAmount = Decimal(input("Bitte geben sie den Darlehensbetrag in Euro ein:"))
        break
    except:
        print("Bitte geben Sie einen Zahlenwert groeßer 0 ein!")

while rateOfInterest != Decimal or rateOfInterest <= 0:
    try:
        rateOfInterest = Decimal(input("Bitte geben Sie den Zinssatz in Prozent ein:") * 0.01)
        break
    except:
        print("Bitte geben Sie einen Zahlenwert groeßer 0 ein!")

while runTime != Decimal or runTime <= 0:
    try:
        runTime = Decimal(input("Bitte geben Sie die Laufzeit in Jahren ein:"))
        break
    except:
        print("Bitte geben Sie einen Zahlenwert groeßer 0 ein!")



"""" determing the annuity"""

annuity=Decimal(loanAmount*(((1+rateOfInterest)**runTime)*rateOfInterest/(((1+rateOfInterest)**runTime)-1)))
sumOfInterest=Decimal((annuity*runTime)-loanAmount)

print(locale.currency(annuity,True,True,True))
print(locale.currency(sumOfInterest,True,True,True))



