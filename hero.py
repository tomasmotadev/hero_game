class Hero:
    def __init__(self, name, age, hero_type):
        self.name = name
        self.age = age
        self.hero_type = hero_type.lower()

    def attack(self):
        attacks = {
            "mage": "magic",
            "warrior": "sword",
            "monk": "martial arts",
            "ninja": "shuriken"
        }

        attack = attacks.get(self.hero_type, "unknown attack")
        return f"the {self.hero_type} attacked using {attack}"

if __name__ == "__main__":
    hero1 = Hero("Gandalf", 150, "Mage")
    print(hero1.attack())
