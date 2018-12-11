from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db=SQLAlchemy(app)

class Movie(db.Model)
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    rating = db.Column(db.Integer)

    def __init__(self, title, rating):
        self.rating = rating
        self.title = title
    
    def __repr__(self):
        return '<Title %r>' % self.title

@app.route('/')
def home():
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.debug = True
    app.run()