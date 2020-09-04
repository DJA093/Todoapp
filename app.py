from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATA_URI']= 'postgresql://dj@localhost:5443/todoapp'
db = SQLAlchemy(app)


class Todo(db.model):
    __tablename__ ='todos'
    id = db.column(db.Integer, primary_key=True)
    description = db.column(db.string(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}{self.description}>'

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=[{
        'description': 'Todo 1'},
        {'description': 'Todo 2'},
         {'description': 'Todo 3'}])