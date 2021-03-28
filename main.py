from flask import Flask, render_template, redirect, url_for
from my_form import LoginForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "my secret key"  # Use .env


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and \
                login_form.password.data == '12345678':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=login_form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
