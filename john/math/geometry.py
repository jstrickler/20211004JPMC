"""
Geometric routines for area and volume.

This is a simple library for demonstrating how modules work.
"""
from math import pi

print("MY NAME IS", __name__)

def circle_area(diameter):
    """
    Calculate area of circle with specified diameter

    """
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    """
    Calculate area of rectangle.
    """
    return length * width

def square_area(side):
    """
    Calculate area of a square.

    Blah blah blah
    Whoo hoo hoo
    """
    return rectangle_area(side, side)

