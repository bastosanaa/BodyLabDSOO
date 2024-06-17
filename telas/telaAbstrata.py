from abc import ABC, abstractmethod

class TelaAbstrata(ABC):
    
    @abstractmethod
    def tela_opcoes(self):
        pass
    
    @abstractmethod
    def init_opcoes(self):
        pass