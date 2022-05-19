from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Alice in the Wonderland"

    picture= "Alice.jpg"
    
    text = """It is a story of a girl who lost in the forest. Let's try to find a way to get her back home. You have two paths and you need to choose one. The first one is leading to the village and the second one is leading to the wonderland with the zoo"""

    choices = [
        ('enter_house',"Go to the village"),
        ('run_away',"Go to the wonderland")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices,picture=picture)



@app.route("/inside")
def enter_house():
    title = "You go to the village ..."
    
    text = """... and you see the local people who are welcoming you by waving a red flag."""

    choices = [
        ('up_stairs',"Waving them back and try to make a conversation"),
        ('run_away',"To ignore them and find a map")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You are in the Wonderland!"
    
    text = """You have just entered the Wonderland with a weird creatures and excited to explore the surrounding area. Let' see!"""
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/stairs")
def up_stairs():
    title = "Hello everybody!"
    
    text = """You introduced yourself to the citizens and they invited you to have lunch together. You feel safe and accepted the invitation.
    THE END."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
