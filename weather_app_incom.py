# Import Required Library
import requests
from tkinter import *
#pip install tk

# -------------------------------------------
# TO DO - Update API Key with your own API key
# Remember, if you run out of calls for the day,å
# all you have to do is delete the app and create
# a new one.
API_KEY = ""
# -------------------------------------------

# Request Weather
def weather_request(location):
    location_key = get_location(location)
    temp, cond = call_weather_functions(location_key)
    return temp, cond

# Output current weather information on Tkinter
def weather_information(loc_text, weather_cond, temp, deg_f):
    temp_f,condtion = weather_request(loc_text.get())
    weather_cond.config(text=condtion)
    temp.config(text=int(temp_f))
    deg_f.config(text="°F")

# -------------------------------------------
# TO DO - Test in Jupyter Notebook (or Google Colab) before implementing the four
# functions below.

# Get location code to use for other API requests
def get_location(location):



    return
 
# Perhaps, in order to limit API calls, you may want to get all the
# response.json() data once, then send it to the two functions below.
# That way, you do not have to call the API more times than necessary.
def call_weather_functions(location_key):
    # Get the results
 
 
 
 
 
 
        
    # Call functions below, using those results
    temp = get_temperature(location_key, data)
    cond = get_condition(location_key, data)
    
    return temp, cond

# Get temperature - called from call_weather_functions() above
def get_temperature(location_key, data=False):



    return result

# Get condition - called from call_weather_functions() above
def get_condition(location_key, data=False):



    return result
# -------------------------------------------


def main():
    # Setup GUI
    root = Tk()
    root.title('Weather App')
    root.geometry('560x400')
    root.maxsize(560,300)
    root.minsize(560,300)

    # weather app text
    weather_app = Label(root,text="GET THE WEATHER", font=("Times", "24"), bg='#5cffc3', pady=5)
    weather_app.pack()

    # Set default background color using HEX color code
    # See https://g.co/kgs/cVkpPm for more info on how to change this
    root.configure(bg='#5cffc3')
    
    # Displays location (shows up after location searched for)
    location = Label(root, text="", font=("pacifico", "20","italic"), bg='#5cffc3')
    location.place(x=10, y=100)

    # Displays weather condition
    weather_condition=Label(root, text="", font=("Times", "14", "italic"), bg='#5cffc3')
    weather_condition.place(x=240, y=160)

    # Display temperature
    temperature=Label(root, text="", font=("Times", "40","italic"), bg='#5cffc3')
    temperature.place(x=240, y=185)

    # Display temperature unit
    degree_f=Label(root, text="", font=("Times", "14","italic"), bg='#5cffc3')
    degree_f.place(x=300, y=190)
    
    # Searchbar for location to get the weather from
    location_text = Entry(root, font=("Arial", "20"), width=30, borderwidth=2)
    location_text.bind('<Return>', lambda event, location_text=location_text, weather_condition=weather_condition, temperature=temperature, degree_f=degree_f: weather_information(location_text, weather_condition, temperature, degree_f))
    location_text.place(x=100, y=50)
    
    # Execute Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()

