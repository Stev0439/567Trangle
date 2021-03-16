# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from _triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testIsocelesTriangleA(self): 
        self.assertEqual(classify_triangle(3,3,5),'Isoceles','3,3,5 is an Isoceles triangle')
        
    def testIsocelesTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,3),'Isoceles','5,3,3 is an Isoceles triangle')
        
    def testIsocelesTriangleC(self): 
        self.assertEqual(classify_triangle(3,5,3),'Isoceles','3,5,3 is an Isoceles triangle')
        
    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(4,5,6),'Scalene','4,5,6 is a Scalene triangle')
        
    def testLowerBoundA(self): 
        self.assertEqual(classify_triangle(-1,2,3),'InvalidInput','This is not a valid input')
    
    def testLowerBoundB(self): 
        self.assertEqual(classify_triangle(1,-2,3),'InvalidInput','This is not a valid input')
        
    def testLowerBoundC(self): 
        self.assertEqual(classify_triangle(1,2,-3),'InvalidInput','This is not a valid input')
        
    def testUpperBoundA(self): 
        self.assertEqual(classify_triangle(201,2,3),'InvalidInput','This is not a valid input')
        
    def testUpperBoundB(self): 
        self.assertEqual(classify_triangle(1,202,3),'InvalidInput','This is not a valid input')
        
    def testUpperBoundC(self): 
        self.assertEqual(classify_triangle(1,2,203),'InvalidInput','This is not a valid input')
        
    def testSideLimitA(self): 
        self.assertEqual(classify_triangle(1,1,3),'NotATriangle','This is not a valid triangle')
        
    def testSideLimitB(self): 
        self.assertEqual(classify_triangle(1,3,1),'NotATriangle','This is not a valid triangle')
        
    def testSideLimitC(self): 
        self.assertEqual(classify_triangle(3,1,1),'NotATriangle','This is not a valid triangle')
        
    def testnonint1(self): 
        self.assertEqual(classify_triangle("s",1,1),'InvalidInput','This is not a valid input')
        
    def testnonint2(self): 
        self.assertEqual(classify_triangle(1,1.1,1),'InvalidInput','This is not a valid input')
        
    def testnonint3(self): 
        self.assertEqual(classify_triangle(1,1,'t'),'InvalidInput','This is not a valid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

