from flask import Flask, render_template, Response, jsonify, request
from database.jobs import get_job_list, get_job_info_by_id

app = Flask(__name__)


@app.route('/')
def home():
    jobs = get_job_list()
    return render_template('home.html', jobs=jobs)


@app.route('/info')
def info():
    jobs = get_job_list()
    return jsonify(jobs)


@app.route('/job/<job_id>')
def job(job_id):
    job_info = get_job_info_by_id(job_id)
    if not job_info:
        return "Job not found", 404
    return render_template('job_page.html', job=job_info)


@app.route('/job/<job_id>/apply', methods=['POST'])
def job_apply(job_id):
    data = request.form
    file = request.files.get('file')
    print(data, file)
    if not file:
        return "File not loaded", 400

    file.save(f"uploads/{file.filename}")

    return render_template('job_apply', data=data, file=file.filename)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
