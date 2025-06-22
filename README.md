# 🧠 Mall Customer Segmentation Project

Ce projet de Data Science a pour objectif d'explorer deux types d'analyses :

- 📊 **Partie A – Clustering** : Segmenter les clients d’un centre commercial selon leur âge, revenu et score de dépense.
- 📈 **Partie B – Régression** : Prédire le prix médian des maisons en Californie selon des variables socio-économiques.

---

## 📁 Structure du projet

mall_customer_segmentation_project/
│
├── data/
│ ├── mall/ # Données pour le clustering
│ │ └── Mall_Customers.csv
│ └── housing/ # Données pour la régression
│ └── california_housing.csv
│
├── notebooks/
│ ├── clustering/ # Partie A - Clustering
│ │ └── partie_A_clustering.ipynb
│ └── regression/ # Partie B - Régression
│ └── partie_B_regression.ipynb
│
├── outputs/ # Graphiques exportés
│ ├── clustering/
│ └── regression/
│
├── models/ # Modèles sauvegardés
│ ├── clustering/
│ └── regression/
│
├── env/ # Environnement virtuel Python
│
├── requirements.txt # Liste des dépendances
├── README.md # Ce fichier
└── .gitignore # Fichiers à ignorer (Git)


---

## ⚙️ Installation & Lancement

### 1. Cloner le projet
```bash
git clone https://github.com/ton-utilisateur/mall_customer_segmentation_project.git
cd mall_customer_segmentation_project

## Créer un environnement virtuel
python -m venv env

## Activer l’environnement virtuel
### Sous Windows :
env\Scripts\activate

### Sous Linux/macOS :
source env/bin/activate

##  Installer les dépendances
pip install -r requirements.txt


##🚀 Lancer les notebooks avec VS Code
### Ouvrir le projet dans VS Code :
code .

- Installer l’extension Jupyter si ce n’est pas encore fait.

- Ouvrir un des fichiers dans notebooks/clustering/ ou notebooks/regression/.

- Sélectionner le kernel Python correspondant à l’environnement virtuel env.

- Exécuter les cellules pas à pas.