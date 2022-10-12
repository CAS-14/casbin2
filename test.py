import json

my_dict = {
    "posts": {
        "0": {
            "title": "blah",
            "content": "waa"
        },
        "1": {
            "title": "blahdddd",
            "content": "waaaaaa"
        }
    }
}

for post in my_dict["posts"]:
    print(post)