#!/usr/bin/env python

import os
import  redis
from flask import Flask

from App.user_views import user_blueprint
from App.models import db

def create_app():
    BASE_DIR=os.path.dirname(os.path.dirname(__file__))
    static_dir=os.path.join(BASE_DIR,'static')
    templates_dir=os.path.join(BASE_DIR,'templates')
    app=Flask(__name__,static_folder=static_dir,template_folder=templates_dir)
    app.register_blueprint(blueprint=user_blueprint,url_prefix='/user')

    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@127.0.0.1:3306/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    app.config['SECRET_KEY']='secret_key'
    app.config['SESSION_TYPE']='redis'

    app.config['SESSION_REDIS']=redis.Redis(host='127.0.0.1',port=6379)

    db.init_app(app=app)

    return app
