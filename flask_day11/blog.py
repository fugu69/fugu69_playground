import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set secret key from environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
