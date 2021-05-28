# importing libraries
from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

# calling flask constructor
app = Flask(__name__)
# creating URL prefix for APIs
api = Api(app, prefix="/api/v1")

# calling BasicAuth constructor
auth = HTTPBasicAuth()

# this username and password should store in some file or DB
USER_DATA = {
    "admin" : "password"
}


# function called when request comes for private resource
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

# class for private resource
class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {'this_is_private_data': 45}

# class for public resource
class PublicResource(Resource):
    def get(self):
        return {'public_data': 46}

# adding resource to API with URL string
api.add_resource(PrivateResource, '/private')
api.add_resource(PublicResource, '/public')

# running our app
if __name__ == "__main__":
    app.run(debug = True)