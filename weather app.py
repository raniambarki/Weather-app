from tkinter import *
import tkinter as tk
#Nominatim uses OpenStreetMap data to find locations on Earth by name and address
from geopy.geocoders import Nominatim
#ttk is a module that is used to style the tkinter widgets. Just like CSS is used to style an HTML element
#messagebox provides a different set of dialogues that are used to display message boxes, showing errors or warnings, widgets to select files or change colors
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
#request:  a library for making HTTP requests
import requests
import pytz

root= Tk()
root.title("weather App")
#root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.geometry("900x500+300+200")
root.resizable(False,False)



#Function to get weather
def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercices")
        location = geolocator.geocode(city)
        obj= TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CUREENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ca094909fd42b61c618d4403e87cd744"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        #temperature and clock
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE:",temp,"°"))
        #weather state
        w.config(text=(wind,"km/h"))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,"mb"))
        d.config(text=(description))
    except Exception as e:
        messagebox.showerror("Weather app","Invalid Entry!")

    



#Search box
Search_image=PhotoImage(file="search.png")
myimage= Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry (root,justify="center",width=20,font=("poppins",20,"bold"),bg="#404040",border=0,fg="#B4B4B3")
textfield.place (x=65, y=43)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
srchicn = Button (image=Search_icon, borderwidth=0,cursor="hand2",bg="#404040",activebackground="#404040",command=getWeather)
srchicn.place (x= 400, y=34)

#logo
Logo_image= PhotoImage(file="logo.png")
logo = Label (image=Logo_image)
logo.place(x=150, y=100)


#bottom box
Frame_image = PhotoImage (file="box.png")
frame_img = Label(image=Frame_image)
frame_img.pack(padx=5, pady=5, side= BOTTOM)


#time
name= Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20,"bold"))
clock.place(x=30,y=130)

#Label
label1= Label (root, text="WIND",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label1.place (x=120,y=400)

label2= Label (root, text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label2.place (x=250,y=400)

label3= Label (root, text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label3.place (x=430,y=400)

label4= Label (root, text="PRESSURE",font=("Helvetica",15,"bold"),fg="white", bg="#1ab5ef")
label4.place (x=650,y=400)

t=Label(font=('arial',70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=('arial',15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=('arial',15,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=('arial',15,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=('arial',15,"bold"),bg="#1ab5ef")
d.place(x=440,y=430)

p=Label(text="...",font=('arial',15,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


#This method will loop forever, waiting for events from the user, until the user exits the program
root.mainloop()
