import os

from flask import Flask, render_template, Response, jsonify, request, redirect, flash
from database.jobs import get_job_list, get_job_info_by_id
from utils.mail.mail import make_mail, send_mail

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 生成一个随机的秘密密钥

mail = make_mail(app)


@app.route('/mail_form')
def mail_form():
    return render_template('send_mail.html')


@app.route('/send_mail', methods=['POST'])
def send_mail_form():
    email_address = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    message = email_address + ": \n" + message
    file = request.files.get('file')
    if send_mail(mail, subject, message, file):
        flash("Email sent successfully", "success")
        return redirect('/')
    flash("Error sending mail", "danger")
    return "Error sending mail", 500


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
    if not file:
        return "File not loaded", 400

    file.save(f"uploads/{file.filename}")
    if send_mail(mail, data.get('name')+data.get('email')+'简历', data.get('personal_statement'), file):
        return render_template('job_apply_success.html', data=data, file=file.filename)
    return "Error sending mail", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
