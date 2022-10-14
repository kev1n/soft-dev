"""
TEAM FLASKERS - Harry ZHu, Kevin Wang, Daniel He
SoftDev
k09-- seeing how static html files work in flask
2022-10-07
time spent: 1.5 hrs
"""

# DEMO 
# basics of /static folder

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
