class Conta:
    def __init__(self, titular, number, saldo):
        self.titular = titular
        self.number = number
        self.saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo <0:
            print("O novo saldo não pode ser negativo")
        else:
            self._saldo = novo_saldo
    
    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("saldo retirado com sucesso")
        else:
            print("saldo insuficiente")
    
    def deposita(self, saldo):
        self.saldo+=valor
    
    def extrato(self):
        print("Client: {self.titular} | Saldo Atual: {self.saldo}")