"""
Orientação a Objetos
Prática - criando classes, construtores e métodos
Desafios

1. Crie uma classe chamada ContaBancaria com um 
construtor que aceita os parâmetros titular e saldo. 
Inicie o atributo ativo como False por padrão.
"""
class ContaBancaria():
    def __init__(
            self, 
            titular: str, 
            saldo: float, 
            ativo: bool = False
            ):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    """
    2. Na classe ContaBancaria, adicione um método 
    especial __str__ que retorna uma mensagem 
    formatada com o titular e o saldo da conta. 
    Crie duas instâncias da classe e imprima essas 
    instâncias.
    """
    def __str__(self):
        return f"Titular: {self.titular}\nSaldo: {self.saldo:.2f}"
    
    """
    3. Adicione um método de classe chamado 
    ativar_conta à classe ContaBancaria que define o 
    atributo ativo como True. 
    Crie uma instância da classe, chame o método de 
    classe e imprima o valor de ativo.
    """
    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

"""
4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
"""
class ContaBancariaPythonica():
    def __init__(
            self,
            titular: str,
            saldo: float,
            ativo: bool = False
            ):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo
        
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True


"""
5. Crie uma instância da classe e imprima o valor da propriedade titular.
"""
"""
6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
"""
class ClienteBanco():
    def __init__(self, nome, idade, cpf, tipo_conta, saldo = 0.0):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self._saldo = saldo

    """
    7. Crie um método de classe para a conta ClienteBanco.
    """
    @classmethod
    def fazer_deposito(cls, conta, valor):
        conta._saldo += valor

if __name__ == "__main__":
    # 2. Crie duas instâncias da classe e imprima essas instâncias.
    conta1 = ContaBancaria("Maria Silva", 1090.60)
    conta2 = ContaBancaria("João Costa", 213.40)
    print(conta1)
    print(conta2)

    # 3. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    conta3 = ContaBancaria("José Ribeiro", 427.90)
    ContaBancaria.ativar_conta(conta3)
    print(conta3.ativo)

    # 5. Crie uma instância da classe e imprima o valor da propriedade titular.
    conta_pythonica = ContaBancariaPythonica("Ana Pereira", 832,10)
    print(conta_pythonica.titular)
    
    # 6. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
    cliente1 = ClienteBanco("Maria Silva", 19, 12345678901, "Poupança")
    cliente2 = ClienteBanco("João Costa", 45, 10987654321, "Corrente", 213.40)
    cliente3 = ClienteBanco("José Ribeiro", 70, 873098903030, "Corrente")
