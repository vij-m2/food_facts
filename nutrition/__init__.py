import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import food_item
    app.register_blueprint(food_item.bp)

    # a simple page that says hello
    """
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    """


    return app