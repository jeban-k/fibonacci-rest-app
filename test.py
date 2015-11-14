#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
from app import fibo

#Unittest for the app
class TestFibo(unittest.TestCase):
 
    def setUp(self):
        pass
    #test for value 0 
    def test_num_0(self):
        self.assertListEqual( fibo(0),[] )
    #test for value 1
    def test_num_1(self):
        self.assertListEqual( fibo(1), [0] )
    #test for value 5
    def test_num_5(self):
        self.assertListEqual( fibo(5), [0,1,1,2,3])
 
if __name__ == '__main__':
    unittest.main()
    
