import os
import config
from flask import Flask
from models.base_model import db
from models.user import User
from flask_login import LoginManager

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'instagram_web')

app = Flask('NEXTAGRAM', root_path=web_dir)
app.secret_key = 'm\x888\xc2\xdc+\xbaR\x95P\xf5\x8c\xf3\xb6\xed\x18\xb8i"\x06\xc7\x94}\x9b\xdd\x1e\t\xf4\x81\xd3\xe1/'


if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

login_manager = LoginManager()
login_manager.init_app(app)


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc


@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.id == user_id)
