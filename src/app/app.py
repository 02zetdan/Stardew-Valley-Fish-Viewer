from flask import Flask,jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from dotenv import load_dotenv
import os
load_dotenv()
# with open("/home/zeth/Repos/stardew-valley-scraper/fishes.json","r") as f:
#     data:dict = json.load(f)

# fish_info:dict = {}
# for fish_key,info in data.items():
#     fish_info[fish_key] = Fish(fish_key,info["Locations"],info["Time"],info["Seasons"],info["Weather"])
def create_app():
    app = Flask(__name__,template_folder='templates')

    return app

app = create_app()
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("POSTGRES_HOST", "database-service")  # Container name from docker-compose
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
CORS(app, resources={r"/*": {"origins": "*"}}) # Temporarily allow all origins (for debugging)
class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    locations = db.Column(db.JSON, nullable=False)  # Storing list of locations as JSON
    time = db.Column(db.JSON, nullable=False)  # Storing list of time ranges as JSON
    seasons = db.Column(db.JSON, nullable=False)  # Storing list of seasons as JSON
    weather = db.Column(db.JSON, nullable=False)
    def __init__(self,name,locations,time,seasons,weather,):
        self.name = name
        self.locations = locations
        self.time = time
        self.seasons = seasons
        self.weather = weather
    def __repr__(self):
        return f"{self.name} is found in {self.locations} during {self.seasons} in {self.weather} weather at {self.time}"
    def get_time_string(self):
        time_string =""
        full_strings= []
        for times in self.time:
            time_strings = []
            if times == "Night Market":
                times = [17,2]
            for time in times:
                suffix =""
                if time >= 12:
                    suffix = "pm"
                    if time > 12:
                        time = time - 12
                else:
                    suffix = "am"
                time_strings.append(str(time)+suffix)
            full_time_string = " to ".join(time_strings)
            full_strings.append(full_time_string)
        connector_string =', and '
        if len(full_strings) == 2:
            connector_string = " and "
        time_string= ", ".join(full_strings[:-2] + [connector_string.join(full_strings[-2:])])
        return time_string
    def get_location_string(self):
        return ",".join(self.locations)
    def get_seasons_string(self):
        return ",".join(self.seasons)
    def get_weather_string(self):
        return ",".join(self.weather)

@app.route('/',methods=['GET'])
def fish():
    fish_info = db.session.execute(db.select(Fish)).scalars().all()
    fishes = {}
    for fish in fish_info:
        fishes[fish.name] = {"name":fish.name,"locations":fish.locations,"time":fish.time,"seasons":fish.seasons,"weather":fish.weather}
    return jsonify(fishes)
# @app.route('/fish',methods=['POST'])
# def fish_name():
#     fish = request.form.get("fish")
#     fishes = {}
#     fishes[fish] = fish_info[fish]
#     return render_template('index.html',fishes=fishes)
# @app.route('/fish/location',methods=['POST'])
# def fish_location():
#     location = request.form['location']
#     fishes = {}
#     for fish in fish_info.keys():
#         if location in fish_info[fish].locations:
#             fishes[fish] = fish_info[fish]
#     return render_template('index.html', fishes=fishes)
# @app.route('/fish/season',methods=['POST'])
# def fish_season():
#     season = request.form.get('season')
#     fishes = {}
#     for fish in fish_info.keys():
#         if season in fish_info[fish].seasons:
#             fishes[fish] = fish_info[fish]
#     return render_template('index.html', fishes=fishes)
# @app.route('/time',methods=['POST'])
# def filter_by_start_time():
#     start_time = int(request.form.get('start_time'))
#     end_time = int(request.form.get('end_time'))
#     fishes = {}
#     for fish in fish_info.keys():
#         # if time in fish_info[fish]['Time']:
#         #     fishes[fish] = fish_info[fish]
#         for times in fish_info[fish].time:
#             if times == "Night Market":
#                 times = [17,2]

#             if times[1] == 2 or times[1] == 1:
#                 times[1] +=24
#             if start_time<=times[0] and times[1] <= end_time:
#                 fishes[fish] = fish_info[fish]

#     return render_template('index.html',fishes=fishes)
if __name__ == '__main__':
    app.run(debug=True)