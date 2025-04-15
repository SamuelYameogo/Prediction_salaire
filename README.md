
# 📊 Application de Prédiction avec Régression Linéaire

Ce projet propose une application complète de régression linéaire pour prédire une valeur cible en fonction de plusieurs variables explicatives. Dans ce cas, l'objectif est de prédire un salaire en fonction de l'âge, du genre, du niveau d'éducation, du poste occupé et des années d'expérience. Le projet intègre la création d'une API avec Flask, le déploiement dans Google Cloud Platform (GCP) et la dockerisation du modèle pour sa mise en production.

---

## 🗂️ Table des matières

1. [Introduction](#-introduction)
2. [Structure du projet](#-structure-du-projet)
3. [Installation](#-installation)
4. [Utilisation](#-utilisation)
5. [Déploiement](#-déploiement)
6. [Tests](#-tests)
7. [Contribution](#-contribution)
8. [Licence](#-licence)

---

## 🧠 Introduction

Ce projet, fruit d'un travail de groupe scolaire pour but de démontrer l'application pratique des concepts de régression linéaire dans un contexte de machine learning. Il inclut également des étapes pratiques telles que :

- Préparation des données (nettoyage, recodage, et standardisation).
- Entraînement et évaluation d'un modèle de régression linéaire.
- Création d'une API avec Flask pour l'accès au modèle.
- Dockerisation de l'application.
- Déploiement de l'API sur Google Cloud Platform (GCP).

A l'issue de quoi l'API permet de retourner une prédiction du salaire basé sur les variables d'entrée.

---

## 🗃️ Structure du projet

Le projet est organisé comme suit :

```
/.idea                   # Dossier de configuration pour l'IDE (JetBrains)
modules/                 # Contient les modules Python spécifiques au traitement des données et au modèle
static/                  # Dossier pour les fichiers statiques (CSS, JS, images) si nécessaire pour l'interface
templates/               # Contient les templates HTML pour les pages web si nécessaire
app.py                   # Application principale Flask contenant les routes pour l'API
best_Ridge_model.joblib  # Modèle Ridge sauvegardé (format joblib)
best_Ridge_model.pkl     # Modèle Ridge sauvegardé (format pickle)
Dockerfile               # Fichier de configuration Docker pour créer l'image
model.pkl                # Modèle de régression linéaire sauvegardé (pickle)
model1.pkl               # Modèle de régression linéaire alternatif (pickle)
Projet_Lamrani.ipynb     # Notebook Jupyter montrant les étapes de préparation et d'entraînement du modèle
README.md                # Documentation du projet
requirements.txt         # Liste des dépendances nécessaires (Flask, scikit-learn, pandas, etc.)
```

---

## ⚙️ Installation

### Prérequis

- **Python 3.6+** : [Télécharger Python](https://www.python.org/downloads/)
- **Git** : [Télécharger Git](https://git-scm.com/downloads)
- **Docker** : [Télécharger Docker](https://www.docker.com/products/docker-desktop)
- **Google Cloud Platform** : Créez un compte sur [GCP](https://cloud.google.com/).

### Étapes d'Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/ton-utilisateur/nom-du-repo.git
   cd nom-du-repo
   ```

2. Créez un environnement virtuel et activez-le :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Utilisation

### Lancer l'API

Lancez l'application Flask avec la commande suivante :

```bash
python app.py
```

L'API sera accessible à l'adresse suivante dans votre navigateur : [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Routes disponibles

- **`/predict` (Méthode POST)** : Envoie un JSON avec les variables explicatives après saisie et retourne la prédiction du salaire.

  Exemple de requête :

  ```json
  {
    "Age": 30,
    "Gender": "Male",
    "Education Level": "Master",
    "Job Title": "Software Engineer",
    "Years of Experience": 5
  }
  ```

- **`/health` (Méthode GET)** : Vérifie si le service est opérationnel. Retourne `{"status": "ok"}` si l'API fonctionne correctement.

---

## ☁️ Déploiement

### Dockerisation

1. Construire l'image Docker :

   ```bash
   docker build -t monapp-deploiement .
   ```

2. Lancer l'image Docker :

   ```bash
   docker run -p 5000:5000 monapp-deploiement
   ```

### Déploiement sur Google Cloud Platform (GCP)

1. Créez un compte GCP et configurez un projet.

2. Push de l'image Docker vers Google Container Registry (GCR) :

   ```bash
   docker tag monapp-deploiement gcr.io/[YOUR_PROJECT_ID]/monapp-deploiement
   docker push gcr.io/[YOUR_PROJECT_ID]/monapp-deploiement
   ```

3. Déployer sur Google Cloud Run :

   ```bash
   gcloud run deploy --image gcr.io/[YOUR_PROJECT_ID]/monapp-deploiement --platform managed
   ```

L'API est désormais accessible via une URL publique sur GCP du style https://samuel-155985849716.us-central1.run.app.
    
    Celui est expiré, car GCP est une plateforme d'ébergement payant.
---

## ✅ Tests

Les tests peuvent être réalisés en local que ce soit pour vérifier les performances du modèle où réaliser des prédictions. Ou encore via le service déployé.   


---

## 🤝 Contribution

Ce dépôt est libre de licence. Toutefois, les modifications directes sur le dépôt ne sont pas autorisées. Si vous souhaitez proposer une amélioration, une correction ou une nouvelle fonctionnalité, merci de me contacter par e-mail à l'adresse suivante :

📧 pawndtaoresamuel@gmail.com

---

## 📄 Licence

Ce projet est distribué sans licence formelle, il est libre d'utilisation et de modification dans un cadre personnel ou commercial. Toutefois, les contributions doivent passer par un contact préalable à l'adresse e-mail ci-dessus.
