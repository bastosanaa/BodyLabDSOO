import random
from telas.telaFicha import TelaFicha
from modelos.treino import Treino
from modelos.ficha import Ficha
from DAOs.ficha_dao import FichaDAO

class ControladorFicha:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_ficha = TelaFicha()
        self.__fichas_dao = FichaDAO()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.criar_ficha,
            2: self.remover_ficha,
            3: self.listar_fichas,
            4: self.mostrar_lista_pelo_id,
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
                if not novo_treino:
                    raise ValueError
                treinos.append(novo_treino)

            nova_ficha = Ficha(id_ficha,descricao, n_treinos, treinos)
            self.__fichas_dao.add(nova_ficha)
            self.__tela_ficha.mostra_mensagem(f'Ficha {id_ficha} criada com sucesso!')
        except TypeError:
            self.__tela_ficha.mostra_mensagem("Operação Cancelada.")
        except ValueError:
            self.__tela_ficha.mostra_mensagem("Por favor preencha todos os campos.")


    def criar_treino(self):
            treinos = [treino for treino in Treino]

            dados_treino = self.__tela_ficha.pega_dados_treino()
            titulo_treino = dados_treino['treino']
            
            return titulo_treino

    def remover_ficha(self):
        #pegar id na tela
        try:
            if not self.__fichas_dao:
                self.__tela_ficha.mostra_mensagem("Nenhuma ficha cadastrada no sistema")
                return
            id = self.__tela_ficha.pega_id_ficha()
            for ficha in self.__fichas_dao.get_all():
                if ficha.id_ficha == id:
                    self.__fichas_dao.remove(id)
                    self.__tela_ficha.mostra_mensagem(f'Ficha {id} removida com sucesso')
                    return
            self.__tela_ficha.mostra_mensagem(f'Nenhuma ficha de ID: {id} encontrada')
            
        except ValueError:
            self.__tela_ficha.mostra_mensagem('Operação cancelada.')
        except TypeError:
            self.__tela_ficha.mostra_mensagem("Operação Cancelada.")


    def listar_fichas(self):
        if not self.__fichas_dao:
            self.__tela_ficha.mostra_mensagem("Nenhuma ficha cadastrada no sistema")
            return
        contagem_fichas = 0 
        numero_fichas = len(self.__fichas_dao.get_all())
        for ficha in self.__fichas_dao.get_all():
            contagem_fichas += 1
            dados_ficha = {
                'id_ficha' : ficha.id_ficha,
                'descricao': ficha.descricao,
                'numero_treinos': ficha.numero_treinos,
                'treinos': ficha.treinos
            }
            self.__tela_ficha.mostra_ficha_listagem(dados_ficha, contagem_fichas, numero_fichas)


    def mostrar_lista_pelo_id(self):
        if not self.__fichas_dao:
            self.__tela_ficha.mostra_mensagem("Nenhuma ficha cadastrada no sistema")
            return
        id = self.__tela_ficha.pega_id_ficha()
        for ficha in self.__fichas_dao.get_all():
            if ficha.id_ficha == id:
                dados_ficha = {
                'id_ficha' : ficha.id_ficha,
                'descricao': ficha.descricao,
                'numero_treinos': ficha.numero_treinos,
                'treinos': ficha.treinos
            }
                self.__tela_ficha.mostra_ficha_unica(dados_ficha)
                return
        self.__tela_ficha.mostra_mensagem("Nenhuma ficha com esse ID encontrada")


        