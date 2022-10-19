"""
Foo Bar:: Ameer Alnasser, Wan Ying Li, Kevin Wang
SoftDev
k09-- seeing how static html files work in flask
2022-10-07
time spent: 1.5 hrs
"""

# DEMO 
# basics of /static folder


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templati

app = Flask(__name__) 

@app.route("/")       
def render():
    return render_template("index.html")

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
