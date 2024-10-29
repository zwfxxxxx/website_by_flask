import os

from flask import Flask
app = Flask(__name__)
app.secret_key = os.urandom(24)  # 生成一个随机的秘密密钥