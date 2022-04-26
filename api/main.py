from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class users(Resource):
    def get(self):
        return {"nbr_users":"1"}

api.add_resource(users, "/users")

if __name__ == "__main__":
    app.run(debug=True)

