# PyPerfScore

Dies ist ein kleines Python-Programm, das so schnell, wei es die CPU erlaubt von null auf eine Million zählt (das ist der Standardwert von *max_runs*). 
Vor und nach dem Zählen wird jeweils ein Zeitstempel in eine Variable gespeichert, deren Differenz nach dem Durchlauf berechnet wird. Danach teilt das Programm den Wert von *max_runs* durch die Zeit, die das Zählen gebraucht hat und gibt   
-> die Zeit, die das Zählen benötigte (auf drei Nachkommastellen gerundet),   
-> die Zahl, zu der das Programm hochgezählt hat und   
-> den Punktestand (auf ganze Zahl gerundet) aus.   
Das Runden geschieht mit der *round()*-Funktion. 

# Warum die Tagbezeichnungen von den Titeln der Versionen abweichen: 
Die pre-alpha-Versionen bekommen die Versionsnummern 0.1.x, alpha 0.2.x, beta 0.3.x und die Vollversionen sind dann 1.x.x, 2.x.x und so weiter.

# Pläne für die Zukünftige Entwicklung des Programms: 
-> Hinzufügen einer *tkinter*-basierten graphischen Benutzeroberfläche.

# Systemvorraussetzungen:
-> Python 3.5 oder höher   
-> Alles, um Python 3.5 oder höher ausführen zu können   
