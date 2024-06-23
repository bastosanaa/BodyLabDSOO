import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        try:
            with open(self.__datasource, 'rb') as f:
                self.__cache = pickle.load(f)
        except EOFError:
            self.__cache = {}

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = obj
                self.__dump()
        except KeyError:
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
            return True
        except KeyError:
            return False


    def get_all(self):
        return self.__cache.values()