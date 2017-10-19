# encoding:utf-8
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments =[
        {
            'user': u'李嘉亮',
            'comment': u'是个男的'
        },
        {
            'user': u'田甜',
            'comment': u'是个女的'
        }
    ]
    return  render_template('index_filter.html', comments=comments)
    # 如果变量值存在，则模版中直接展示变量内容
    # return render_template('index_filter.html',
    #                        avatar='https://static-qa.baiwandian.cn/xinyunlian-admin/static/upload/image//201707/4c6c2081-f03e-495e-a30f-806fcdfa0f81.png')

    # 如果变量值不存在，则调用default过滤器里面的默认值
    # return render_template('index_filter.html')

if __name__ == '__main__':
    app.run(debug=True)