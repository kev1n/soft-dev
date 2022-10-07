# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
import occupation #this is a copy of 06_py_csv

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def random_occupation():
    return_value = "TEAM FLASKERS - Harry ZHu, Kevin Wang, Daniel He </br>"
    occupation_to_percent, total_percent = occupation.csv_to_dictionary()

    return_value += f"<h1> {occupation.get_random_occupation()} </h1></br>"

    occupations = list(occupation_to_percent.keys())

    for oc in occupations:
        return_value += oc + "</br>"

    return return_value
    

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

