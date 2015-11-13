from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Welcome! You have reached the default page'}

class FibonacciGet(Resource):
    def get(self, num):
        return {'number':num}

api.add_resource(HelloWorld, '/')
api.add_resource(FibonacciGet, '/fibonacci/get/<string:num>')

if __name__ == '__main__':
    app.run(debug=True)
