from telas.telaAbstrata import TelaAbstrata

class TelaMatricula(TelaAbstrata):
    def tela_opcoes(self):
        print("----------- Matrículas ------------")
        print("1 - Mostrar matrículas cadastradas")
        print("2 - Realizar matrícula")
        print("3 - Cancelar matrícula")
        print("4 - Mostrar dados da matrícula")
        print("5 - Alterar algum dado da matrícula")
        print("0 - Voltar ao menu inicial")
        opcao = int(input("Insira a opção escolhida: "))
        return opcao

    def pega_dados_matricula(self):
        print("----------- Realizar matrícula ------------")
        aluno = input("Insira o nome do aluno: ")
        plano = input("Insira o plano do curso: ")
        turno = input("Insira o turno do curso: ")
        return {"aluno": aluno, "plano": plano, "turno": turno}
    
    
    def mostra_matricula(self, dados_matricula):
        print("----------- Matrícula ------------")
        print(f"ID matricula: {dados_matricula['id_matricula']}")
        print(f"Aluno: {dados_matricula['aluno']}")
        print(f"Plano: {dados_matricula['plano']}")
        print(f"Turno: {dados_matricula['turno']}")
        print(f"Data da matrícula: {dados_matricula['data_matricula']}")
        print(f"Data de vencimento: {dados_matricula['data_vencimento']}")
        print(f"Valor da matrícula: {dados_matricula['valor_matricula']}")

    def seleciona_aluno(self, alunos):
        print("Selecione o aluno:")
        for i, aluno in enumerate(alunos):
            print(f"{i} - {aluno}")
        aluno_selecionado = int(input("Insira nome do aluno: "))
        return alunos[aluno_selecionado]

    def seleciona_plano(self, planos):
        print("Selecione o curso:")
        for i, plano in enumerate(planos):
            print(f"{i} - {plano}")
        plano_selecionado = int(input("Insira o plano do curso escolhido: "))
        return planos[plano_selecionado]

    def seleciona_turno(self, turnos):
        print("Selecione o turno:")
        for i, turno in enumerate(turnos):
            print(f"{i} - {turno}")
        turno_selecionado = int(input("Insira o número do turno escolhido: "))
        return turnos[turno_selecionado]
    
    def cancelar_matricula(self):
        print("Insira o ID da matrícula que deseja cancelar")
        id_matricula = int(input("ID: "))
        return id_matricula
    
    def plano_mais_procurado(self, plano):
        print("Plano mais procurado: ", plano)
    
    def turno_mais_procurado(self, turno):
        print("Turno mais procurado: ", turno)
    
    def alterar_dados_matricula(self):
        print("Insira o ID da matrícula que deseja alterar")
        id_matricula = int(input("ID: "))
        return id_matricula