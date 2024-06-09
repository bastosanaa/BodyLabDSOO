from telas.telaAbstrata import TelaAbstrata

class TelaMatricula(TelaAbstrata):
    def tela_opcoes(self):
        print("----------- Matrículas ------------")
        print("1 - Realizar Matrícula")
        print("2 - Cancelar Matrícula")
        print("3 - Listar Matrículas")
        print("4 - Vizualizar Matricula Específica")
        print("5 - Alterar Plano")
        print("6 - Alterar Turno")
        print("7 - Plano mais procurado")
        print("8 - Turno mais procurado")
        print("0 - Voltar ao menu inicial")
        opcao = int(input("Insira a opção escolhida: "))
        return opcao

    def pega_dados_matricula(self, turnos, planos):
        print("----------- Realizar matrícula ------------")
        aluno = input("Insira o nome do aluno: ")
        turno = self.seleciona_turno(turnos)
        plano = self.seleciona_plano(planos)
        return {"aluno": aluno, "turno": turno, "plano": plano}
    
    def seleciona_plano(self, planos):
        print("Selecione o plano:")
        for i, plano in enumerate(planos):
            print(f"{i} - {plano}")
        plano_selecionado = int(input("Insira o número do plano escolhido: "))
        return planos[plano_selecionado]

    def seleciona_turno(self, turnos):
        print("Selecione o turno:")
        for i, turno in enumerate(turnos):
            print(f"{i} - {turno}")
        turno_selecionado = int(input("Insira o número do turno escolhido: "))
        return turnos[turno_selecionado]

    def seleciona_id_matricula(self):
        id_matricula = int(input("Insira o id da matrícula: "))
        return id_matricula

    def mostra_dados_matricula(self, matricula):
        print("-------- Dados da Matrícula ----------")
        print(f"ID: {matricula.id_matricula}")
        print(f"Aluno: {matricula.aluno.nome}")
        print(f"Turno: {matricula.turno.name}")
        print(f"Plano: {matricula.plano.name}")
        print(f"Mensalidade: {matricula.mensalidade}")
        print(f"Data de Início: {matricula.data_inicio_matricula}")
        print(f"Data de Vencimento: {matricula.data_vencimento_matricula}")
        print(f"Data de Término: {matricula.data_termino_matricula}")

    def relatorios(self, resultado):
        print(resultado)
    def mostra_mensagem(self, msg):

        print(msg)