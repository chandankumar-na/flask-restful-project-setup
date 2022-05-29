from flask import Flask

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    from demoapp.app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    #Db Connection
    from demoapp.Model import db
    db.init_app(app)

    return app
