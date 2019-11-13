from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from models.user import User
import peewee as pw
from werkzeug.security import generate_password_hash


profiles_blueprint = Blueprint('profiles',
                               __name__,
                               template_folder='templates')


@profiles_blueprint.route('/<username>', methods=['GET'])
@login_required
def new(username):
    return render_template('profiles/userprofile.html')


@profiles_blueprint.route('/update', methods=['GET'])
@login_required
def update():
    return render_template('profiles/update.html')


@profiles_blueprint.route('/create', methods=['POST'])
@login_required
def create():

    # hashed_password = generate_password_hash(password)
    if current_user:
        update_account = current_user.update(name=request.form.get('inputName'),
                                             email=request.form.get(
                                                 'inputEmail'),
                                             password=request.form.get('inputPassword'))
        update_account.execute()

    # update_account.execute()

    flash("Changes Saved", "success")
    return redirect(url_for("profiles.update"))

    # if len(update_user.name) < 6:
    #     flash("username must be 6 characters or above", "danger")
    #     return redirect(url_for('profiles.update'))
    # elif " " in update_user.name:
    #     flash("there cannot be spaces in your username", "danger")
    #     return redirect(url_for('profiles.update'))
    # elif User.select().where(User.name == name):
    #     flash("username already exist", "danger")
    #     return redirect(url_for('profiles.update'))
    # elif User.select().where(User.email == email):
    #     flash("this email has already signed up", "danger")
    #     return redirect(url_for('profiles.update'))
    # elif password.islower():
    #     flash("password need to contain atleast one Uppercase", "danger")
    #     return redirect(url_for('profiles.update'))
    # elif len(password) < 6:
    #     flash("password need to contain atleast 6 characters", "danger")
    #     return redirect(url_for('profiles.update'))
    # else:
    #     flash("account successfully created!", "success")
    #     update_user.save()
    #     return redirect(url_for('profiles.update'))

    # @profiles_blueprint.route('/signout', methods=['GET'])
    # def signout():
    #     session.pop('logged_in', Nosne)
    #     flash("you have successfully signed out", 'success')
    #     return redirect(url_for('sessions.new'))
    # @app.route("/", methods=["POST"])
    # def upload_file():
    #         # A
    #     if "user_file" not in request.files:4
    #         return "No user_file key in request.files"
    #         # B
    #     file = request.files["user_file"]
    #     """
    #         These attributes are also available
    #         file.filename               # The actual name of the file
    #         file.content_type
    #         file.content_length
    #         file.mimetype
    #     """
    # # C.
    #     if file.filename == "":
    #         return "Please select a file"
    #         # D.
    #     if file and allowed_file(file.filename):
    #         file.filename = secure_filename(file.filename)
    #         output = upload_file_to_s3(file, app.config["S3_BUCKET"])
    #         return str(output)
    #     else:
    #         return redirect("/")
