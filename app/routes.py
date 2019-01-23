from datetime import datetime
from flask import render_template, redirect, url_for, flash
from app import app, db
from .models import Task
from .forms import TaskForm, TaskDone


@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    for j in range(len(tasks)-1):
        for i in range(len(tasks)-1):
            if (tasks[i + 1].done == False) and (tasks[i].done == True):
                tasks[i], tasks[i + 1] = tasks[i + 1], tasks[i]
    return render_template('index.html', title='ToDoList', tasks=tasks)


@app.route('/task/<int:task_id>', methods=['GET', 'POST'])
def task(task_id):
    form = TaskDone()
    task = Task.query.filter_by(id=task_id).first()
    task_datetime = '{}.{}.{}  {}:{}'.format(task.start_datetime.day,\
            task.start_datetime.month, task.start_datetime.year, task.start_datetime.hour, task.start_datetime.minute)
    task.start_datetime = task_datetime
    if form.validate_on_submit():
        task.done_flip()
        flash('Вы выполнили задачу')
        db.session.add(task)
        db.session.commit()
        return render_template('task.html', title='Task', task=task)
    return render_template('task.html', title='Task', task=task, form=form)



@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
                    task=form.task.data,
                    description=form.description.data,
                    )
        flash('Вы успешно добавили задачу')
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_task.html', title='AddTask', form=form)


@app.route('/task_drop/<int:task_id>')
def task_drop(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
