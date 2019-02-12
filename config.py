import os
from dotenv import load_dotenv

#comment the next 2 lines in production if you don't want to use self created .env in production
base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))

class Config(object):
    ENV = os.environ.get("ENV", "production")
    HOST = os.environ.get("HOST", "localhost")
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = os.environ.get("DEBUG", False)
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", None)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", 'sqlite:///' + os.path.join(base_dir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)


    API_VERSION = '1.0'
    API_TITLE = 'Sample API'
    API_DESCRIPTION = 'This is the interface for the Sample application that all integrated applications will interact with'

    API_VERSION1_NAMESPACE = 'api/v1'
    API_VERSION1_DESCRIPTION = 'First version'

    API_VERSION2_NAMESPACE = 'api/v2'
    API_VERSION2_DESCRIPTION = 'Second version'
    