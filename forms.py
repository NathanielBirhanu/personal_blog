from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=10)])

    email = StringField('email', validators=[DataRequired(), Email()])

    password = passwordField('password', validators=[DataRequired()])
    confirm_password = passwordField('confirm_password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = passwordField('password', validators=[DataRequired()])

    submit = SubmitField('Login')