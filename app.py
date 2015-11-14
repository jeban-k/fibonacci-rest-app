#!/usr/bin/env python
# -*- coding: utf-8 -*
from flask import Flask
from flask_restful import Resource, Api
from fibonacci import Fibonacci
import helper as helper
import os
#App Initialization
app = Flask(__name__)
api = Api(app)
config = None
cachelist = None
#handler for default page
class LandingPage(Resource):
    def get(self):
        return {config['DEFAULT_TITLE']: config['DEFAULT_MESSAGE']}

#Handler for fibonacci/get/<num>
class FibonacciGetWithParam(Resource):
    def get(self, num):
        if num.isnumeric():          
            num = int(num)
            if num > config['CACHING_UPPER_LIMIT']:
                return helper.handle_invalid_usage(config['CACHE_LIMIT_EXCEEDED_ERROR'], config['CACHE_LIMIT_EXCEEDED_CODE'],config)
            elif num < 0:
                return helper.handle_invalid_usage(config['NEGATIVE_VALUE_ERROR'], config['NEGATIVE_CODE'],config)
            elif config['CACHE_ENABLE'] and num > config['LOWER_LIMIT_FOR_CACHING']:
                cachelist = os.listdir(config['CACHE_DIRECTORY'])
                if len(cachelist) > 0:
                #elif num < max(cachelist):
                  if num in cachelist:
                     res = Fibonacci().fibofetchFromCache(num,num)
                     return helper.handle_success(res,config['SUCCESS_CODE'], config)
                  else:
                     templist = map(int,cachelist)
                     templist.append(num)
                     templist.sort()
                     ifound = templist.index(num)
                     if ifound+1 < len(templist):
                        idealCacheFile = templist[ifound+1]
                        res = Fibonacci().fibofetchFromCache(num,idealCacheFile)
                        return helper.handle_success(res,config['SUCCESS_CODE'], config) 
                     else:
                        idealCacheFile = None
                        res = Fibonacci().fiboGen(num)
                        return helper.handle_success(res,config['SUCCESS_CODE'], config) 
                else:
                   res = Fibonacci().fiboGen(num)
                   return helper.handle_success(res,config['SUCCESS_CODE'], config)
            else:
              print "caching not necessary"
              res = Fibonacci().fiboGen(num)
              return helper.handle_success(res,config['SUCCESS_CODE'], config)
        else:
          return helper.handle_invalid_usage(config['NEGATIVE_VALUE_ERROR'], config['NEGATIVE_CODE'], config )

#handler for fibonacci/get
class FibonacciGetWithoutParam(Resource):
     def get(self):
        return helper.handle_invalid_usage(config['NUMERIC_ONLY_ERROR'], config['NEGATIVE_CODE'], config)

#set debug=False  in config.yaml for Production
if __name__ == '__main__':
    config = helper.getConfig()
    api.add_resource(LandingPage, '/')
    api.add_resource(FibonacciGetWithParam, '/{0}/{1}/<string:num>'.format(config["API_VERSION"], config["API_ENDPOINT"]))
    api.add_resource(FibonacciGetWithoutParam, '/{0}/{1}/'.format(config['API_VERSION'], config['API_ENDPOINT']))
    app.run(host = config["HOST"],port = config["PORT"],debug = config['DEBUG'])