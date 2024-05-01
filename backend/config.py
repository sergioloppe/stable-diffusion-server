import os
import torch
import platform, subprocess

from src.utils.hardware import detected_apple_silicon

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    def __init__(self):
        self.HF_TOKEN = os.environ.get('HF_TOKEN', None)
        self.HF_MODEL = os.environ.get('HF_MODEL', "CompVis/stable-diffusion-v1-4")
        self.TESTING = False
        self.set_device()

    def set_device(self):
        if torch.cuda.is_available():
            self.TORCH_DEVICE_NAME = torch.device("cuda")
            self.TORCH_AUTOCAST = "cuda"
            self.TORCH_DTYPE = torch.float16
        else:
            self.TORCH_DEVICE_NAME = torch.device("mps" if detected_apple_silicon() else "cpu")
            self.TORCH_DTYPE = torch.float32
            self.TORCH_AUTOCAST = "cpu"

    def __str__(self):
        attributes = vars(self)
        return '\n'.join(f"{key}: {value}" for key, value in attributes.items())


class ProductionConfig(Config):
    FLASK_CONFIG = 'production'


class DevelopmentConfig(Config):
    FLASK_CONFIG = 'testing'
    TESTING = True


app_config = {
    'production': Config,
    'development': DevelopmentConfig
}