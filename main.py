from cgitb import text
from socket import INADDR_ALLHOSTS_GROUP
from tkinter import *
from tkinter import ttk


def calculate_price(km):
    start_price = 4.8
    #km = int(input("Bitte gebe die Kilometer Anzahl an: "))
    if km > 5:
        costs = 1.7
    else:
        costs = 2.1
    total_expenses = start_price + costs * km
    return "Preis:", total_expenses,"€"


def getinput():
    Kilometerstand=  int(input.get())
    text = calculate_price(Kilometerstand)
    ttk.Label(frm, text=text).grid(column=0, row=2)
    root.update()


root = Tk()

input = StringVar()
Kilometerstand = ''



frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="TaxaMeter").grid(column=0, row=0)
ttk.Label(frm, text="Kilometeranzahl eingeben: ").grid(column=0, row=1)
ttk.Entry(frm, textvariable=input).grid(column=1, row=1)
ttk.Button(frm, text="Berechnen", command=getinput).grid(column=1, row=0)

#print (input)

root.mainloop()