from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name  = StringField('Name', validators=[DataRequired()])
    email =  StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    textarea = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send', validators=[DataRequired()])