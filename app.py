from flask import Flask
from flask_restful import Resource, Api
#Fibo(number of elements)
#Gives the list of fibonacci series fitting the range as output
def fibo(n):
  list1=[]
  if n==0:
    return list1
  list1.append(0)
  f1,f2 = 0,1
  for i in range(n-1):
    f1,f2 = f2,f1+f2
    list1.append(f1)
  return list1

#App Initialization
app = Flask(__name__)
api = Api(app)

#handler for default page
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Welcome! You have reached the default page'}

#Handler for fibonacci/get/<num>
class FibonacciGet(Resource):
    def get(self, num):
        if num.isnumeric():          
          num = int(num)
          if num < 0:
            return {'Exception' : 'please enter positive values' }
          else :
            return {'fibonacci':fibo(num) }
        else:
          return {'Exception' : 'Please enter positive numeric values' }

#handler for fibonacci/get
class FibonacciHandler(Resource):
     def get(self):
        return {'Exception' : 'Enter any numeric value to get desired result' }

#Routing for respective resources
api.add_resource(HelloWorld, '/')
api.add_resource(FibonacciGet, '/fibonacci/get/<string:num>')
api.add_resource(FibonacciHandler, '/fibonacci/get/')

#start the app
#set debug=False for Production
if __name__ == '__main__':
    app.run(debug=True)
