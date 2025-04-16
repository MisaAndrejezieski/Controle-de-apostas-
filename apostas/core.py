class Aposta:
    def __init__(self, data, descricao, valor_apostado, odd, resultado):
        self.data = data
        self.descricao = descricao
        self.valor_apostado = valor_apostado
        self.odd = odd
        self.resultado = resultado.lower()

    @property
    def valor_ganho(self):
        if self.resultado == 'ganhou':
            return self.valor_apostado * self.odd
        return 0

class ControleApostas:
    def __init__(self):
        self.apostas = []

    def adicionar_aposta(self, aposta):
        self.apostas.append(aposta)

    @property
    def total_apostado(self):
        return sum(aposta.valor_apostado for aposta in self.apostas)

    @property
    def total_ganho(self):
        return sum(aposta.valor_ganho for aposta in self.apostas)

    @property
    def lucro_total(self):
        return self.total_ganho - self.total_apostado

    def resumo(self):
        return (
            f"\nResumo Geral:\n"
            f"Total Apostado: R$ {self.total_apostado:.2f}\n"
            f"Total Ganho: R$ {self.total_ganho:.2f}\n"
            f"Lucro Total: R$ {self.lucro_total:.2f}"
        )

    def historico(self):
        historico = ["\nHistórico de Apostas:"]
        for i, aposta in enumerate(self.apostas, 1):
            historico.append(
                f"\nAposta {i}:\n"
                f"Data: {aposta.data}\n"
                f"Descrição: {aposta.descricao}\n"
                f"Valor Apostado: R$ {aposta.valor_apostado:.2f}\n"
                f"Odd: {aposta.odd}\n"
                f"Resultado: {aposta.resultado.upper()}\n"
                f"Valor Ganho: R$ {aposta.valor_ganho:.2f}"
            )
        return "\n".join(historico)