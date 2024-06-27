class OpcaoInvalida(Exception):
    def __init__(self):
        super().__init__("Nenhum campo preenchido ou opção inválida. Tente novamente.")