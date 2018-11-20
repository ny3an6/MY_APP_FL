import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "first.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)

    def __init__(self, name, author, content):
        self.name = name
        self.author = author
        self.content = content


@app.route('/', methods=['GET'])
def book():
    return render_template('fff.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.form:
        name = request.form.get('name')
        author = request.form.get('author')
        content = request.form.get('content')
        db.session.add(Book(name, author, content))
        db.session.commit()
    books = Book.query.all()
    return render_template('fff.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
