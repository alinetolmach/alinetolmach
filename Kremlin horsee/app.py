from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Kremlin Horse"

    picture= "Horse.png"
    
    text = """ Kremlin Horse strives to promote educational and work experiences in Russia for a diverse array of people from around the globe. We assist with finding the right opportunity for each individual, guiding them through the necessary processes needed to unclock their path to Russia."""

    choices = [
        ('enter_house', "Study in Russia"),
        ('run_away', "Travel in Russia")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices,picture=picture)


@app.route("/inside")
def enter_house():
    title = "Educational opportunities in Russia"
    
    text = """Russia is a perfect place for foreign students, and Kremlin Horse can prove that!"""

    choices = [
        ('up_stairs',"Degree Programs (BA,MA,MBA,PhD)"),
        ('run_away',"Non-degree Programs (exchange,language course)")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "Get your degree in any field in Russia"
    
    text = """In many Western countries, after 3 or 4 years of study at the university a student receives an undergraduate Bachelor’s degree. To obtain a graduate degree, one has to attend a separate graduate programme, where after 2 or more years they will gain a Master’s or Doctor’s degree.

This system is relatively new to Russia, and today the predominant majority of Russian universities offer undergraduate degree courses alongside diploma degree (specialist) courses, in which Russian higher education institutions bypass the undergraduate, and directly provide for graduate education.

Russian higher education institutions (HEIs) commonly offer the following degrees:

bachelor’s degree
master’s degree
diploma (specialist) degree
doctoral degree
postdoctoral degree"""
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/stairs")
def up_stairs():
    title = "Tourism in Russia"
    
    text = """Since 2000, tourism in Russia has developed at an astonishing pace. Today it is as safe, easy-to-get-to and interesting as any of its European neighbours. Yet, despite its appeal, the biggest country on earth remains a bit of a secret destination. Travellers who take the road less travelled to Russia will be rewarded with a diverse and sophisticated Eurasian culture, some of the planet’s most spectacular natural wonders and more than twenty UNESCO world heritage sites. The lack of crowds and favourable exchange rate is just the cherry on top of Russia’s many attractions that make it a dream destination.."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
