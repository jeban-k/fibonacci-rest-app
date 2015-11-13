from flask import Flask
from flask_restful import Resource, Api
def fibo(n):
  list1=[0]
  f1,f2 = 0,1
  for i in range(n-1):
    f1,f2 = f2,f1+f2
    list1.append(f1)
  return list1


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Welcome! You have reached the default page'}

class FibonacciGet(Resource):
    def get(self, num):
        if num.isnumeric():          
          num = int(num)
          if num < 0:
            return {'Exception' : 'please enter positive values' }
          elif num == 0:
            return {'fibonacci' : '0' }
          elif num == 1:
            return {'fibonacci':'0,1'}
          else :
            return {'fibonacci':fibo(num) }
        else:
          return {'Exception' : 'Please enter positive numeric values' }

class FibonacciHandler(Resource):
     def get(self):
        return {'Exception' : 'Enter any numeric value to get desired result' }

api.add_resource(HelloWorld, '/')
api.add_resource(FibonacciGet, '/fibonacci/get/<string:num>')
api.add_resource(FibonacciHandler, '/fibonacci/get/')


if __name__ == '__main__':
    app.run(debug=True)
