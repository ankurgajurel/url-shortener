
from flask import Flask, jsonify, request, redirect
from dotenv import load_dotenv
import psycopg2
import os
import random, string

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(80), unique=True)

with app.app_context():
    db.create_all()

@app.route('/api', methods=['GET'])
def index():
    return jsonify({'message': 'This is the API for URL Shortener'})

def generate_short_url():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=5))

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    original_url = request.args.get('url')
    if original_url:
        url = Url.query.filter_by(original_url=original_url).first()
        if url:
            return jsonify(shortened_url='http://localhost/api/' + url.short_url), 200
        else:
            short_url = generate_short_url()
            new_url = Url(original_url=original_url, short_url=short_url)
            db.session.add(new_url)
            db.session.commit()
            return jsonify(shortened_url='http://localhost/api/' + short_url), 201
    else:
        return jsonify(error='Missing url parameter'), 400

@app.route('/api/get_url', methods=['GET'])
def get_long_url():
    short_url = request.args.get('shortcode')
    if short_url:
        url = Url.query.filter_by(short_url=short_url).first()
        if url:
            return jsonify(original_url=url.original_url)
        else:
            return 'Short URL not found!', 404
    else:
        return 'Missing shortcode parameter', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)