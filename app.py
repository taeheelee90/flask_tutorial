import os
from flask import Flask 
from flask import render_template
from flask import request # for HTTP methods
from flask import redirect
from models import db
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm

from models import WebUser

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        webUser = WebUser()
        webUser.userid = form.data.get('userid')
        webUser.username = form.data.get('username')
        webUser.password = form.data.get('password')

        db.session.add(webUser)
        db.session.commit()
        return redirect('/')
    return render_template('registration.html', form=form)

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
    app.config['SECRET_KEY'] = 'adlfkja;fladfa' #random String
   
    csrf = CSRFProtect()
    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True)