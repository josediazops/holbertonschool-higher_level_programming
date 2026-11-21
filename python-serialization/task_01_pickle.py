#!/usr/bin/env python3
"""Create a function using pickle"""
import pickle


class CustomObject:
    """Class represent custom object"""

    def __init__(self, name, age, is_student):
        """Initialiaze each parameter as an attribute on objects"""
        # store each parameter as an attribute on the object
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display attributes per line in requiered format to print"""
        # print the three attributes, one per line, in the required format
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize file into a binary read mode and pickel object"""
        # open the file in binary read mode and pickle this object into it
        try:
            with open(filename, 'wb') as f:
                self = pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Open file in binary read and load object to return failure"""
        # open the file in binary read mode and load the object from it
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
