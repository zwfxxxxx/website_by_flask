from config import config
from flask_mail import Mail, Message


mail_config = config.get('mail', {})


def make_mail(app):
    app.config.update(mail_config)
    _mail = Mail(app)
    return _mail


def send_mail(mail, subject, body, file=None):
    msg = Message(subject, sender=mail_config['MAIL_USERNAME'], recipients=[mail_config['MAIL_RECIPIENTS']])
    msg.body = body
    if file:
        msg.attach(file.filename, file.content_type, file.read())
    try:
        mail.send(msg)  # 发送邮件
        return True
    except Exception as e:
        print(e)
        return False
