#!/usr/bin/env python
# -*- coding: utf-8 -*
import time
import pickle
import helper as helper
config= helper.getConfig()
#conf = helper().getConfig()
LIMIT = config['LOWER_LIMIT_FOR_CACHING']
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result
    return timed


class Fibonacci(object):
  class Memoize:
     def __init__(self, fn):
        self.fn = fn
        self.memo = {}
     def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]

  @staticmethod
  @Memoize
  @timeit
  def fiboGen(numOfElements):
    flist = []
    """Fibo(number of elements) Gives the list of fibonacci series within the specified range as output"""
    if config['CACHE_ENABLE']:
        try:
            filen= open("{0}{1}".format(config['CACHE_DIRECTORY'],str(numOfElements)),"rb")
            flist = pickle.load(filen)
            return flist
        except IOError:
            pass
    if numOfElements == 0:
         return flist
    flist.append(str(0))
    f1,f2 = 0,1
    for i in range(numOfElements-1):
         f1,f2 = f2,f1+f2
         flist.append(str(f1))
    if config['CACHE_ENABLE']:
         if numOfElements >= LIMIT:
             print "writing to cache"
             pickleit=pickle.dump(flist, open("{0}{1}".format(config['CACHE_DIRECTORY'],str(numOfElements)),"wb"))
    return flist
  
  @staticmethod
  @timeit
  def fibofetchFromCache(numOfElements, idealCachefile):
    flist = []
    print "fetching from cache::{0}".format(idealCachefile)
    """Fibo(number of elements) Gives the list of fibonacci series within the specified range as output loaded from cache"""
    try:
        filen= open("{0}{1}".format(config['CACHE_DIRECTORY'],str(idealCachefile)),"rb")
        flist = pickle.load(filen)
        partialList= flist[0:numOfElements]
        return partialList
    except IOError:
        pass