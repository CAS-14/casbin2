from flask import Flask, render_template
import os
import json
from datetime import datetime

def get_data():
    with open("instance/data.json", "r") as f:
        data = json.load(f)

    return data

def set_data(data):
    with open("instance/data.json", "w") as f:
        json.dump(data, f, indent=4)

def create_post(title: str, author: str, content: str):
    data = get_data()
    post_id = max(data["posts"].keys()) + 1

    data["posts"][post_id] = {
        "title": title,
        "author": author,
        "content": content,
    }

    set_data(data)

app = Flask(__name__)

if "instance" not in os.listdir():
    os.mkdir("instance")
    data = {"posts":{}}
    set_data(data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("create.html")