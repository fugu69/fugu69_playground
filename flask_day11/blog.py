from flask import Flask, render_template

app = Flask(__name__)

dummy_posts = [
    {
        "author": "Goofy",
        "title": "Bark side of bagels",
        "content": "Enjoy your bagels",
        "date_posted": "May, 4, 1999",
    },
    {
        "author": "Scoofy",
        "title": "Argggh",
        "content": "The Second Post Content",
        "date_posted": "May, 4, 1999",
    },
    {
        "author": "LKJJ",
        "title": "Kkjjknjnin",
        "content": "Jjhduaciauhncaisnk",
        "date_posted": "May, 4, 1999",
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=dummy_posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
