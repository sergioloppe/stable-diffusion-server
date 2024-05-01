import os
from flask import Flask
from flask_cors import CORS

from config import app_config
from src.utils.stable_diffusion import initialize_model

# Initialize the Flask application
config_name = os.getenv('FLASK_CONFIG', 'development')

config = app_config[config_name]()

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config.from_object(config)
app.debug = True

# CORS(app)

# Initialize the stable diffusion model HF_MODEL
pipe = initialize_model(app.config)

# Import the routes
from src.controllers.app_controller import *
from src.controllers.inference_controller import *

