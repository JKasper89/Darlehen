from math import *
from decimal import *
import locale

x=''.center(80, '*')+"\n"+  (' '*76).center(80, '*')+"\n"+'Annuitaetisches Darlehen'.center(76,' ').center(80, '*')\
+"\n"+'Version 0.1 vom 23.11.2017'.center(76,' ').center(80, '*')+"\n"+'Fehler bitte an itf17a@tbs1.de'.center(76,' ').center(80, '*')\
+"\n"+(' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)

locale.setlocale(locale.LC_ALL,'de_DE')


loanAmount =Decimal(input("Bitte geben sie den Darlehensbetrag in Euro ein:"))
while loanAmount != Decimal

rateOfInterest = Decimal(input("Bitte geben Sie den Zinssatz in Prozent ein:")*0.01)
runTime = Decimal(input("Bitte geben Sie die Laufzeit in Jahren ein:"))

"""" determing the annuity"""

annuity=Decimal(loanAmount*(((1+rateOfInterest)**runTime)*rateOfInterest/(((1+rateOfInterest)**runTime)-1)))
sumOfInterest=Decimal((annuity*runTime)-loanAmount)

print(locale.currency(annuity,True,True,True))
print(locale.currency(sumOfInterest,True,True,True))



