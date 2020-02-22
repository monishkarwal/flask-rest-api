import os
from flask import Flask
from flask_restful import Resource, Api, request
import json

app = Flask(__name__)
api = Api(app)


class EndPoint(Resource):
    def get(self):
        return {'message': 'Hello World!'}

    def post(self):
        data = request.get_json()
        print(data)
        return data


api.add_resource(EndPoint, '/')

if __name__ == "__main__":
    if(os.getenv('ENV') == "production"):
        app.run()
    else:
        app.run(debug=True)
