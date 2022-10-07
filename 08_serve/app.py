# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
import occupation #this is a copy of 06_py_csv

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def random_occupation():
    return occupation.get_random_occupation()

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

