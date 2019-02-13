from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api, Namespace
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
api_init = Api(app=app, version=Config.API_VERSION, title=Config.API_TITLE, description=Config.API_DESCRIPTION)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#List of api namespaces must be continued here
api1 = Namespace(Config.API_VERSION1_NAMESPACE, description=Config.API_VERSION1_DESCRIPTION)
api2 = Namespace(Config.API_VERSION2_NAMESPACE, description=Config.API_VERSION2_DESCRIPTION)
#namespaces created must be added here
api_init.add_namespace(api1)
api_init.add_namespace(api2)
from api import v1
from api import v2