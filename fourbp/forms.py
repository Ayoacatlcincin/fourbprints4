from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField, 
                     TextAreaField, SubmitField, IntegerField, FileField)
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import ValidationError

class ContactUsForm(FlaskForm):
    first = StringField('First Name:', validators=[DataRequired()])
    last = StringField('Last Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    quantity = StringField('Approx Quantity:')
    message = TextAreaField('Enter Your Message:', validators=[DataRequired()])
    dateby = DateTimeField('Date Needed by:')
    file = FileField('Upload a file to send us', validators=[FileAllowed(['png', 'jpg', 'gif'], 'Invalid file type')])
    submit = SubmitField('SEND')