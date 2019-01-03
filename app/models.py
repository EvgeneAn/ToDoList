from datetime import datetime
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(64))
    description = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    start_datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def done_flip(self):
        return self.done = not self.done
    
    def __repr__(self):
        return 'Task {}'.format(self.task)
