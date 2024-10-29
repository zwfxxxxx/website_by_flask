from celery_app import create_celery_app
from config import config
from flask_mail import Mail, Message

from flask_app import app

mail_config = config.get('mail', {})


def make_mail(app):
    app.config.update(mail_config)
    _mail = Mail(app)
    return _mail


celery = create_celery_app(app)
mail = make_mail(app)


@celery.task
def send_mail(subject, body, file_content=None, file_name=None):
    print("send_mail task start")
    msg = Message(subject, sender=mail_config['MAIL_USERNAME'], recipients=[mail_config['MAIL_RECIPIENTS']])
    msg.body = body
    print(type(file_content))
    print("file_content: ")
    if file_name and file_content:
        msg.attach(file_name, 'application/octet-stream', file_content)
    try:
        mail.send(msg)  # 发送邮件
        return True
    except Exception as e:
        print(e)
        return False
