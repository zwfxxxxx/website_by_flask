from flask import Flask, render_template, Response, jsonify
from database.jobs import get_jobs

app = Flask(__name__)


@app.route('/')
def home():
    jobs = get_jobs()
    return render_template('home.html', jobs=jobs)


@app.route('/info')
def info():
    jobs = get_jobs()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
