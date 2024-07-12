from abc import ABC, abstractmethod

class Converter(ABC): 
    def __init__(self, format):
        self.__format__ = format

    @abstractmethod
    def convert(self, input_format):
        pass
