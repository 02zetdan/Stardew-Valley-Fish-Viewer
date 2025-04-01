import json
from app import db, app,Fish


# Load JSON data
with open("./fishes.json", "r") as file:
    fishes_data = json.load(file)

# Insert data into database
with app.app_context():  # Ensure we have the Flask app context
    for name, details in fishes_data.items():
        fish = Fish(
            name=name,
            locations=details["Locations"],
            time=details["Time"],
            seasons=details["Seasons"],
            weather=details["Weather"],
        )
        db.session.add(fish)
    db.session.commit()
