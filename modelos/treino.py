


class Treino():
    def __init__(self, titulo, exercicios:[]):
        self.__titulo = titulo
        self.__exercicios = exercicios


    @property
    def exercicios(self):
        return self.__exercicios
    
    @exercicios.setter
    def exercicios(self, exercicios):
        if isinstance( exercicios, int):
            self.__exercicios = exercicios

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def  titulo(self, titulo):
        if isinstance( titulo, int):
            self.__titulo = titulo