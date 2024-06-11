from modelos.matricula import Matricula
from telas.telaMatricula import TelaMatricula
from modelos.plano import Plano
from modelos.turno import Turno
from datetime import datetime, timedelta
import random
from collections import Counter

class ControladorMatricula:
    def __init__(self, controlador_sistema):
        self.__tela_matricula = TelaMatricula()
        self.__controlador_sistema = controlador_sistema
        self.__matriculas = []
        self.__planos = [Plano.Silver, Plano.Gold, Plano.Diamond]
        self.__turnos = [Turno.Matutino, Turno.Vespertino, Turno.Noturno]

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    def aluno_esta_matriculado(self, nome_aluno):
        for matricula in self.__matriculas:
            if matricula.aluno == nome_aluno:
                return True
        return False

    def realizar_matricula(self):
        dados_matricula = self.__tela_matricula.pega_dados_matricula(self.__turnos, self.__planos)
        aluno = dados_matricula['aluno']
        if self.aluno_esta_matriculado(aluno):
            return self.__tela_matricula.mostra_mensagem("Aluno já está matriculado")
        else:
            turno = dados_matricula['turno']
            plano = dados_matricula['plano']
            
            plano_selecionado = self.__tela_matricula.pega_dados_matricula(turno, plano)["plano"]

            if plano_selecionado == "Diamond":
                plano_selecionado = Plano.Diamond
            elif plano_selecionado == "Gold":
                plano_selecionado = Plano.Gold
            elif plano_selecionado == "Silver":
                plano_selecionado = Plano.Silver
            else:
                self.__tela_matricula.mostra_mensagem("Plano inválido. Por favor, selecione um plano válido.")
                return

            mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano_selecionado)
            id_matricula = random.randint(1000, 9999)

            mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
            data_inicio_matricula = datetime.now()
            data_vencimento_matricula = data_inicio_matricula + timedelta(days=30)
            data_termino_matricula = data_inicio_matricula + timedelta(days=365)
            matricula = Matricula(id_matricula, turno, plano, mensalidade, aluno, data_inicio_matricula, data_vencimento_matricula, data_termino_matricula)
            self.__matriculas.append(matricula)
            self.__tela_matricula.mostra_mensagem(f"Matrícula realizada com sucesso!\nID da matrícula: {id_matricula}")


    def definir_mensalidade_de_acordo_com_plano(self, plano_selecionado):
        mensalidade = 0.0
        if plano_selecionado == Plano.Diamond:
            mensalidade = 350.0
        elif plano_selecionado == Plano.Gold:
            mensalidade += 250.0
        elif plano_selecionado == Plano.Silver:
            mensalidade = 150.0
        else:
            raise ValueError("Plano inválido")
        return mensalidade

    def cancelar_matricula(self):
        id_matricula_escolhida = self.__tela_matricula.seleciona_id_matricula()
        matricula = self.buscar_matricula_por_id(id_matricula_escolhida)
        if matricula:
            self.__matriculas.remove(matricula)
            self.__tela_matricula.mostra_mensagem("Matrícula cancelada com sucesso")
        else:
            self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

    def lista_matriculas(self):
        if not self.__matriculas:
            return self.__tela_matricula.mostra_mensagem("Não há matrículas cadastradas")
        else:
            for matricula in self.__matriculas:
                self.__tela_matricula.mostra_dados_matricula({
                                                              'id_matricula': matricula.id_matricula,
                                                              'aluno': matricula.aluno,
                                                              'turno': matricula.turno.name,
                                                              'plano': matricula.plano.name,
                                                              'mensalidade': matricula.mensalidade,
                                                              'data_inicio_matricula': matricula.data_inicio_matricula,
                                                              'data_vencimento_matricula': matricula.data_vencimento_matricula,
                                                              'data_termino_matricula': matricula.data_termino_matricula})

    def vizualizar_matricula_especifica(self):
        id_matricula = self.__tela_matricula.seleciona_id_matricula()
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula:
            self.__tela_matricula.mostra_dados_matricula(matricula)
        else:
            self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

    def buscar_matricula_por_id(self, id_matricula):
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                return matricula
        return None

    def alterar_plano(self, id_matricula):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula is None:
            return self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

        plano = self.__tela_matricula.seleciona_plano(self.__planos)
        matricula.plano = plano
        matricula.mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
        self.__tela_matricula.mostra_mensagem("Plano alterado com sucesso")

    def alterar_turno(self, id_matricula):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula is None:
            return self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

        turno = self.__tela_matricula.seleciona_turno(self.__turnos)
        matricula.turno = turno
        self.__tela_matricula.mostra_mensagem("Turno alterado com sucesso")

    def plano_mais_procurado(self):
        contagem_planos = {}
        for matricula in self.__matriculas:
            if matricula.plano not in contagem_planos:
                contagem_planos[matricula.plano] = 0
            contagem_planos[matricula.plano] += 1

        max_vendas = max(contagem_planos.values())
        planos_mais_procurados = [plano for plano, vendas in contagem_planos.items() if vendas == max_vendas]

        if len(planos_mais_procurados) > 1:
            nomes_planos = ", ".join(plano.name for plano in planos_mais_procurados)
            return self.__tela_matricula.relatorios(f"Há um empate entre os seguintes planos: {nomes_planos}")
        else:
            return self.__tela_matricula.relatorios(f"Plano mais vendido: {planos_mais_procurados[0].name}")

    def turno_mais_procurado(self):
        contagem_turnos = {}
        for matricula in self.__matriculas:
            if matricula.turno not in contagem_turnos:
                contagem_turnos[matricula.turno] = 0
            contagem_turnos[matricula.turno] += 1

        max_vendas = max(contagem_turnos.values())
        turnos_mais_procurados = [turno for turno, vendas in contagem_turnos.items() if vendas == max_vendas]

        if len(turnos_mais_procurados) > 1:
            nomes_turnos = ", ".join(turno.name for turno in turnos_mais_procurados)
            self.__tela_matricula.relatorios(f"Há um empate entre os seguintes turnos: {nomes_turnos}")
        else:
            self.__tela_matricula.relatorios(f"Turno mais vendido: {turnos_mais_procurados[0].name}")

    def abre_tela(self):
        lista_opcoes = {1: self.realizar_matricula, 2: self.cancelar_matricula, 3: self.lista_matriculas, 4: self.vizualizar_matricula_especifica,
                        5: lambda: self.alterar_plano(self.__tela_matricula.seleciona_id_matricula()),
                        6: lambda: self.alterar_turno(self.__tela_matricula.seleciona_id_matricula()),
                        7: self.plano_mais_procurado, 8: self.turno_mais_procurado, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_matricula.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
