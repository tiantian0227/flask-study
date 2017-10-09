# encoding:utf-8
from template01 import Flask
from template01 import request
# 初始化一个Flask对象
# Flask()
# 需要传递一个参数__name__
# 这个参数的作用是方便flask框架去寻找资源；方便flask插件比如Flask-Sqlalchemy出现错误的时候，好去寻找问题的所在位置
app = Flask(__name__)

# @开头，并且在函数的上面，说明是装饰器，这个装饰器的作用，是做一个url与视图函数的映射
# 127.0.0.1:50000/  ->去请求hello_world这个函数，然后将结果返回给浏览器


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/simpleWeb/callback', methods=['POST'])
def callback():
    f = open('/data/ylfinCallback', 'a')
    for key in request.form:
        f.write(key + ':' + request.form[key])
        f.write("\t")
    f.write("\n")
    f.close()
    return 'SUCCESS'

# 如果当前这个文件是作为入口程序运行，那么就执行app.run()
if __name__ == '__main__':
    # 启动一个应用服务器，来接受用户的请求
    app.run()

