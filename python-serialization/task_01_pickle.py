#!/usr/bin/env python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    """Custom Python objects"""

    def __init__(self, name, age, is_student):
        """initialise the attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display the attributes values"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize and save a custom object to a pickle file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """load and deserialize the pickle file to recreate custom object"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError,
                AttributeError, ImportError, IndexError):
            return None
