from config import get_config
from flask_mail import Mail, Message


def make_mail(app):
    config = get_config()
    mail_config = config.get('mail', {})
    app.config.update(mail_config)
    _mail = Mail(app)
    return _mail


def send_mail(app, subject, body, file=None):
    mail = make_mail(app)
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_RECIPIENTS']])
    msg.body = body
    if file:
        msg.attach(file.filename, file.content_type, file.read())
    try:
        mail.send(msg)  # 发送邮件
        return True
    except Exception as e:
        print(e)
        return False
