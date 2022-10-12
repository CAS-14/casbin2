from flask import Flask, render_template, request, flash, redirect, url_for
import os
import json
import random

def get_data():
    with open("instance/data.json", "r") as f:
        data = json.load(f)

    return data

def set_data(data):
    with open("instance/data.json", "w") as f:
        json.dump(data, f, indent=4)

def get_int_post_ids():
    data = get_data()

    int_post_ids = []
    str_post_ids = data["posts"].keys()

    if len(str_post_ids) == 0:
        return None

    for str_post_id in str_post_ids:
        try:
            int_post_ids.append(int(str_post_id))
        except:
            None

    return int_post_ids

def create_post(title: str, author: str, content: str):
    data = get_data()

    post_ids = get_int_post_ids()

    if post_ids:
        post_id = max(post_ids) + 1
    else:
        post_id = 0

    post_id = str(post_id)

    data["posts"][post_id] = {
        "title": title,
        "author": author,
        "content": content,
    }

    set_data(data)

if "instance" not in os.listdir():
    os.mkdir("instance")
    data = {
        "database_id": random.randint(10000000, 99999999),
        "posts": {},
    }
    set_data(data)

database_id = get_data()["database_id"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", posts=get_data()["posts"])

@app.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        content = request.form["content"]

        if not author:
            author = "Anonymous"

        if not title:
            flash("Title is required.")
        elif not content:
            flash("A post body is required.")

        else:
            create_post(title, author, content)
            return redirect(url_for('index'))

    return render_template("create.html")

@app.route("/about")
def about():
    return render_template("about.html", database_id=database_id)