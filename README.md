
# 🎲 Dice Roller – Simulateur de Lancer de Dé

Une petite application web ludique développée en Python avec Flask qui simule le lancer d'un dé classique à 6 faces.

## 🚀 Fonctionnalités

- Lance un dé à 6 faces en un clic
- Affiche le chiffre obtenu et l’image correspondante
- Interface simple et responsive
- Images personnalisées faites à la main ✍️

## 🛠️ Technologies utilisées

- Python 3
- Flask
- HTML/CSS
- (Images personnalisées dans `/static/images`)

## 📦 Installation

```bash
git clone https://github.com/ton-utilisateur/Dice-roller.git
cd Dice-roller
pip install -r requirements.txt
```

## ▶️ Lancer l'application

```bash
python main.py
```

Puis ouvre ton navigateur sur :
👉 `http://localhost:5000`

## 📂 Arborescence du projet
dice-roller/
├── main.py                 # Code principal Flask
├── templates/
│   └── index.html          # Interface utilisateur
├── static/
│   ├── style.css           # Styles CSS
│   └── images/             # Faces du dé (dice1.png à dice6.png)
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation du projet
