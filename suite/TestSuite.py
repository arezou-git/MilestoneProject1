'''
Created on 20 Jan 2020

@author: Arezo
'''
import unittest
from testcases import test_TTT

suite1= unittest.loader.findTestCases(test_TTT)

testrunner = unittest.TextTestRunner()
testrunner.run(suite1)