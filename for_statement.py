# encoding:utf-8
from flask import Flask, render_template

app = Flask(__name__)


''' 
# for 遍历字典
@app.route('/')
def index():
    user = {
        'username': u'田甜',
        'age': 18
    }
    websites = ['www.baidu.com', 'www.google.com']
    return render_template('index_for.html', user1=user, websites=websites)
   # 打印出key 和values
    for k, v in user.items():
        print k
        print v
    # 只打印key
    for k in user.keys():
        print k
    # 只打印values
    for v in user.values():
        print v
'''


@app.route('/')
def index():
    books =[
        {
            'name': u'西游记',
            'autor': u'吴承恩',
            'price': 110
        },
        {
            'name': u'红楼梦',
            'autor': u'曹雪芹',
            'price': 120
        },
        {
            'name': u'三国演义',
            'autor': u'罗贯中',
            'price': 130
        },
        {
            'name': u'水浒传',
            'autor': u'施耐庵',
            'price': 140
        }
    ]
    return render_template('index_for.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)