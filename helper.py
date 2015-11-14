#!/usr/bin/env python
# -*- coding: utf-8 -*
import yaml
"""parse yaml config file"""
def getConfig(configFile = "config.yaml"):
    fil = open(configFile,'rb')
    if not fil:
        print("Error in opening configFile: "+configFile)
        return None
    config = yaml.load(fil)
    fil.close()
    return config

"""handles messages for errors and exceptions"""
def handle_invalid_usage(error, code, config):
    response = {config['EXCEPTION_TITLE'] : error , config['STATUSCODE_TITLE'] : code}
    return response

"""handles messages for success"""
def handle_success(result, code, config):
    response = {config['SUCCESS_TITLE']: result, config['STATUSCODE_TITLE']: code}
    return response
