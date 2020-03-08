class Pessoa:

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.nome_completo = ''

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def nome_completo(self):
        return self._nome_completo

    @nome_completo.setter
    def nome_completo(self, nome_completo):
        if isinstance(nome_completo, str):
            nome_completo = f'{self._nome} {self._sobrenome}'
        self._nome_completo = nome_completo


# Este formato de Getter e Setter funciona junto da instancia da classe,
# sem a necessidade de serem chamados
nova_pessoa = Pessoa('Renan', 'Berti Ribas', 21)

# chamada dos Getters que retornam as variaveis privadas
print(nova_pessoa.nome)
print(nova_pessoa.sobrenome)
print(nova_pessoa.idade)
print(nova_pessoa.nome_completo)
