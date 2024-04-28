import os
import torch

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HUGGINGFACE_TOKEN = os.environ.get('HUGGINGFACE_TOKEN')
    TESTING = False
    TORCH_DEVICE_NAME = torch.device("mps")  # cuda, cpu, mps
    TORCH_DTYPE = torch.float32
    TORCH_AUTOCAST = "cpu"

class ProductionConfig(Config):
    FLASK_CONFIG = 'production'


class DevelopmentConfig(Config):
    FLASK_CONFIG = 'testing'
    TESTING = True


app_config = {
    'production': Config,
    'development': DevelopmentConfig
}
