"""
One Day One Dream Team:: Wan Ying Li, Kevin Wang
SoftDev
k20-- RESTful API
2022-11-21
time spent: 0.5 hrs
"""

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
#from flask import request           #facilitate form submission
import requests
#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    with open("key_nasa.txt", "r") as file:
        api_key = file.read()
        request = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
        info = request.json() #dictionary version of the request
        img = info["hdurl"]
        explanation = info["explanation"]
        #print(info)
        return render_template('main.html', img_link=img, explanation=explanation)


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
