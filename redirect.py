# encoding:utf-8
from template01 import Flask, url_for, redirect
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    login_url = url_for('login')
    return redirect(login_url)
    return u'这是首页'


@app.route('/login/')
def login():
    return u'这是登陆页'


@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return '这是问答页面'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()