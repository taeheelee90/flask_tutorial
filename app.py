import os
from flask import Flask 
from flask import render_template
from flask import request # for HTTP methods
from flask import redirect
from models import db

from models import WebUser

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
         #get data from form
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        #validate: not null
        if (userid and username and password and re_password) and password == re_password:
            #Save data
            webUser = WebUser()
            webUser.userid = userid
            webUser.username = username
            webUser.password = password

            db.session.add(webUser)
            db.session.commit()
            return redirect('/')
    return render_template('registration.html')

@app.route('/')
def hello():
    return render_template('hello.html')

# 지금까지는 flask run으로 실행했다면, 이제 python으로 실행하도록 설정
if __name__ == "__main__":
    basdedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basdedir, 'db.sqlite')
        
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True)