from flask import Flask, render_template, redirect, url_for
from my_form import LoginForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "my secret key"  # Use .env

# This line sets defaults in app.config.*
#   'BOOTSTRAP_USE_MINIFIED' = {bool} True
#   'BOOTSTRAP_CDN_FORCE_SSL' = {bool} False
#   'BOOTSTRAP_QUERYSTRING_REVVING' = {bool} True
#   'BOOTSTRAP_SERVE_LOCAL' = {bool} False
#   'BOOTSTRAP_LOCAL_SUBDOMAIN' = {NoneType} None
# Also adds app.blueprints.bootstrap.*, e.g.
#   jinja_loader
#   root_path = {str} 'E:\\Python\\Projects\\day-61_flask_wtf\\venv\\lib\\site-packages\\flask_bootstrap'
#   static_folder = {str} 'E:\\Python\\Projects\\day-61_flask_wtf\\venv\\lib\\site-packages\\flask_bootstrap\\static'
#   static_url_path = {str} '/static/bootstrap'
#   etc.
Bootstrap(app)


@app.route("/")
def home():
    # print(app.static_url_path)
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and \
                login_form.password.data == '12345678':
            return redirect(url_for('success'))
            # return redirect('/success')
            # return render_template('success.html')
        else:
            return redirect(url_for('denied'))
            # return redirect('/denied')
            # return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
