class unitPrice(Exception):
    f"""Erro no preço únitario"""
    def __init__(self, mensagem="Erro no preço únitario"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)