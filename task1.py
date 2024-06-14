from flask import Flask, render_template
from datetime import datetime
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d.%m.%Y")
    return render_template('task1.html', time=current_time, date=current_date)


@app.route('/time')
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return jsonify(time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
