import unittest
from hero import Hero

class TestHero(unittest.TestCase):
    def test_attack_mage(self):
        hero = Hero("Merlin", 200, "Mage")
        self.assertEqual(hero.attack(), "the mage attacked using magic")

    def test_attack_warrior(self):
        hero = Hero("Conan", 35, "Warrior")
        self.assertEqual(hero.attack(), "the warrior attacked using sword")

    def test_attack_monk(self):
        hero = Hero("Li Mei", 28, "Monk")
        self.assertEqual(hero.attack(), "the monk attacked using martial arts")

    def test_attack_ninja(self):
        hero = Hero("Hanzo", 40, "Ninja")
        self.assertEqual(hero.attack(), "the ninja attacked using shuriken")

    def test_unknown_type(self):
        hero = Hero("Unknown", 30, "Pirate")
        self.assertEqual(hero.attack(), "the pirate attacked using unknown attack")

if __name__ == '__main__':
    unittest.main()
