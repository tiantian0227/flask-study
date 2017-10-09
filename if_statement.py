# encoding:utf-8
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<is_login>/')
def index(is_login):
    if is_login =='1':
        user = {
            'username': u'田甜',
            'age': 20
        }
        return render_template('index_if.html', user1=user)
    else:
        return render_template('index_if.html')

if __name__ == '__main__':
    app.run(debug=True)