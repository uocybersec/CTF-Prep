from flask import Flask, request, render_template
import sqlite3
from secrets import token_hex

app = Flask(__name__)
conn = sqlite3.connect("database.db", check_same_thread=False)
cur = conn.cursor()

# creates ratings table
cur.executescript(f"""CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT,
    rating INTEGER,
    comments TEXT
); 
DELETE FROM ratings;
INSERT INTO ratings (name, rating, comments) VALUES ('john', 3, 'it was okay...');
INSERT INTO ratings (name, rating, comments) VALUES ('sam', 5, 'I LOVED IT!!');
INSERT INTO ratings (name, rating, comments) VALUES ('lisa', 4, 'It was nice! Could be a bit better though...');
INSERT INTO ratings (name, rating, comments) VALUES ('{token_hex(32)}', 5, 'the flag');""")

@app.route('/')
def home():
    return render_template('index.html'), 200  

@app.route('/get-rating', methods=['POST'])
def add_rating():
    name = request.form.get('name')
    results = cur.execute("SELECT * FROM ratings WHERE name = '" + name + "';")
    ratings = []
    for row in results:
        ratings.append(row)
    return ratings, 200

if __name__ == '__main__':
    app.run("0.0.0.0", 1337, debug=True, use_evalex=False)