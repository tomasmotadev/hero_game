class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }

        ataque = ataques.get(self.tipo, "ataque desconhecido")
        return f"o {self.tipo} atacou usando {ataque}"

if __name__ == "__main__":
    heroi1 = Heroi("Gandalf", 150, "Mago")
    print(heroi1.atacar())
