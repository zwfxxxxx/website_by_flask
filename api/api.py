from flask import Blueprint, render_template, request, flash, redirect, jsonify
from database.jobs import get_job_info_by_id, get_job_list
from flask_app import app
from utils.mail.mail_task import send_mail, mail

api_bp = Blueprint('api', __name__, url_prefix='/')


@api_bp.route('/mail_form')
def mail_form():
    return render_template('send_mail.html')


@api_bp.route('/contact', methods=['POST'])
def send_mail_form():
    email_address = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    message = email_address + ": \n" + message
    file = request.files.get('file')
    file_content = file.read() if file else None
    file_name = file.filename if file else None
    print(type(file_content))
    ret = send_mail.delay(subject, message, file_content, file_name)
    print(ret)
    return redirect('/')


@api_bp.route('/')
def home():
    jobs = get_job_list()
    return render_template('home.html', jobs=jobs)


@api_bp.route('/info')
def info():
    jobs = get_job_list()
    return jsonify(jobs)


@api_bp.route('/job/<job_id>')
def job(job_id):
    job_info = get_job_info_by_id(job_id)
    if not job_info:
        return "Job not found", 404
    return render_template('job_page.html', job=job_info)


@api_bp.route('/job/<job_id>/apply', methods=['POST'])
def job_apply(job_id):
    data = request.form
    file = request.files.get('file')
    if not file:
        return "File not loaded", 400
    file_name = file.filename
    file_content = file.read()
    file.save(f"uploads/{file.filename}")
    print(type(file_content))
    print("file_content")
    a = send_mail(data.get('name')+data.get('email')+'简历', data.get('personal_statement'), file_content, file_name)
    ret = send_mail.delay(data.get('name')+data.get('email')+'简历', data.get('personal_statement'), file_content, file_name)
    print(ret, a)
    return render_template('job_apply_success.html', data=data, file=file.filename)
