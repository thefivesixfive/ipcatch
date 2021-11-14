# ipcatch
# by Caleb "fivesixfive" North

# Version
# 0.0.0

# Imports
from flask import Flask, request
from os.path import exists, join
from sys import path

# Main Flask App object
ipcatch = Flask(__name__)

# Logging Application
def log(ip):
    # Create log filepath
    ip_log = join(path[0], "ips.log")
    # Check if log file exists
    if not exists(ip_log):
        open("ips.log", "w").close()
    # Write to log
    with open(ip_log, "a") as file:
        # Write IP to file with newline
        msg = f"{ip}\n"
        file.write(msg)
# Homepage, grabs IP
@ipcatch.route("/")
def ipcatcher():
    # Attempt to grab IP
    ip = request.remote_addr
    log(ip)
    # Return cheerful message
    return f"Thanks for your Internet protocol address!"

# Execute App
if __name__ == "__main__":
    ipcatch.run()