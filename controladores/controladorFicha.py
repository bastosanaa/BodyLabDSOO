import random
from telas.telaFicha import TelaFicha
from modelos.treino import Treino
from modelos.ficha import Ficha

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
        try:
            dados_ficha = self.__tela_ficha.pega_dados_nova_ficha()
            print(dados_ficha)
            id_ficha =  random.randint(1000, 9999)
            descricao = dados_ficha['descricao']
            n_treinos = int(dados_ficha['numero_treinos'])
            treinos = []

            for _ in range(n_treinos):
                novo_treino = self.criar_treino()
                treinos.append(novo_treino)

            nova_ficha = Ficha(id_ficha,descricao, n_treinos, treinos)
            self.__fichas.append(nova_ficha)
        except TypeError:
            self.__tela_ficha.mostra_mensagem("Operação Cancelada.")


    def criar_treino(self):

        dados_treino = self.__tela_ficha.pega_dados_treino()
        titulo_treino = dados_treino['titulo']
        exercicio_1 = dados_treino['exercicio_1']
        exercicio_2 = dados_treino['exercicio_2']
        exercicio_3 = dados_treino['exercicio_3']
        exercicios = [exercicio_1,exercicio_2,exercicio_3]
        novo_treino = Treino(titulo_treino, exercicios)
        return novo_treino

    def remover_ficha(self):
        pass
        #remover ficha pelo id

    def listar_fichas(self):
        pass
        #listar fichas mostrando o nome da ficha e o titulo dos treinos
        #opcional - mostrar ficha especifica, listando treinos com exercicios