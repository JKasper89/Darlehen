from decimal import *
import locale


"""temp = "**"
leer=" "
leer1=leer*18
temp1 =temp * 40

print (temp1)
print(temp+leer*76+temp )
print(temp+leer*20+"Willkommen zu Darlehensrechner"+leer*26+temp )
print(temp+leer*20+"Version: 0.1 vom 07.09.2017"+leer*29+temp )
print(temp+leer*20+"Fehler bitte an tbs1.de"+leer*33+temp )
print(temp+leer*76+temp )
print (temp1)"""

x=''.center(80, '*')+"\n"+  (' '*76).center(80, '*')+"\n"+'Willkommen zum Darlehensrechner'.center(76,' ').center(80, '*')\
+"\n"+'Version 0.1 vom 07.09.2017'.center(76,' ').center(80, '*')+"\n"+'Fehler bitte an itf17a@tbs1.de'.center(76,' ').center(80, '*')\
+"\n"+(' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)

"""print(''.center(80, '*'))
print((' '*76).center(80, '*'))
print('Willkommen zum Darlehensrechner'.center(76,' ').center(80, '*'))
print('Version 0.1 vom 07.09.2017'.center(76,' ').center(80, '*'))
print('Fehler bitte an tbs1.de'.center(76,' ').center(80, '*'))
print((' '*76).center(80, '*'))
print(''.center(80, '*'))"""
locale.setlocale(locale.LC_ALL,'de_DE')

db = Decimal(input("Bitte geben sie den Darlehensbetrag ein?"))
zins = Decimal(input("Bitte geben sie den Zinssatz an?")*0.01)
laufzeit = Decimal(input("Bitte geben sie die Laufzeit an?"))

jahreszinsen= db*zins
gesamtzinsen = jahreszinsen * laufzeit
gesamtbetrag = db+gesamtzinsen

locale.currency(jahreszinsen)
locale.currency(gesamtzinsen)
locale.currency(gesamtbetrag)

print('Der jaehrlich faellige Zinsbetrag betraegt ' +  locale.currency(jahreszinsen, True, True, True))
print('Die Gesamtzinsen betragen ' + locale.currency(gesamtzinsen,True,True,True))
print('Insgesamt sind '+ locale.currency(gesamtbetrag,True,True,True)+' zu zahlen!')

"""Dies ist eine Aenderung"""