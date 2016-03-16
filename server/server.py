import requests
import json
import thread
from flask import Flask, jsonify
from apis import pulse
from db import Database
from scheduler import start_scheduled_jobs

app = Flask(__name__)
database = Database()
thread.start_new_thread(start_scheduled_jobs, ())

@app.route("/")
def hello():
    return "ClimateFrame FTW!"

@app.route("/forecast")
def get_forecast():
    return jsonify({'forecast': pulse.get_hourly_6day_forecast()})

@app.route("/recipes")
def get_recipes():
    recipes = database.get_all_recipes()
    return jsonify(recipes)

if __name__ == "__main__":
    app.run(debug=True)