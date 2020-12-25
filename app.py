from flask import Flask, render_template, url_for, request, request
import sqlite3
import json
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='Frontend', static_folder='Frontend/assets')

@app.route('/')
def index(): 
    return render_template('index.html')
# server start kro mere pr blank dikha rha
@app.route('/slangs')
def slang():
    return render_template('slangs.html')

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))

def test_make_json(cur, row):
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    return r

@app.route('/api/search')
def search():
    query = request.args.get('query', None)
    if query:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        rows = cursor.execute("SELECT * FROM Zealot WHERE slang=?", (query,))
        conn.commit()

        return json.dumps(make_dicts(cursor, rows))
    
    return json.dumps({"message": "No query found"}), 400

@app.route('/api/getAllSlangs')
def get_all_slangs():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM Zealot")
    conn.commit()
    return json.dumps(test_make_json(cursor, rows))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
