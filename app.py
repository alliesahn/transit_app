from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://transitapp:transitapp123@ds045694.mongolab.com:45694/subways')
db = client.get_default_database()

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()