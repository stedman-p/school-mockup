# from urllib import request
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

student_put_args = reqparse.RequestParser()
student_put_args.add_argument("student_id",type=int,help="Student id# (6 digits)")
student_put_args.add_argument("name",type=str,help="First and last name")
student_put_args.add_argument("class",type=str,help="freshman sophomore junior senior")

students = {}

class students(Resource):
    # def get(self,student_id):
    def get(self, student_id):
        return {student_id: students[student_id]}

    def put(self,student_id):
        # args = student_put_args.parse_args()
        students[student_id] = request.form['data']
        return {student_id: students[student_id]}




api.add_resource(students, "/students/<string:student_id>")

if __name__ == "__main__":
    app.run(port=4000,debug=True)

