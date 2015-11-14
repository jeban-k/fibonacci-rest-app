#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
import json
import app
#Funtional Test cases for the app
class TestCalls(unittest.TestCase):

    # this method is run before each test
    def setUp(self):
        self.client = app.app.test_client()  #we instantiate a flask test client

    # this method is run after each test
    def tearDown(self):
        pass
    
    #test to see if such a path exists and is handled by the app
    def test_get_path_exists_stat(self):
        # the test client can request a route
        response = self.client.get( '/v1/fibonacci/get/' )
        self.assertEqual(response.status_code, 200)
    
    #test to see if such a path exists and handled by the app
    def test_get_path_with_value_exists_stat(self):
        # the test client can request a route
        response = self.client.get( '/v1/fibonacci/get/1' )
        self.assertEqual(response.status_code, 200)
    
    #test to see if api responds appropriately for negative inputs
    def test_get_output_for_negative(self):
        # the test client can request a route
        response = self.client.get( '/v1/fibonacci/get/-1' )
        self.assertEqual(response.status_code, 200)
        msg = json.loads(response.data.decode('utf-8'))
        self.assertEqual(msg['Exception'], 'Please enter positive integer values to get desired output')

     #test to see if api responds appropriately for negative inputs
    def test_get_output_for_alphabet(self):
        # the test client can request a route
        response = self.client.get( '/v1/fibonacci/get/a' )
        self.assertEqual(response.status_code, 200)
        msg = json.loads(response.data.decode('utf-8'))
        self.assertEqual(msg['Exception'], 'Please enter positive integer values to get desired output')
    
    #check if the app runs without errors
    def test_get_app_running_stat(self):
        # the test client can request a route
        response = self.client.get( '/' )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
