from flask_restplus import Resource, Namespace, reqparse
from api import api1 as api
from api import jwt, app
from flask_jwt_extended import jwt_optional, jwt_required, get_jwt_claims, get_jwt_identity, create_access_token, create_refresh_token, fresh_jwt_required
from flask_cors import CORS

parser = reqparse.RequestParser(bundle_errors=True)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

class Home(Resource):
    @jwt_required
    def get(self):
        return "home"

class Login(Resource):
    def post(self):
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        # call to the algostack SSO return details

        user = {"id":1, "first_name":"Pelumi", "last_name":"Algostacks", "email":"pelz@gmail.com", "role":[1,5]}
        access_token = create_access_token(identity=user)
        return {"user_id":user["id"], "access_token":access_token}

@jwt.user_identity_loader
def user_identity_loader(user):
    return user["id"]
@jwt.user_claims_loader
def user_claims_loader(user):
    return{
        "email":user["email"],
        "first_name":user["first_name"],
        "last_name":user["last_name"],
    }




api.add_resource(Login, '/admin/login')
api.add_resource(Home, '/admin/')