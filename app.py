from flask import Flask
import os
import subprocess
import pytz
from datetime import datetime
import pwd

app = Flask(__name__)

@app.route("/htop")
def htop():
    full_name = "Gourav R" 
    username = pwd.getpwuid(os.getuid()).pw_name

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    return f"""
    <h2>Name: {full_name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
