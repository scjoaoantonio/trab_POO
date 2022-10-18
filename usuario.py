# Classe de Usuário
class Usuario():
    def __init__(self, id, nome, idade, email):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email

    # Imprime o dado do usuário na tela
    def listarDados(self):
        print("ID = {} Nome = {} Idade = {} Email = {}".format(
            self.id, self.nome, self.idade, self.email))


# Pessoa Física, (Filha de Usuário)
class PessoaFisica(Usuario):
    def __init__(self, id, cpf, nome, idade, email, endereço, carrinho):
        super().__init__(id, nome, idade, email)
        self.CPF = cpf
        self.endereço = endereço
        self.carrinho = carrinho

    # Imprime os dados do usuário
    def listarDados(self):
        print("ID = {} Nome = {} CPF = {} Idade = {} Email = {}".format(
            self.id, self.nome, self.CPF, self.idade, self.email))

    def get_id(self):
        return self.id

    def get_doc(self):
        return self.CPF


# Pessoa Jurídica (Filha de Usuário)
class PessoaJuridica(Usuario):
    def __init__(self, id, cnpj, nome, idade, email, carrinho):
        super().__init__(id, nome, idade, email)
        self.CNPJ = cnpj
        self.carrinho = carrinho

    # Imprime os dados do usuário
    def listarDados(self):
        print("ID = {} Nome = {} CNPJ = {} Email = {}".format(
            self.id, self.nome, self.CNPJ, self.email))

    def get_id(self):
        return self.id

    def get_doc(self):
        return self.CNPJ


# Classe Endereço
class Endereço():
    def __init__(self, cep):
        self.CEP = cep

    # Imprime Endereço
    def listarDados(self):
        print("CEP: {}".format(self.CEP))
