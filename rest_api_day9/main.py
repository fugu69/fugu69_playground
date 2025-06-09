from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy # Object-relational mapping (ORM)

# instance of the Flask app class
app = Flask(__name__)

# Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

# SQLAlchemy consume the app as an argument
db = SQLAlchemy(app)

# create model
class Destination(db.Model):    # Model is like a row in the db
    id = db.Column(db.Integer, primary_key=True)    # column in the db
    destination = db.Column(db.String(50), nullable=False) #String(50) limits length to 50 chars
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # mthod converts data to dictionary to easier convert it to JSON
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating,
        }
    

# Create Route
# https://www.root.com/
@app.route("/") # create 'home' route
def home():
    # return "Hello!" # logic when the route is accessed
    return jsonify({"message": "Welcome to Travel API"})

# https://www.root.com/destinations/(extension)
@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()

    return jsonify([destination.to_dict() for destination in destinations])


@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error": "Destination not found"}), 404

# POST
@app.route("/destinations", methods=["POST"])
def add_destination():
    data = request.get_json()

    new_destination = Destination(destination=data["destination"],
                                  country=data["country"],
                                  rating=data["rating"])

    db.session.add(new_destination)
    db.session.commit()

    return jsonify(new_destination.to_dict()), 201

# UPDATE
@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    data = request.get_json()

    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)

        db.session.commit()

        return jsonify(destination.to_dict())
    else:
        return jsonify({"error": "Destination not found"}), 404

# DELETE
@app.route("/destinations/<int:destination_id>")
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({"message": "Deleted"})
    else:
        return jsonify({"error": "Destination not found"}), 404






if __name__ == "__main__":
    with app.app_context(): # Content Manager to release resources after use and prevent memory leaks
        db.create_all()     # create all models
    # debug mode for continuous update
    app.run(debug=True)
