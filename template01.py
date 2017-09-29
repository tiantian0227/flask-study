# encoding:utf-8
from flask import Flask, render_template

app = Flask(__name__)

'''
@app.route('/template/')
def index():

    # 模版会从templates文件夹下面去找，所以不用写templates路径
    return render_template('index.html', username=u'田甜1', gender=u'女1', age=18)
'''


@app.route('/')
def index():
    class Person(object):
        name = u'田甜'
        age = 20
    p = Person()
    # 若传参数据比较多，则把要传参的数据放到数据字典里面
    context = {
        'username': u'田甜0227',
        'gender': u'女',
        'age': 18,
        'person': p,
        'website': {
           'baidu': 'www.baidu.com',
           'google': 'www.google.com'
        }
    }
    # 模版会从templates文件夹下面去找，所以不用写templates路径
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
