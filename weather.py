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

#get weather function
def getWeather():
    try:
       city= textfield.get()
    
       geolocator= Nominatim(user_agent="geoapiExercises")
       location= geolocator.geocode(city)
       obj = TimezoneFinder()
       result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

       home=pytz.timezone(result) #use pytz to get time zone
       local_time=datetime.now(home)
       current_time=local_time.strftime("%I:%M %p")
       clock.config(text=current_time)
       name.config(text="CURRENT WEATHER")
    
      #weather
       apiKey = "144f6187c7276c51078a737b6285484d"
       api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey #vår request som vi vill skicka

       json_data = requests.get(api).json() #spar ner datan i json_data
       condition = json_data['weather'][0]['main']
       description = json_data['weather'][0]['description'] #fetching data from json to vars
       temp = int(json_data['main']['temp']-273.15)
       pressure = json_data['main']['pressure']
       humidity = json_data['main']['humidity']
       wind = json_data['wind']['speed']
    
       #set label text to the vars
       t.config(text=(temp, '°'))
       c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
       w.config(text=wind)
       h.config(text=humidity)
       d.config(text=description)
       p.config(text=pressure)
       
    except Exception as e: #when exception gets thrown , invalid entry
        messagebox.showerror("Weather App", "Invalid Entry!")
    
    
#search box
Search_image=PhotoImage(file="search.png") #search icon
myimage=Label(image=Search_image)
myimage.place(x=70, y=20)  #placerar search bar

#textfield inside search bar
textfield=tk.Entry(root, justify="center", width = 23, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=100, y = 40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather) #button with image
myimage_icon.place(x=500, y=34)

#logo
logo_image=PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=650, y=0)

#Bottom box 
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side = BOTTOM)
frame_myimage.place(x=50, y = 350)

#time
name=Label(root, font=("arial", 18, "bold"))
name.place(x=80, y=120)
clock=Label(root, font=("Helvetica", 23))
clock.place(x=80, y=150)

#label 
label1=Label(root,text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg= "#5c9388")
label1.place(x=120, y=380)

label2=Label(root,text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg= "#5c9388")
label2.place(x=225, y=380)

label3=Label(root,text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg= "#5c9388")
label3.place(x=420, y=380)

label4=Label(root,text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg= "#5c9388")
label4.place(x=650, y=380)

t=Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c=Label(font=("arial", 15, 'bold'))
c.place(x=400, y=230)

#Display weather data, wind, humiditym description, pressure
w=Label(text="...", font=("arial", 20, "bold"), bg="#5c9388")
w.place(x= 125, y = 400)
h=Label(text="...", font=("arial", 20, "bold"), bg="#5c9388")
h.place(x= 240, y = 400)
d=Label(text="...", font=("arial", 20, "bold"), bg="#5c9388")
d.place(x= 420, y = 400)
p=Label(text="...", font=("arial", 20, "bold"), bg="#5c9388")
p.place(x= 670, y = 400)




root.mainloop()