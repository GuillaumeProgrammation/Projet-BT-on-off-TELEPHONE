from tkinter import *
from gpiozero import LED
#red = LED()

def red_cli():
    print("Hello")
def red_nocli():
    print("Good bye")


fenetre = Tk()
fenetre.geometry('400x400')
fenetre.title('Bouton pour allumer une LED')
fenetre['bg'] = 'white'
fenetre.resizable(height=False, width=False)
 
bouton1 = Button(fenetre, text='ON', bg = 'green', fg='white', command=red_cli, height = 11, width = 50)
bouton1.pack()

bouton2 = Button(fenetre, text='OFF', bg = 'red', fg='white', command = red_nocli, height = 15, width = 50)
bouton2.pack()

fenetre.mainloop

