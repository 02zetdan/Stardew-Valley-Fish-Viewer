from flask import Flask,jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
db = SQLAlchemy()
with open("/home/zeth/Repos/stardew-valley-scraper/fishes.json","r") as f:
    data = json.load(f)

def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    db.init_app(app)

    #migrate = Migrate(app, db)
    return app

app = create_app()

@app.route('/',methods=['GET'])
def fish():
    # return jsonify({"Fishes":data})
    return render_template('index.html', fishes=data)
@app.route('/fish',methods=['POST'])
def fish_name():
    fish = request.form.get("fish")
    fishes = {}
    fishes[fish] = data[fish]
    return render_template('index.html',fishes=fishes)
@app.route('/fish/location',methods=['POST'])
def fish_location():
    location = request.form['location']
    fishes = {}
    for fish in data.keys():
        if location in data[fish]['Locations']:
            fishes[fish] = data[fish]
    return render_template('index.html', fishes=fishes)
@app.route('/fish/season',methods=['POST'])
def fish_season():
    season = request.form.get('season')
    fishes = {}
    for fish in data.keys():
        if season in data[fish]['Seasons']:
            fishes[fish] = data[fish]
    return render_template('index.html', fishes=fishes)
@app.route('/time',methods=['POST'])
def filter_by_start_time():
    time = request.form.get('time')
    fishes = {}
    for fish in data.keys():
        if time in data[fish]['Time']:
            fishes[fish] = data[fish]
    return render_template('index.html',fishes=fishes)
if __name__ == '__main__':
    app.run(debug=True)