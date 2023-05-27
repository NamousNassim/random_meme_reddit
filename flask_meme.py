from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)

@app.route("/")
def index():
    
    url = "https://www.reddit.com/r/ProgrammerHumor/random.json"
    headers = {"User-Agent": "Mozilla/5.0"} 
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        post = data[0]["data"]["children"][0]["data"]
        title = post["title"]
        url = post["url"]

        return render_template("index.html", title=title, url=url)
    else:
        return "error cannot fitch"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
