from decimal import *
import locale

x=''.center(80, '*')+"\n"+  (' '*76).center(80, '*')+"\n"+'Willkommen zum Darlehensrechner'.center(76,' ').center(80, '*')\
+"\n"+'Version 0.1 vom 07.09.2017'.center(76,' ').center(80, '*')+"\n"+'Fehler bitte an itf17a@tbs1.de'.center(76,' ').center(80, '*')\
+"\n"+(' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)

locale.setlocale(locale.LC_ALL,'')

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