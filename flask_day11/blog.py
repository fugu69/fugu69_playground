import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Integer, Text
from sqlalchemy.sql import func
from forms import RegistrationForm, LoginForm

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set secret key from environment variable
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

# db structure == Classes == Models
db = SQLAlchemy(app)

# Table row
class User(db.Model):
    # Table columns
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    # Image will be hashed with 20 characters format -> String(20) format
    image_file = Column(String(20), nullable=False, default="default.jpg")
    # Password will be hashed with 60 characters format -> String(60) format
    password = Column(String(60), nullable=False)

    # A virtual list of Post objects on each User instance — user.posts
    # A backref (reverse lookup) so that each Post can access its User via post.author
    # "User has many posts" and "Each post has one author (user)"
    posts = db.relationship("Post", backref="author", lazy=True)

    # How the object is printed out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    content = Column(Text, nullable=False)

    # db.ForeignKey("user.id") -> Each Post must be linked to a User
    # The column author_id in Post is a foreign key referencing User.id
    # user is the name of the table created by User class
    # "This post belongs to the user whose id matches author_id"
    author_id = Column(Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"
    

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
