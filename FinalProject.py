#importing the packages

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#creating the root window
root=tk.Tk()

#setting the size of the main window
root.minsize(700,500)

#title of the window
root.title("Ludus Games")

#opening 1st image file
image1 = Image.open("Dropship.jpg")

#resizing the image
image1 = image1.resize((150, 150), Image.Resampling.LANCZOS)
test = ImageTk.PhotoImage(image1)

#opening 2nd image file
image2 = Image.open("Mercs.jpg")

#resizing the image
image2 = image2.resize((150, 150), Image.Resampling.LANCZOS)
test2 = ImageTk.PhotoImage(image2)

#setting 1st image in label l3
l3=tk.Label(root,image=test)
l3.place(x=100,y=10)#position the label

#setting 2nd image in label l4

l4=tk.Label(root,image=test2)
l4.place(x=450,y=10)#position the label

#displaying a menu for pizza using a label with font and size of text

l5=tk.Label(root,text="Dropship Remastered",font=("Arial", 15))
l5.place(x=100,y=200)

#displaying a menu for hot dog

l6=tk.Label(root,text="Mercs: Remastered",font=("Arial", 15))
l6.place(x=400,y=200)


l1=tk.Button(root,text="Click to Buy",font=("Arial", 15))
l1.place(x=150,y=280)


l2=tk.Button(root,text="Click to Buy",font=("Arial", 15))
l2.place(x=400,y=280)

l7=Button(root,text="Shopping Cart",font=("Arial", 15))
l7.place(x=250,y=400)

l7.bind("<Button>",
         lambda e: NewWindow(root))

priceOfDrop=l1*24.99
priceOfMerc=l2*34.99

class NewWindow(Toplevel):
     
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Shopping Cart")
        self.geometry("600x300")
        label = Label(self, text ="Items in cart:")
        label.pack()

    def itemcart():


#starting the main window
root.mainloop()