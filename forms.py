from flask_wtf import FalskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class  RegistrationForm(FalskForm):
    """docstring for  RegistrationForm"""
    username = StringField('Username', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email', 
                         validators=[DataRequired(), Email()])
    Password = PasswordField('Password', 
                              validators=[DataRequired()])
    comfirm_password = PasswordField('Confirm Password',
                                      validators=[DataRequired(), EqualTo('password')])
    submit = submitField('Sign Up')


class  LoginForm(FalskForm):
    """docstring for  RegistrationForm"""

    email = StringField('Email', 
                         validators=[DataRequired(), Email()])
    Password = PasswordField('Password', 
                              validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = submitField('Sign Up')