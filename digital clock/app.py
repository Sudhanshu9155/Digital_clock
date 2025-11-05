from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')   # ← this line must be indented

@app.route('/time')
def get_time():
    # return current server time in HH:MM:SS format
    now = datetime.now().strftime('%H:%M:%S')
    return jsonify(time=now)

if __name__ == '__main__':
    app.run(debug=True)
