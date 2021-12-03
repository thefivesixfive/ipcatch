# ipcatch
# by Caleb "fivesixfive" North

# Version
# 0.0.0

# Imports
from flask import Flask, request, render_template
from os import getcwd
from sys import path

# Main Flask App object
ipcatch = Flask(__name__)

# Homepage, grabs IP
@ipcatch.route("/")
def ipcatcher():
    # Attempt to grab IP
    try:
        ip = request.environ["HTTP_X_FORWARDED_FOR"]
        print("Reverse proxy IP")
    except:
        ip = request.remote_addr
        print("Direct IP")
    return render_template("index.html", client_ip=ip)#, client_ip="123.456.789.012")