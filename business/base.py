from util import serializer

class Base:

    def __init__(self,name):
        self.data=serializer.load(name)