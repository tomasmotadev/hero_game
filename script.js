// Footer year
document.getElementById('year').textContent = new Date().getFullYear();

//
// Mobile Menu
//
// Menu mobile toggle
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('active');
});

// Dropdown Photography
const mobilePhotoBtn = document.getElementById('mobile-photography-btn');
const mobilePhotoMenu = document.getElementById('mobile-photography-menu');

mobilePhotoMenu.style.display = 'none';
mobilePhotoBtn.classList.remove('active');

mobilePhotoBtn.addEventListener('click', () => {
  const isOpen = mobilePhotoMenu.style.display === 'block';
  mobilePhotoMenu.style.display = isOpen ? 'none' : 'block';
  mobilePhotoBtn.classList.toggle('active', !isOpen);
});

// Dropdown Contact
const mobileContactBtn = document.getElementById('mobile-contact-btn');
const mobileContactMenu = document.getElementById('mobile-contact-menu');

mobileContactMenu.style.display = 'none';
mobileContactBtn.classList.remove('active');

mobileContactBtn.addEventListener('click', () => {
  const isOpen = mobileContactMenu.style.display === 'block';
  mobileContactMenu.style.display = isOpen ? 'none' : 'block';
  mobileContactBtn.classList.toggle('active', !isOpen);
});

// **Hero Class Logic (JavaScript)**

// Equivalent to your Python Hero class
class Hero {
    constructor(name, age, heroType) {
        this.name = name;
        this.age = age;
        this.heroType = heroType.toLowerCase();
    }

    attack() {
        const attacks = {
            "mage": "magic",
            "warrior": "sword",
            "monk": "martial arts",
            "ninja": "shuriken"
        };
        const attack = attacks[this.heroType] || "unknown attack";
        return `the ${this.heroType} attacked using ${attack}`;
    }
}

// Function to create a hero and display the attack result
function createAndAttack() {
    const name = document.getElementById('heroName').value;
    const age = document.getElementById('heroAge').value;
    const type = document.getElementById('heroType').value;
    const resultDiv = document.getElementById('result');

    if (!name || !age || !type) {
        resultDiv.textContent = "Please fill in all fields.";
        resultDiv.style.color = "var(--c-red)";
        return;
    }

    const hero = new Hero(name, age, type);
    const attackResult = hero.attack();
    
    resultDiv.innerHTML = `<div class="result-box">
        <p><strong>Name:</strong> ${hero.name}</p>
        <p><strong>Age:</strong> ${hero.age}</p>
        <p><strong>Type:</strong> ${hero.heroType}</p>
        <p><strong>Attack Result:</strong> ${attackResult}</p>
    </div>`;
    resultDiv.style.color = "var(--c-blue)";
}
