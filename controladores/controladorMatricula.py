from modelos.matricula import Matricula
from telas.telaMatricula import TelaMatricula
from controladores.controladorSistema import ControladorSistema
from controladores.controladorAluno import ControladorAluno
from modelos.plano import Plano
from modelos.turno import Turno
from datetime import datetime, timedelta
import random


class ControladorMatricula:
    def __init__(self):
        self.__controlador_sistema = ControladorSistema()
        self.__tela_matricula = TelaMatricula()
        self.__matriculas = []
        self.__alunos = []
    
        
    def mostrar_matriculas_cadastradas(self):
        if not self.__matriculas:
            return "Não há nenhuma matrícula cadastrada no momento."
        else:
            for matricula in self.__matriculas:
                 return "-------- Dados da Matrícula ----------\n" \
                           f"Nome: {matricula.aluno.nome}\n" \
                           f"Plano: {matricula.plano}\n" \
                           f"Turno: {matricula.turno}\n" \
                           f"Data de Início: {matricula.data_inicio_matricula}\n" \
                           f"Data de Término: {matricula.data_termino_matricula}\n" \
                           f"Data de Vencimento da Mensalidade: {matricula.data_vencimento_matricula}\n" \
                           f"Mensalidade: {matricula.mensalidade}"
        
    def aluno_esta_matriculado(self, aluno):
        for matricula in self.__matriculas:
            if matricula.aluno == aluno:
                return True
        return False
    
    def realizar_matricula(self):
        aluno = self.__tela_matricula.seleciona_aluno(self.__alunos)
        if self.aluno_esta_matriculado(aluno):
            return self.__tela_matricula.mostra_mensagem("Aluno já está matriculado")
    
        plano = self.__tela_matricula.seleciona_plano(self.__planos)
        turno = self.__tela_matricula.seleciona_turno(self.__turnos)
        id_matricula = random.randint(1000, 9999)
    
        mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
        data_inicio_matricula = datetime.now()
        data_vencimento_matricula = data_inicio_matricula + timedelta(days=30)
        data_termino_matricula = data_inicio_matricula + timedelta(days=365)
        matricula = Matricula(id_matricula, aluno, plano, turno, mensalidade, data_inicio_matricula, data_vencimento_matricula, data_termino_matricula)
        self.__matriculas.append(matricula)

    
    def definir_mensalidade_de_acordo_com_plano(self, plano_selecionado):
        mensalidade = 0.0
        if plano_selecionado == Plano.Diamond:
            mensalidade = 250.0
        elif plano_selecionado == Plano.Gold:
            mensalidade += 150.0
        elif plano_selecionado == Plano.Silver:
            mensalidade = 200.0
        else:
            raise ValueError("Plano inválido")
        return mensalidade
    
    
    def cancelar_matricula(self, id_matricula):
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                self.__matriculas.remove(id_matricula)
                return id_matricula
        return id_matricula
    
    def mostrar_dados_matricula_aluno_escolhido(self):
        aluno_selecionado = self.__tela_matricula.seleciona_aluno(self.__alunos)
        if aluno_selecionado:
            for matricula in self.__matriculas:
                if matricula.aluno == aluno_selecionado:
                    return "-------- Dados da Matrícula ----------\n" \
                           f"Nome: {matricula.aluno.nome}\n" \
                           f"Plano: {matricula.plano}\n" \
                           f"Turno: {matricula.turno}\n" \
                           f"Data de Início: {matricula.data_inicio_matricula}\n" \
                           f"Data de Término: {matricula.data_termino_matricula}\n" \
                           f"Data de Vencimento da Mensalidade: {matricula.data_vencimento_matricula}\n" \
                           f"Mensalidade: {matricula.mensalidade}"
            
    
    def buscar_matricula_por_id(self, id_matricula):
        for matricula in self.__matriculas:
            if matricula.id_matricula == id_matricula:
                return matricula
        return None
            
    
    def alterar_dados_matricula(self):
        id_matricula = self.__tela_matricula.alterar_dados_matricula()
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula:
            opcoes = {1: self.alterar_plano, 2: self.alterar_turno}
            opcao = self.__tela_matricula.tela_opcoes()
            opcoes[opcao](matricula)
        else:
            return self.__tela_matricula.mostra_mensagem("Matrícula não encontrada")

    def plano_mais_procurado(self):
        contagem_planos = {plano: 0 for plano in Plano}
        for matricula in self.__matriculas:
            contagem_planos[matricula.plano] += 1
        max_vendas = 0
        plano_mais_procurado = None
        for plano, vendas in contagem_planos.items():
            if vendas > max_vendas:
                max_vendas = vendas
                plano_mais_procurado = plano
        planos_mais_procurados = []
        for plano, vendas in contagem_planos.items():
            if vendas == max_vendas:
                planos_mais_procurados.append(plano)
        if len(planos_mais_procurados) > 1:
            nomes_planos = ""
            for plano in planos_mais_procurados:
                if nomes_planos != "":
                    nomes_planos += ", "
                nomes_planos += plano.name
            return f"Há um empate entre os seguintes planos: {nomes_planos}"
        else:
            return f"Plano mais vendido: {planos_mais_procurados[0].name}"
        
    def turno_mais_procurado(self):
        pass
    
    def abre_tela(self):
        lista_opcoes = {1: self.mostrar_matriculas_cadastradas, 2: self.realizar_matricula, 3: self.cancelar_matricula, 4: self.mostrar_dados_matricula_aluno_escolhido, 5: self.alterar_dados_matricula, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_matricula.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()