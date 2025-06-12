import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set secret key from environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Temporary dammy data
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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Temporary dammy data
        if form.user_identity.data == "dm@dm.com" or form.user_identity.data == "dima" and form.password.data == "1234#":
            flash("Login success!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
