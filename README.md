# Hero Game - DIO Challenge Project

This project implements a simple class representing an adventure hero with basic properties and a customized attack method based on the hero type.

## Features

- `Hero` class with properties:
  - name
  - age
  - hero_type (warrior, mage, monk, ninja)
- `attack()` method returns a custom attack message depending on the hero type:
  - mage -> uses magic
  - warrior -> uses sword
  - monk -> uses martial arts
  - ninja -> uses shuriken

## How to use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hero_game.git
   cd hero_game
   ```

2. Run the main file:
   ```bash
   python hero.py
   ```

3. To run automated tests:
   ```bash
   python -m unittest test_hero.py
   ```

## Project Structure

- `hero.py` - Hero class and main execution
- `test_hero.py` - Unit tests
- `README.md` - Project documentation

---

### Next steps

You can improve this project by adding:

- New hero types
- Methods for defense, healing, different magic attacks
- Interaction between heroes in battles
