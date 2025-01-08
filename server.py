"""
********************************************************************************
* Project Name:  Name and Age Guessing App
* Description:   This web application guesses your gender and age based on your name. By entering your name in the URL, the app uses external APIs to predict your gender and age, then displays the results on a new page.
* Author:        ziqkimi308
* Created:       2025-01-08
* Updated:       2025-01-08
* Version:       1.0
********************************************************************************
"""

from flask import Flask, render_template
import datetime as dt
import requests

flask_app = Flask(__name__)

# Setup home
@flask_app.route("/")
def home():
	name = "John Wick"
	year = dt.datetime.now().year
	return render_template("index.html", YOUR_NAME=name, CURRENT_YEAR=year)

# Setup guess page
@flask_app.route("/guess/<name>")
def guess(name):
	AGIFY_URL = "https://api.agify.io"
	AGIFY_PARAMS = {
		"name": name
	}
	response = requests.get(AGIFY_URL, params=AGIFY_PARAMS)
	age_output = response.json()["age"]

	GENDERIZE_URL = "https://api.genderize.io"
	GENDERIZE_PARAMS = {
		"name": name
	}
	response = requests.get(GENDERIZE_URL, params=GENDERIZE_PARAMS)
	gender_output = response.json()["gender"]

	return render_template("guess.html", name=name, age=age_output, gender=gender_output)

# Run the flask app
if __name__ == "__main__":
	flask_app.run(debug=True)