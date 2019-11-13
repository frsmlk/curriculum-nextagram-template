from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from models.user import User
import peewee as pw
from werkzeug.security import generate_password_hash


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    # name = request.form.get['inputName']
    # email = request.form.get['inputEmail']
    # password = request.form.get['inputPassword']
    return render_template('users/new.html')


@users_blueprint.route('/signup', methods=['POST'])
def create():

    name = request.form.get('inputName')
    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')
    hashed_password = generate_password_hash(password)

    create_user = User(name=name, email=email, password=hashed_password)
    if len(create_user.name) < 6:
        flash("username must be 6 characters or above", "danger")
        return redirect(url_for('users.new'))
    elif " " in create_user.name:
        flash("there cannot be spaces in your username", "danger")
        return redirect(url_for('users.new'))
    elif User.select().where(User.name == name):
        flash("username already exist", "danger")
        return redirect(url_for('users.new'))
    elif User.select().where(User.email == email):
        flash("this email has already signed up", "danger")
        return redirect(url_for('users.new'))
    elif password.islower():
        flash("password need to contain atleast one Uppercase", "danger")
        return redirect(url_for('users.new'))
    elif len(password) < 6:
        flash("password need to contain atleast 6 characters", "danger")
        return redirect(url_for('users.new'))
    else:
        flash("account successfully created!", "success")
        create_user.save()
        return redirect(url_for('sessions.new'))

    # return new_user.save()

    # if username.save():
    #     return render_template("users/home")
    # useremail.save()
    # userpassword.save()


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    return "You are logged in"


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
