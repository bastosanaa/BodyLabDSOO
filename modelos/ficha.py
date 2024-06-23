class Ficha():
    def __init__(self,id_ficha:int, descricao: str, numero_treinos: int, treinos:list):
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(numero_treinos, int):
            self.__prof_reponsavel = numero_treinos
        if isinstance(treinos, list):
            self.__treinos = treinos
        self.__id_ficha = id_ficha
        
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def treinos(self):
        return self.__treinos
    
    @treinos.setter
    def treinos(self, treinos):
        if isinstance(treinos, list):
            self.__treinos = treinos

    @property
    def numero_treinos(self):
        return self.__prof_reponsavel

    @numero_treinos.setter
    def numero_treinos(self, numero_treinos):
        if isinstance(numero_treinos, int):
            self.__prof_reponsavel = numero_treinos

    @property
    def id_ficha(self):
        return self.__id_ficha
    
    @id_ficha.setter
    def id_ficha(self, id_ficha):
        self.__id_ficha = id_ficha