from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/deva'
db = SQLAlchemy(app)

class Devathon(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)



@app.route("/", methods = ['GET', 'POST'])
def home():
    if(request.method=='POST'):
        email = request.form.get('email')
        pw = request.form.get('pw')
        entry = Devathon(password = pw, mail = email )
        db.session.add(entry)
        db.session.commit()
    return render_template('deva.html')


app.run(debug=True) 