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
            
            id_ficha =  random.randint(1000, 9999)
            descricao = dados_ficha['descricao']
            n_treinos = int(dados_ficha['numero_treinos'])
            treinos = []

            for _ in range(n_treinos):
                novo_treino = self.criar_treino()
                treinos.append(novo_treino)

            nova_ficha = Ficha(id_ficha,descricao, n_treinos, treinos)
            print(id_ficha,descricao, n_treinos, treinos)
            self.__fichas.append(nova_ficha)
            self.__tela_ficha.mostra_mensagem(f'Ficha {id_ficha} criada com sucesso!')
        except TypeError:
            self.__tela_ficha.mostra_mensagem("Operação Cancelada.")


    def criar_treino(self):

        treinos = [treino for treino in Treino]
        print(treinos)

        dados_treino = self.__tela_ficha.pega_dados_treino()
        titulo_treino = dados_treino['treino']
        
        return titulo_treino

    def remover_ficha(self):
        #pegar id na tela
        try:
            if not self.__fichas:
                self.__tela_ficha.mostra_mensagem("Nenhuma ficha cadastrada no sistema")
                return
            dados_ficha = self.__tela_ficha.pega_dados_remover_ficha()
            id = int(dados_ficha['id_ficha'])
            print(type(id))
            for ficha in self.__fichas:
                print(type(ficha.id_ficha))
                if ficha.id_ficha == id:
                    self.__fichas.remove(ficha)
                    self.__tela_ficha.mostra_mensagem(f'Ficha {id} removida com sucesso')
                    return
            self.__tela_ficha.mostra_mensagem(f'Nenhuma ficha de ID: {id} encontrada')
            
        except ValueError:
            self.__tela_ficha.mostra_mensagem('Operação cancelada. ID inválido')


    def listar_fichas(self):
        if not self.__fichas:
            self.__tela_ficha.mostra_mensagem("Nenhuma ficha cadastrada no sistema")
            return
        contagem_fichas = 0 
        numero_fichas = len(self.__fichas)
        for ficha in self.__fichas:
            contagem_fichas += 1
            dados_ficha = {
                'id_ficha' : ficha.id_ficha,
                'descricao': ficha.descricao,
                'numero_treinos': ficha.numero_treinos,
                'treinos': ficha.treinos
            }
            self.__tela_ficha.mostra_ficha(dados_ficha, contagem_fichas, numero_fichas)
        #listar fichas mostrando o nome da ficha e o titulo dos treinos
        #opcional - mostrar ficha especifica, listando treinos com exercicios


        # if not self.__professores:
        #     self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistema")
        #     return
        # contagem_professor = 0
        # numero_professores = len(self.__professores)
        # for professor in self.__professores:
        #     contagem_professor += 1
        #     dados_professor = {
        #         'nome': professor.nome,
        #         'numero_telefone' : professor.numero_telefone,
        #         'email': professor.email,
        #         'turno': professor.turno,
        #         'salario': professor.salario
        #     }