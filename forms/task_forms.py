from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')], validators=[DataRequired()])
    submit = SubmitField('Create Task')
