# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My App Setup
app = Flask(__name__)
Scss(app)

app.config("SQLALCHEMY_DATABASE_URI") = "sqlite:///taskdata.db"

db = SQLAlchemy(app)

# Data Class ~ Every row is a model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contect = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Task {self.id}"

@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
