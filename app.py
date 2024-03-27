from flask import Flask, render_template, request, url_for, redirect,Response, url_for
from flask_pymongo import PyMongo
from bson.objectid import *

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb+srv://tebellobelle:vudkS7NVOEikdCUo@cluster0.qpwpugb.mongodb.net/Salon"
Mongo = PyMongo(app)
db = Mongo.db


@app.route('/')
def home():
    return render_template('Calendar.html')

@app.route('/booking', methods=['POST'])
def booking():
    if request.method == 'POST':
        bookingdate = request.values.get('bookingdate')
        time = request.values.get('time')

        db.Calendar.insert_one( { "date": bookingdate, "time": time } )

        return render_template('Calendar.html')

        
        
    



if __name__ == '__main__':
    app.run(debug=True, port=5002)

