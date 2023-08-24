    # '_' = privado/protected (public _)
    # '__" privado (_NOMECLASSE__nomeatributo)

class BaseDeDados: 
    
    # init é um construtor
    # O underline '__' antes do atributo "dados" serve para
    # o sistema não recomendar sua modificação
    
    def __init__(self):
        self.__dados = {}
        
    @property
    def dados(self):
        return self.__dados    
        
    # Na primeira vez que for usado, vai ser criado o
    # dicionário, nas próximas, o dicionário vai ser
    # atualizado
        
    def inserir_cliente(self, id, nome):
            if 'clientes' not in self.__dados:
                self.__dados['clientes'] = {id: nome}
            else: 
                self.__dados['clientes'].update({id: nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):  
        del self.__dados['clientes'] [id]
        
bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
print(bd.dados)

