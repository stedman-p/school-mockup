from urllib import request
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# students = {
#     "125122":{
#         "first_name":"Peter",
#         "last_name":"Stedman",
#         "sex":"m"
#     },
#     "123456":{
#         "first_name":"John",
#         "last_name":"Doe",
#         "Sex":"m"
#     }}

student_put_args = reqparse.RequestParser()
student_put_args.add_argument("student_id",type=int,help="Student id# (6 digits)")
student_put_args.add_argument("name",type=str,help="First and last name")
student_put_args.add_argument("class",type=str,help="freshman sophomore junior senior")

students = {}

class students(Resource):
    # def get(self,student_id):
    def get(self):
        return students

    def put(self,student_id):
        args = student_put_args.parse_args()
        return {student_id: args}




api.add_resource(students, "/students/<int:student_id>")

if __name__ == "__main__":
    app.run(debug=True)

