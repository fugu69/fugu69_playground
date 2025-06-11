from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

def CheckSpecialCharacters():
    def _check_special_chars(form, field):
        special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
        if not any(c in special_characters for c in field.data):
            raise ValidationError("Password must include at least one special character")
    return _check_special_chars

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=4), CheckSpecialCharacters()])
    confirm_password = PasswordField('Confirm password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    user_identity = StringField('Username or Email',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=4), CheckSpecialCharacters()])
    remember_user = BooleanField('Remember Me')
    submit = SubmitField('Login')