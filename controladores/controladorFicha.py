from telas.telaFicha import TelaFicha

class ControladorFicha:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_ficha = TelaFicha()
        self.__fichas = []

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.criar_ficha,
            2: self.remover_ficha,
            3: self.listar_fichas,
            0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_ficha.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def criar_ficha(self):
        pass

    def remover_ficha(self):
        pass

    def listar_fichas(self):
        pass