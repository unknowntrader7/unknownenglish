import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    PAPAGO_CLIENT_ID = os.getenv('PAPAGO_CLIENT_ID')
    PAPAGO_CLIENT_SECRET = os.getenv('PAPAGO_CLIENT_SECRET')
    CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    AWS_POLLY_VOICE_ID = os.getenv('AWS_POLLY_VOICE_ID')

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
