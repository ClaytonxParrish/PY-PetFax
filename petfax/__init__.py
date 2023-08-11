from flask import Flask
from . import pet


def create_app(): 
    app = Flask(__name__)

    app.register_blueprint(pet.bp)


    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    return app
