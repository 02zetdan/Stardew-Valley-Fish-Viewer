# from app import db
class Fish():
    # __tablename__ = 'fish'
    # id = db.Column(db.Integer, primary_key=True)
    # locations = db.Column(db.Text,nullable=False)
    # time = db.Column(db.Text,nullable=False)
    # seasons = db.Column(db.Text,nullable=False)
    # weather = db.Column(db.Text,nullable=False)
    # name = db.Column(db.String(80),unique=True,nullable=False)
    def __init__(self,name,locations,time,seasons,weather,):
        self.name = name
        self.locations = locations
        self.time = time
        self.seasons = seasons
        self.weather = weather
    def __repr__(self):
        return f"{self.name} is found in {self.locations} during {self.seasons} in {self.weather} weather at {self.time}"
    def get_time_string(self):
        output = ""
        time_strings = []
        for times in self.time:
            for time in times:
                suffix =""
                if time >= 12:
                    suffix = "pm"
                else:
                    suffix = "am"
                time_strings.append(str(time)+suffix)
            time_string = " to ".join(time_strings) +'\n'
        return time_string
    def get_location_string(self):
        pass
    def get_seasons_string(self):
        pass
    def get_weather_string(self):
        pass
