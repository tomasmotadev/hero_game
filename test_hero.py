import unittest
from hero import Heroi

class TestHeroi(unittest.TestCase):
    def test_ataque_mago(self):
        heroi = Heroi("Merlin", 200, "Mago")
        self.assertEqual(heroi.atacar(), "o mago atacou usando magia")

    def test_ataque_guerreiro(self):
        heroi = Heroi("Conan", 35, "Guerreiro")
        self.assertEqual(heroi.atacar(), "o guerreiro atacou usando espada")

    def test_ataque_monge(self):
        heroi = Heroi("Li Mei", 28, "Monge")
        self.assertEqual(heroi.atacar(), "o monge atacou usando artes marciais")

    def test_ataque_ninja(self):
        heroi = Heroi("Hanzo", 40, "Ninja")
        self.assertEqual(heroi.atacar(), "o ninja atacou usando shuriken")

    def test_tipo_desconhecido(self):
        heroi = Heroi("Desconhecido", 30, "Pirata")
        self.assertEqual(heroi.atacar(), "o pirata atacou usando ataque desconhecido")

if __name__ == '__main__':
    unittest.main()
