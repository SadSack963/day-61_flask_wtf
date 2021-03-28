from flask import Flask, render_template
from my_form import LoginForm


app = Flask(__name__)
app.secret_key = "my secret key"  # Use .env


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # if f.validate_on_submit():
    #     return render_template('success.html')
    # else:
    #     return render_template('denied.html')
    return render_template('login.html', form=login_form)


# @app.route("/success")
# def success():
#     return render_template('success.html')
#
#
# @app.route("/denied")
# def success():
#     return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
