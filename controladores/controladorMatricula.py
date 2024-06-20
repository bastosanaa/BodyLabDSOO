from DAOs.matricula_dao import MatriculaDAO
from Exception.AlunoDuplicado import AlunoDuplicado
from modelos.matricula import Matricula
from Exception.AlunoNaoCadastrado import AlunoNaoCadastrado
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
        self.__matriculas_dao = MatriculaDAO()
        self.__planos = [Plano.Silver, Plano.Gold, Plano.Diamond]
        self.__turnos = [Turno.Matutino, Turno.Vespertino, Turno.Noturno]


    def aluno_esta_matriculado(self, nome_aluno):
        for matricula in self.__matriculas_dao.get_all():
            if matricula.aluno == nome_aluno:
                return True
        return False

    def realizar_matricula(self):
        dados_matricula = self.__tela_matricula.pega_dados_matricula(self.__turnos, self.__planos)
        aluno = dados_matricula['aluno']
        try:
            if not self.__controlador_sistema.controlador_aluno.aluno_esta_cadastrado(aluno):
                raise AlunoNaoCadastrado()
            if self.aluno_esta_matriculado(aluno):
                raise AlunoDuplicado()
            else:
                turno = dados_matricula['turno']
                plano = dados_matricula['plano']

                if plano == "Diamond":
                    plano = Plano.Diamond
                elif plano == "Gold":
                    plano = Plano.Gold
                elif plano == "Silver":
                    plano = Plano.Silver
                else:
                    self.__tela_matricula.mostra_mensagem("Plano inválido. Por favor, selecione um plano válido.")
                    return

                id_matricula = random.randint(1000, 9999)
                mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
                data_inicio_matricula = datetime.now()
                data_vencimento_matricula = data_inicio_matricula + timedelta(days=30)
                data_termino_matricula = data_inicio_matricula + timedelta(days=365)
                matricula = Matricula(id_matricula, turno, plano, mensalidade, aluno, data_inicio_matricula,
                                      data_vencimento_matricula, data_termino_matricula)
                self.__matriculas_dao.add(matricula)
                self.__tela_matricula.mostra_mensagem(f"Matrícula realizada com sucesso!\nID da matrícula: {id_matricula}")
        except AlunoNaoCadastrado as e:
            self.__tela_matricula.mostra_mensagem(str(e))
        except AlunoDuplicado as e:
            self.__tela_matricula.mostra_mensagem(str(e))

    def definir_mensalidade_de_acordo_com_plano(self, plano):
        mensalidade = 0.0
        if plano == Plano.Diamond:
            mensalidade = 350.0
        elif plano == Plano.Gold:
            mensalidade += 250.0
        elif plano == Plano.Silver:
            mensalidade = 150.0
        else:
            raise ValueError("Plano inválido")
        return mensalidade

    def cancelar_matricula(self):
        id_matricula_escolhida = self.__tela_matricula.seleciona_id_matricula()
        matricula = self.buscar_matricula_por_id(id_matricula_escolhida)
        if matricula:
            self.__matriculas_dao.remove(matricula)
            self.__tela_matricula.mostra_mensagem("Matrícula cancelada com sucesso")
        else:
            self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

    def lista_matriculas(self):
        matriculas = self.__matriculas_dao.get_all()
        if not matriculas:
            return self.__tela_matricula.mostra_mensagem("Não há matrículas cadastradas")
        else:
            for matricula in matriculas:
                self.__tela_matricula.lista_de_matricula({
                    'id_matricula': matricula.id_matricula,
                    'aluno': matricula.aluno,
                    'turno': matricula.turno,
                    'plano': matricula.plano.name,
                    'mensalidade': matricula.mensalidade,
                    'data_inicio_matricula': matricula.data_inicio_matricula,
                    'data_vencimento_matricula': matricula.data_vencimento_matricula,
                    'data_termino_matricula': matricula.data_termino_matricula})

    def vizualizar_matricula_especifica(self):
        id_matricula = self.__tela_matricula.seleciona_id_matricula()
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula:
            dados_matricula = {
                'id_matricula': matricula.id_matricula,
                'aluno': matricula.aluno,
                'turno': matricula.turno,
                'plano': matricula.plano.name,
                'mensalidade': matricula.mensalidade,
                'data_inicio_matricula': matricula.data_inicio_matricula,
                'data_vencimento_matricula': matricula.data_vencimento_matricula,
                'data_termino_matricula': matricula.data_termino_matricula
            }
            self.__tela_matricula.mostra_matricula(dados_matricula)
        else:
            self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")


    def buscar_matricula_por_id(self, id_matricula):
        return self.__matriculas_dao.get(id_matricula)

    def alterar_plano(self, id_matricula):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula is None:
            return self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

        plano = self.__tela_matricula.pega_dados_plano()
        if plano == "Diamond":
            plano = Plano.Diamond
        elif plano == "Gold":
            plano = Plano.Gold
        elif plano == "Silver":
            plano = Plano.Silver
        else:
            self.__tela_matricula.mostra_mensagem("Plano inválido. Por favor, selecione um plano válido.")
            return

        matricula.plano = plano
        matricula.mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
        self.__tela_matricula.mostra_mensagem("Plano alterado com sucesso")

    def alterar_turno(self, id_matricula):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula is None:
            return self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

        turno_str = self.__tela_matricula.pega_dados_turno()
        if turno_str == "Matutino":
            turno = Turno.Matutino
        elif turno_str == "Vespertino":
            turno = Turno.Vespertino
        elif turno_str == "Noturno":
            turno = Turno.Noturno
        else:
            self.__tela_matricula.mostra_mensagem("Turno inválido. Por favor, selecione um turno válido.")
            return

        matricula.turno = turno
        self.__tela_matricula.mostra_mensagem("Turno alterado com sucesso")

    def plano_mais_procurado(self):
        contagem_planos = {}
        for matricula in self.__matriculas_dao.get_all():
            if matricula.plano not in contagem_planos:
                contagem_planos[matricula.plano] = 0
            contagem_planos[matricula.plano] += 1

        max_vendas = max(contagem_planos.values())
        planos_mais_procurados = [plano for plano, vendas in contagem_planos.items() if vendas == max_vendas]

        if len(planos_mais_procurados) > 1:
            nomes_planos = ", ".join(plano.name for plano in planos_mais_procurados)
            return self.__tela_matricula.relatorios(f"Os planos mais vendidos são: {nomes_planos}")
        else:
            return self.__tela_matricula.relatorios(f"Plano mais vendido: {planos_mais_procurados[0].name}")

    def turno_mais_procurado(self):
        contagem_turnos = {}
        for matricula in self.__matriculas_dao.get_all():
            if matricula.turno not in contagem_turnos:
                contagem_turnos[matricula.turno] = 0
            contagem_turnos[matricula.turno] += 1

        max_vendas = max(contagem_turnos.values())
        turnos_mais_procurados = [turno for turno, vendas in contagem_turnos.items() if vendas == max_vendas]

        if len(turnos_mais_procurados) > 1:
            nomes_turnos = ", ".join(turno for turno in turnos_mais_procurados)
            self.__tela_matricula.relatorios(f"Os turnos mais procurados são: {nomes_turnos}")
        else:
            self.__tela_matricula.relatorios(f"Turno mais vendido: {turnos_mais_procurados[0]}")

    def abre_tela(self):
        lista_opcoes = {1: self.realizar_matricula, 2: self.cancelar_matricula, 3: self.lista_matriculas,
                        4: self.vizualizar_matricula_especifica,
                        5: lambda: self.alterar_plano(self.__tela_matricula.seleciona_id_matricula()),
                        6: lambda: self.alterar_turno(self.__tela_matricula.seleciona_id_matricula()),
                        7: self.plano_mais_procurado, 8: self.turno_mais_procurado, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_matricula.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
