from flask_restplus import Resource
from api import api1 as api
from api import app
from flask_cors import CORS

cors = CORS(app, resources={r"/*": {"origins": "*"}})

class HelloWorld(Resource):
    def get(self):
        return "customer v1"

api.add_resource(HelloWorld, '/customer')