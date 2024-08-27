from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', language='at')  # Austrian is the default language

@app.route('/en/')
def english():
    return render_template('index.html', language='en')

@app.route('/at/')
def austrian():
    return render_template('index.html', language='at')

if __name__ == '__main__':
    app.run(debug=True)
