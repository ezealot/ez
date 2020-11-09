from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='Frontend', static_folder='Frontend/assets')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/slangs.html')
def slang():
    return render_template('slangs.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


app.add_url_rule('/index.html', '/', index)

if __name__ == '__main__':
    app.run(debug=True)
