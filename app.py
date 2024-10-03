from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

jobs = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "New York, NY",
        "salary": "$100,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "San Francisco, CA",
        "salary": "$80,000"
    },
    {
        "id": 3,
        "title": "Product Manager",
        "location": "Los Angeles, CA",
        "salary": "$90,000"
    },
    {
        "id": 4,
        "title": "Web Developer",
        "location": "Chicago, IL",
        "salary": "$70,000"
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=jobs)


@app.route('/info')
def info():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
