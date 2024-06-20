import pickle
from abc import ABC, abstractmethod
import os

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
       if os.path.getsize(self.__datasource) > 0:
           with open(self.__datasource, 'rb') as f:
            self.__cache = pickle.load(f)
       else:
           self.__cache = {}

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            print("Chave não encontrada")
            return None
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = obj
                self.__dump()
        except KeyError:
            print("Chave não encontrada")

    def remove(self, key):
        try:
            if(self.__cache[key] != None):
                self.__cache.pop(key)
                self.__dump()
        except KeyError:
            print("Chave não encontrada")

    def get_all(self):
        return self.__cache.values()