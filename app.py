from flask import Flask, render_template, url_for, flash, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_session import Session
from flask_login import UserMixin
from flask_sqlalchemy  import SQLAlchemy, BaseQuery
from peewee import *
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisissecrret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/michaelaronian/Desktop/MikesResumeProject/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class GetOrQuery(BaseQuery):
    def get_or(self, ident, default=None):
        return self.get(ident) or default

db = SQLAlchemy(app, query_class=GetOrQuery)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name',db.String(15))
    email = db.Column('email',db.String(50))
    message = db.Column('message',db.String(100))

class Blog(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column('title',db.String(50))
        author = db.Column('author',db.String(20))
        dateposted = db.Column(db.DateTime, index=True)
        content = db.Column('content',db.String(100))

class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired()])
    author = StringField("Name: ", validators=[DataRequired()])
    content = TextAreaField("Content:", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():

    return render_template("projects.html")

@app.route("/render")
def render():
    date = datetime.now()

    return render_template('index.html', date=date)

@app.errorhandler(404)
def fourohfour(exc):
    return render_template('404.html'), 404

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_comment = Contact(name= form.name.data,
                        email  = form.email.data,
                        message=form.message.data)
        db.session.add(new_comment)
        db.session.commit()
        flash("Awesome, thank you for contacting!")
        return redirect(url_for('index'))

    return render_template("contact.html", form=form)


@app.route('/posts', methods=['POST', 'GET'])
def post():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title=form.title.data,
                        author=form.author.data,
                        dateposted=datetime.now(),
                        content=form.content.data)
        db.session.add(new_blog)
        db.session.commit()
        flash("Posted Awesome")
        return redirect(url_for('post'))

    post = Blog.query.all()


    return render_template("posts.html", form=form, post=post)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4500)
