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
l3.place(x=100,y=10)

#setting 2nd image in label l4
l4=tk.Label(root,image=test2)
l4.place(x=450,y=10)

#Creating respective labels and buttons for each game.
l5=tk.Label(root,text="Dropship Remastered",font=("Arial", 15))
l5.place(x=100,y=200)

l6=tk.Label(root,text="Mercs: Remastered",font=("Arial", 15))
l6.place(x=400,y=200)

l1=tk.Button(root,text="Click to Buy",font=("Arial", 15))
l1.place(x=150,y=280)

l2=tk.Button(root,text="Click to Buy",font=("Arial", 15))
l2.place(x=400,y=280)

#Creation of the window and widgets.
def create_top():
    top=Toplevel(root)
    top.geometry("600x300")
    top.title("Shopping Cart")
    Label(top, text="Sorry the cart is currently unavailable.", font='Arial 15 bold').pack()
    button=tk.Button(top, text="Close", command=top.destroy)
    button.pack()

#Upon clicking the shopping cart button a new window pops up.
l7=tk.Button(root,text="Shopping Cart",font=("Arial", 15), command=create_top)
l7.place(x=250,y=400)

l9=tk.Button(root,text="Exit",font=("Arial", 15), command=root.destroy)
l9.place(x=50,y=400)

#starting the main window
root.mainloop()