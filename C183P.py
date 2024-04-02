from tkinter import*
import requests
import json
root = Tk()
root.title("Country Details")
root.geometry("600x600")

city_name_label = Label(root, text="Capital City Name")
city_name_label.place(relx = 0.2, rely= 0.1, anchor = CENTER)

en = Entry(root)
en.place(relx = 0.2, rely = 0.2, anchor = CENTER)

country = Label(root)
country.place(relx = 0.2, rely= 0.4, anchor = CENTER)

region = Label(root)
region.place(relx = 0.2, rely= 0.5, anchor = CENTER)

language = Label(root)
language.place(relx = 0.2, rely= 0.6, anchor = CENTER)

population = Label(root)
population.place(relx = 0.2, rely= 0.7, anchor = CENTER)

area = Label(root)
area.place(relx = 0.2, rely= 0.8, anchor = CENTER)

def city():
    api = requests.get("https://restcountries.com/v2/capital/"+ en)
    
    new = json.loads(api.content)
    
    cy = new["name"]
    rn = new["region"]
    le = new["languages"]["name"]
    pn = new["population"]
    a = new["area"]
    
    country["text"] = "Country: "+ cy
    region["text"] = "Region: "+ rn
    language["text"] = "Language: "+ le
    population["text"] = "Population: "+ pn
    area["text"] = "Area: "+ a
    
    cd.destroy()
    en.destroy()

cd = Button(root, text="City Details", command= city)
cd.place(relx = 0.2, rely= 0.3, anchor= CENTER)



root.mainloop()