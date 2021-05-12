from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from carp.models import User, Busin
from wtforms.fields.html5 import DateField, TimeField

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class BusinForm(FlaskForm):
    companyname = StringField('companyname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    place = StringField('place',
                              validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone = StringField('phone',
                              validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('submit')

    def validate_companyname(self, companyname):
        user = Busin.query.filter_by(companyname=companyname.data).first()
        if user:
            raise ValidationError('That company name is taken. Please choose a different one.')

    def validate_email(self, email):
        user = Busin.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jfif'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')




class BookingForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone = StringField('Phone No',
                           validators=[DataRequired(), Length(min=2, max=20)])




    date = DateField('Date for booking', validators=None)
    time = TimeField('Select starting time', validators=None)
    time1 = TimeField('Select ending ending', validators=None)
    companyname = StringField('company name',
                       validators=[DataRequired(), Length(min=2, max=20)])
    location = StringField('location of turf',
                       validators=[DataRequired(), Length(min=2, max=20)])
    players = StringField('No.of players',
                       validators=[DataRequired(), Length(min=2, max=20)])
    category = StringField('category',
                       validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Book Now')




