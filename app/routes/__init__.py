from flask import Flask
from app.config import Config
from app.routes.meli import bp as bpmeli

def create_app():
    
    app = Flask(__name__, template_folder='../templates')
    
    app.config.from_object(Config)
    
    app.register_blueprint(bpmeli)
    
    
    return app    