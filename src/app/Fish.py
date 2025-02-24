from app import db
class Fish(db.Model):
    __tablename__ = 'fish'
    id = db.Column(db.Integer, primary_key=True)
    locations = db.Column(db.Text,nullable=False)
    time = db.Column(db.Text,nullable=False)
    seasons = db.Column(db.Text,nullable=False)
    weather = db.Column(db.Text,nullable=False)
    name = db.Column(db.String(80),unique=True,nullable=False)
    def __repr__(self):
        return f"{self.name} is found in {self.locations} during {self.seasons} in {self.weather} weather at {self.time}"
