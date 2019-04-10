
from flask import Flask
from .views.user_view import user_api
from .models import db, bcrypt
from .config import app_config


from .views.user_view import user_api as user_blueprint
from .views.blogpost_view import blogpost_api as blog_blueprint
from .views.battle_view import battles_api as battles_blueprint

def create_app(env_name):
    '''
    Create App
    '''

    # app initilaztion
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    app.register_blueprint(user_api, url_prefix='/api/v1/users')
    app.register_blueprint(blog_blueprint, url_prefix='/api/v1/blogpost')
    app.register_blueprint(battles_blueprint, url_prefix='/api/v1/battles')

    bcrypt.init_app(app)
    db.init_app(app)

    return app
