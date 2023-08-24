class Conta:
    
    def __init__(self, id, nome, saldo):
        self.__id = id
        self.__nome = nome
        self.__saldo = saldo
        self.__codigo_banco = "001"
        
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__nome))
    
    def deposita(self, valor):
        self.__saldo += valor
        
    def debitar(self, valor):
        self.__saldo -= valor
        
    @property
    def saldo(self):
            return self.__saldo
    
    @property
    def nome(self):
        return self.__nome
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}   
        
conta01 = Conta(1, 'Luan', 1700)
conta02 = Conta(2, 'Esther', 2400)
conta01.extrato()
conta02.extrato()
conta01.deposita(500)
conta01.extrato()
conta02.extrato()
conta01.debitar(1000)
conta01.extrato()
