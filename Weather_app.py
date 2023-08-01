from tkinter import *
from configparser import ConfigParser
import urllib.request
import json
from tkinter import messagebox
from tkinter import PhotoImage


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    results = urllib.request.urlopen(url.format(city, api_key))
    if results:

        result = results.read()
        json2 = result.decode("utf-8")
        json_result = json.loads(json2)
        city = json_result['name']
        country = json_result['sys']['country']
        temp_kelvin = json_result['main']['temp']
        temp_celsius = temp_kelvin -272.15
        temp_fahrenheit = temp_kelvin -457.87
        weather = json_result['weather'][0]['main']
        icon = json_result['weather'][0]['icon']
        final = (city, country, temp_celsius, temp_fahrenheit,weather,icon)

        return final


        # (City, Country,  temp_celsius, temp_farenheit, icon, weather)




    else:
        return None



def search(self):
    city = city_text.get()
    weather = get_weather(city)


    if weather:


        location_lbl ['text'] = '{} , {}'.format(weather[0],weather[1])

        temp_lbl ['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2],weather[3])
        logo['file'] = 'weather_icons/{}.png'.format(weather[5])
        weather_lbl['text'] = weather[4]


    else:
        messagebox.showerror('Error', 'Cannot find City')

app = Tk()
app.title("Weather app")
app.geometry('350x350')




city_text= StringVar()
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

app.bind('<Return>', search)

search_btn = Button(app, text = 'Search weather' , width = 12, height = 2)
search_btn.bind('<Button-1>',search)
search_btn.pack(pady=0, padx=0)

location_lbl = Label(app, text='', font=('bold', 20), bd=0)
location_lbl.pack(pady=0, padx=0)

image = Label(app, bitmap='',bd=0)
image.pack(pady=0, padx=0)

logo = PhotoImage(file="")
w1 = Label(app, image=logo,bd=0).pack()



temp_lbl = Label(app, text='',bd=0)
temp_lbl.pack(pady=0, padx=0)

weather_lbl = Label(app, text='', font=(10), bd=0)
weather_lbl.pack()


image1 = PhotoImage(file = r'C:\Users\SAAD COMMUNICATION\Downloads\weatherApp-master\weatherApp-master\bg.png')
background_label = Label(app, image = image1).pack()





app.mainloop()