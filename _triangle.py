# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(_sa,_sb,_sc):
    """Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns _sa string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
    If all three sides are equal, return 'Equilateral'
    If exactly one pair of sides are equal, return 'Isoceles'
    If no pair of  sides are equal, return 'Scalene'
    If not _sa valid triangle, then return 'NotATriangle'
    If the sum of any two sides equals the squate of the third side, then return 'Right'

    BEWARE: there may be _sa bug or two in this code
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(_sa,int) and isinstance(_sb,int) and isinstance(_sc,int)):
        valid = False

    # require that the input values be >= 0 and <= 200
    elif _sa > 200 or _sb > 200 or _sc > 200:
        valid = False

    elif _sa <= 0 or _sb <= 0 or _sc <= 0:
        valid = False

    else:
        valid = True

    if valid is False:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not _sa triangle
    if (_sa >= (_sb + _sc)) or (_sb >= (_sa + _sc)) or (_sc >= (_sa + _sb)):
        return 'NotATriangle'

    # now we know that we have _sa valid triangle
    if _sa == _sb and _sb == _sc:
        return 'Equilateral'
    if (((_sa**2)+(_sb**2))==(_sc**2))or(((_sb**2)+(_sc**2))==(_sa**2))or\
        (((_sa**2)+(_sc**2))==(_sb**2)):
        return 'Right'
    if (_sa != _sb) and  (_sb != _sc) and (_sa != _sc):
        return 'Scalene'
    return 'Isoceles'
