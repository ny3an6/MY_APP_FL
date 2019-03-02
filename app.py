import os
import random

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "first.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "Book"
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
    return render_template('fff.html', books=Book.query.all())


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form.get('name')
        author = request.form.get('author')
        content = request.form.get('content')
        book = Book(name, author, content)
        db.session.add(book) # добавляем
        db.session.commit()
    
        return ( jsonify ({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'content': book.content
            }))


@app.route('/update', methods=['POST'])
def update():  
    new_author = request.form.get('new_author')
    new_content = request.form.get('new_content')
    new_name = request.form.get('new_name')
    id = request.form.get('id')
    book = Book.query.filter_by(id=id).first()
    book.name = new_name
    book.author = new_author
    book.content = new_content
    db.session.commit()
    return redirect(url_for('book'))


@app.route('/delete', methods=['POST'])
def delete():
    id = request.form.get('id')
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('book'))


if __name__ == '__main__':
    app.run(debug=True)