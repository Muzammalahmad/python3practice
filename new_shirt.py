""" Two Names, One Shirt """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

"""
Notes:
#when a method is called on an object(self), Python automatically passesses that object as the first argument.
#when you change some of the string values within a list object, the ID for the list object does not change. What is this evidence for? - Lists are mutable objects!


MacBook-Pro-2:py3projects benishsarinelli$ python -i new_shirt.py
>>> red = shirt()
>>> crimson = red
>>> id(red)
4422300736
>>> id(crimson)
4422300736
>>> red.clean
True
>>> crimson.clean
True
>>> red.make_dirty()
>>> red.clean
False
>>> crimson.clean
False
>>> red is crimson
True
>>> crimson = shirt()
>>> id(crimson)
4422300808
>>> crimson.clean
True
>>> red.make_clean()
>>> crimson.clean
True
>>> red is crimson
False
>>> 
"""

