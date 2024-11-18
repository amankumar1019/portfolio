from flask import Flask, render_template, request
from generic.utils import write_data_to_csv
app= Flask(__name__)

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

@app.route("/submit", methods=["GET", "POST"])
def success():
    response_message = [
        "Form Submitted!! Aman will get in touch with you shortly..", #success
        "Cannot Process request at the moment!! Please try again.", #server busy
        "Form not submitted"    # failure
        ]
    if request.method == "POST":
        try:
            write_data_to_csv(request.form)
            return render_template('form_submit_response.html', response_message=response_message[0])
        except Exception as e:
            return render_template('form_submit_response.html', response_message=response_message[1])
    else:
        return render_template('form_submit_response.html', response_message=response_message[2])
    