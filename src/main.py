import os

import torch
from flask import Flask
from flask_cors import CORS
from diffusers import StableDiffusionPipeline

from config import app_config

# Initialize the Flask application
config_name = os.getenv('FLASK_CONFIG', 'development')

config = app_config[config_name]

if torch.cuda.is_available():
    config["TORCH_DEVICE_NAME"] = torch.device("cuda")
    config["TORCH_AUTOCAST"] = "cuda"
    config["TORCH_DTYPE"] = torch.float16

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config.from_object(config)
app.debug = True

CORS(app)

# Load the CompVis SD1.4 model
pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        use_auth_token=True
).to(app.config["TORCH_DEVICE_NAME"].type)


# Import the routes
import src.controllers.app_controller as app_controller
import src.controllers.inference_controller as inference_controller

