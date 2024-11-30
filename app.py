from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from generic.utils import write_data_to_csv
from datetime import datetime
import json
import os

app= Flask(__name__)
app.config["DEBUG"] = True

basedir = os.path.abspath(os.path.dirname(__file__))

config_path = os.path.join(basedir, 'config.json')
with open(config_path) as json_data:
    d = json.load(json_data)
    json_data.close()

DB_PARAMS = d.get("DB_PARAMS")
host = DB_PARAMS.get("host")
user = DB_PARAMS.get("user")
password=DB_PARAMS.get("password")
database_name = DB_PARAMS.get("database")

DB_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=user,
    password=password,
    hostname=host,
    databasename=database_name,
)

# DB_URI = f'mysql+mysqldb://{user}:{password}@{host}/{DB_NAME}?unix_socket={DB_SOCKET}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ContactQuery(db.Model):
    __tablename__ = "contact_query"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    subject = db.Column(db.String(100), unique=False, nullable=True)
    message = db.Column(db.String(4096), nullable=False)
    date = db.Column(db.String(12), nullable=False, default=lambda: datetime.now().strftime('%Y-%m-%d'))

@app.route("/", methods = ["GET"])
def home():
    return render_template('index.html')


@app.route("/about", methods = ["GET"])
def about():
    return render_template('about.html')

@app.route("/education", methods = ["GET"])
def education():
    return render_template('education.html')

@app.route("/skills", methods = ["GET"])
def skills():
    return render_template('skills.html')

@app.route("/experience", methods = ["GET"])
def experience():
    return render_template('experience.html')

@app.route("/profiles", methods = ["GET"])
def profiles():
    return render_template('profiles.html')

@app.route("/portfolio", methods = ["GET"])
def portfolio():
    return render_template('portfolio.html')

@app.route("/clients", methods = ["GET"])
def clients():
    return render_template('clients.html')

@app.route("/contact", methods = ["GET"])
def contact():
    return render_template('contact.html')

# @app.route("/contact", methods=["GET", "POST"])
# def save_message():
#     user_name = request.form.get("user_name")
#     user_email = request.form.get("user_email")
#     user_mobile = request.form.get("user_mobile")
#     user_message = request.form.get("user_message")
#     dt = datetime.now()

#     if request.method == "POST":
#         if user_message != '':
#             p = ContactQuery(name=user_name, email=user_email, mobile=user_mobile, message=user_message, date=dt)
#             db.session.add(p)
#             db.session.commit()
#     return render_template('contact.html', social_media_params=social_media_params)

@app.route("/submit", methods=["GET", "POST"])
def success():
    response_message = [
        "Form Submitted!! Aman will get in touch with you shortly..", #success
        "Cannot Process request at the moment!! Please try again.", #server busy
        "Form not submitted"    # failure
        ]
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            subject = request.form.get("subject", "")
            message_content = request.form.get("message","")
            p = ContactQuery(name=name, email=email, subject=subject, message_content=message_content)
            db.session.add(p)
            db.session.commit()
            return render_template('form_submit_response.html', response_message=response_message[0])
        except Exception as e:
            return render_template('form_submit_response.html', response_message=response_message[1])
    else:
        return render_template('form_submit_response.html', response_message=response_message[2])
