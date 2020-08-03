from flask import  Flask  #引入Flask模块
app = Flask(__name__)  #用Flask模块创建一个应用

@app.route('/')
def index():   #定义根目录处理器
    return '<h1>Hello world!<h1>'

if __name__ == '__main__':
    app.run()  #启动服务

#路由
#Flask通过修饰器(和Java的注解类似)来建立路由映射关系的，已经看到修饰器是 app.rotue()

#简单路由，如访问 /hello
@app.route('/hello')
def hello():
    return 'Hello!'

#动态路由
@app.route('/usr/<name>')
def user(name):
    return '<h1>Hello world!<h1>'
    


