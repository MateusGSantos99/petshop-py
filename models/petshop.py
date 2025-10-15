class PetShop:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []
        self.clientes = []
        self.vendas = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_animal(self, nome):
        for animal in self.animais:
            if animal.nome.lower() == nome.lower():
                return animal
        return None

    def buscar_cliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower():
                return cliente
        return None

    def vender_animal(self, nome_animal, nome_cliente):
        animal = self.buscar_animal(nome_animal)
        cliente = self.buscar_cliente(nome_cliente)

        if animal and cliente:
            cliente.adicionar_compra(animal)
            self.animais.remove(animal)
            self.vendas.append((cliente.nome, animal.nome, animal.get_preco()))
            print(f"Venda realizada! {animal.nome} vendido para {cliente.nome}")
        else:
            print("Erro: Animal ou cliente não encontrado.")

    def listar_animais_disponiveis(self):
        if not self.animais:
            print("Nenhum animal disponível no momento.")
        else:
            for animal in self.animais:
                print(f"{animal.nome} ({type(animal).__name__}) - {animal.idade} anos - R$ {animal.get_preco():.2f}")

    def relatorio_vendas(self):
        if not self.vendas:
            print("Nenhuma venda realizada ainda.")
        else:
            print("=== RELATÓRIO DE VENDAS ===")
            for venda in self.vendas:
                print(f"{venda[1]} vendido para {venda[0]} por R$ {venda[2]:.2f}")
