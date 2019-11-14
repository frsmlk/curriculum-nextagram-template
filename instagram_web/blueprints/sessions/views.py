from models.user import User
from flask import Blueprint, render_template, request, flash, url_for, redirect, session
from flask_login import login_manager, login_required, logout_user, login_user, current_user
from werkzeug.security import check_password_hash


sessions_blueprint = Blueprint('sessions',
                               __name__,
                               template_folder='templates')


@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/signin.html')


@sessions_blueprint.route('/', methods=['POST'])
def create():

    # name = request.form.get('inputName')
    name = request.form.get('inputName')
    # email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')

    account_select = User.get_or_none(name=name)

    if account_select:
        if check_password_hash(account_select.password, password):
            login_user(account_select)
            print(current_user)

            # session['logged_in'] = True
            flash("you are logged in", "success")
            return redirect(url_for('profiles.new', username=name))
        else:
            flash("invalid password", "danger")
            return redirect(url_for('sessions.new'))

    else:
        flash("invalid username", "danger")
        return redirect(url_for('users.new'))


@sessions_blueprint.route("/logout", methods=['GET'])
def logout():
    logout_user()
    print(current_user)

    flash("You have succcessfully logged out", "success")
    return redirect(url_for('sessions.new'))


# if name.current_user.is_authenticated:
#     return redirect(url_for("home"))
# if request.method == "POST":
#     user = SessionUser.find_by_session_id(request.data['user_id'])
#     if user:
#         login_user(user)
#         session['was_once_logged_in'] = True
#         return redirect('/home')
#     flash('That user was not found in the database.')
# if session.get('was_once_logged_in'):
#     flash('You have been automatically logged out.')
#     del session['was_once_logged_in']
# return render_template('/login.html')

# @login_manager.user_loader
# def user_loader(user_id):
#     return SessionUser.find_by_session_id(user_id)


# @sessions_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     if session.get('was_once_logged_in'):
#         # prevent flashing automatically logged out message
#         del session['was_once_logged_in']
#     flash('You have successfully logged yourself out.')
#     return redirect(url_for('sessions.new'))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if app.current_user.is_authenticated:  # already logged in
#         return redirect(url_for('home'))
#     if request.method == 'POST':
#         user = SessionUser.find_by_session_id(request.data['user_id'])
#         if user:
#             login_user(user)
#             session['was_once_logged_in'] = True
#             return redirect('/home')
#         flash('That user was not found in the database.')
#     if session.get('was_once_logged_in'):
#         flash('You have been automatically logged out.')
#         del session['was_once_logged_in']
#     return render_template('/login.html')
