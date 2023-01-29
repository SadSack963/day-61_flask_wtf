from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, InputRequired, Email, Length

# https://wtforms.readthedocs.io/en/2.3.x/validators/#module-wtforms.validators
# Email() requires WTForms email_validator package:
#       pip install wtforms[email]
# or    pip install email-validator


class LoginForm(FlaskForm):
    # email = StringField(
    #     label='Email',
    #     validators=[InputRequired(), Email(check_deliverability=True)],
    #     render_kw={'style': 'width: 30ch'}
    # )
    email = EmailField(
        label='Email',
        validators=[DataRequired(), Email(check_deliverability=True)],
        render_kw={'style': 'width: 30ch'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired(), Length(min=6)],
        render_kw={'style': 'width: 40ch'}
    )
    submit = SubmitField(label='Log In', render_kw={'btn-primary': 'True'})
