from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateTimeField, TextField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    task = StringField('Название задачи', validators=[DataRequired()])
    description = TextField('Описание задачи')
    finish_datetime = DateTimeField('Время окончания задачи')
    submit = SubmitField('Добавить')

class TaskDone(FlaskForm):
    done = BooleanField('Выполнено', default=False)
    submit = SubmitField('Выполнить')