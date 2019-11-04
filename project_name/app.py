from flask import Flask,render_template,request
from base_blogs import select_all,add_info,alter_info,del_info
import form_info
app = Flask(__name__)
app.register_error_handler(form_info.forms)


@app.route('/')
def index():
    res=select_all()
    return render_template('index.html',res=res)


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login_info.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
