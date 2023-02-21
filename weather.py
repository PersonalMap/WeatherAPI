from tkinter import * #GUI for python
import tkinter as tk
from geopy.geocoders import Nominatim #converts adress to cords etc
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests #http requests
import pytz #timezones

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200") #size and pos of window, tkinter 
root.resizable(False, False) #cant resize width nor height

#search box
Search_image=PhotoImage(file="search.png") #search icon
myimage=Label(image=Search_image)
myimage.place(x=20, y=20)  #placerar search bar

textfield=tk.Entry(root, justify="center", width = 16, font=("poppins", 44, "bold"), bg="#92e5d3", border=0, fg="white")
textfield.place(x=50, y = 40)
textfield.focus()

root.mainloop()