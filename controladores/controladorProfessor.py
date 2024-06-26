from telas.telaProfessor import TelaProfessor
from Exception.ProfessorDuplicado import ProfessorDuplicado
from modelos.professor import Professor
from DAOs.professor_dao import ProfessorDAO
from modelos.turno import Turno

class ControladorProfessor():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_professor = TelaProfessor()
        self.__professores_dao = ProfessorDAO()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastar_professor,
            2: self.remover_professor,
            3: self.selecionar_professor_a_alterar,
            4: self.listar_professores,
            5: self.relatorio_professores_turno,
            0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastar_professor(self):
        try:
            dados_professor = self.__tela_professor.pega_dados_novo_professor()
            nome = dados_professor['nome']
            cpf = dados_professor['cpf']
            numero_telefone = dados_professor['numero_telefone']
            email = dados_professor['email']
            turno = self.converte_string_em_Turno(dados_professor['turno'])
            salario = dados_professor['salario']

            try:
                for professor in self.__professores_dao.get_all():
                    if professor.cpf == cpf or professor.nome == nome:
                        raise ProfessorDuplicado
                novo_professor = Professor(cpf, nome, numero_telefone, email, turno, salario)
                self.__professores_dao.add(novo_professor)
                self.__tela_professor.mostra_mensagem("Professor adicionado com sucesso!")
            except ProfessorDuplicado:
                self.__tela_professor.mostra_mensagem("Erro. Este professor já está cadastrado no sistema.")
        except TypeError:
            self.__tela_professor.mostra_mensagem("Operação Cancelada.")

    def listar_professores(self):
        professores = self.__professores_dao.get_all()
        if not professores:
            self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistema")
            return
        dados_professores = []
        for professor in professores:
            turno_convertido = self.converte_Turno_em_string(professor.turno)
            dados_professor = {
                'nome': professor.nome,
                'cpf': professor.cpf,
                'numero_telefone' : professor.numero_telefone,
                'email': professor.email,
                'turno': turno_convertido,
                'salario': professor.salario
            }
            dados_professores.append(dados_professor)
        self.__tela_professor.mostra_professor(dados_professores)
        

    def selecionar_professor_a_alterar(self):
        if self.__professores_dao.get_all():
            try:
                cpf = self.__tela_professor.pega_dados_alterar_professor()

                for professor in self.__professores_dao.get_all():
                    if professor.cpf == cpf:
                        turno_convertido = self.converte_Turno_em_string(professor.turno)
                        dados_professor = {
                        'nome': professor.nome,
                        'cpf': professor.cpf,
                        'numero_telefone' : professor.numero_telefone,
                        'email': professor.email,
                        'turno': turno_convertido,
                        'salario': professor.salario
                        }
                        self.alterar_professor_selecionado(professor,dados_professor)
                        return
            except TypeError as e:
                print(e)
                self.__tela_professor.mostra_mensagem("Operação Cancelada.")
                return
        else:
            self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistemaaaaaaaaaa")

    def alterar_professor_selecionado(self, professor, dados_professor):
        novos_dados_professor = self.__tela_professor.pega_alteracoes_professor(dados_professor)
        professor.nome = novos_dados_professor["nome"]
        professor.numero_telefone = novos_dados_professor["numero_telefone"]
        professor.email = novos_dados_professor["email"]
        professor.turno = self.converte_string_em_Turno(novos_dados_professor["turno"])
        professor.salario = int(novos_dados_professor["salario"])
        self.__professores_dao.update(professor)
        self.__tela_professor.mostra_mensagem("Professor alterado com sucesso!!")


    def remover_professor(self):
        if self.__professores_dao.get_all():
            try:
                cpf = self.__tela_professor.pega_dados_remover_professor()
                if not cpf:
                    raise TypeError
                professor = self.__professores_dao.get(cpf)
                if not professor:
                    self.__tela_professor.mostra_mensagem("Tente novamente. Professor não encontrado no sistema.")
                    return
                self.__professores_dao.remove(cpf)
                self.__tela_professor.mostra_mensagem("Professor removido com sucesso!")
                return
            except TypeError:
                self.__tela_professor.mostra_mensagem("Operação Cancelada.")
                return
        else:
            self.__tela_professor.mostra_mensagem("Nenhum professor cadastrado no sistema")

    def relatorio_professores_turno(self):
        professores_por_turno = {
            'matutino': 0,
            'vespertino': 0,
            'noturno': 0
        }
        professores = self.__professores_dao.get_all()
        if professores:
            for professor in professores:
                turno_convertido = self.converte_Turno_em_string(professor.turno)
                professores_por_turno[turno_convertido] += 1
            
        self.__tela_professor.mostrar_relatorio_prof_turno(professores_por_turno)

    def converte_string_em_Turno(self, string_turno):

        string_para_capitalizada = {
            "matutino": "Matutino",
            "vespertino" : "Vespertino",
            "noturno": "Noturno"
        }

        string_capitalizada = string_para_capitalizada[string_turno]
        turno  = Turno[string_capitalizada]
        return turno
    
    def converte_Turno_em_string(self, turno):
        
        turno_para_string = {
            Turno.Matutino: "matutino",
            Turno.Vespertino: "vespertino",
            Turno.Noturno: "noturno"
        }

        string_turno = turno_para_string[turno]
        return string_turno
        


