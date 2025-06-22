# My\_Data\_App

Ce projet est une application Streamlit conteneurisée, déployée automatiquement grâce à un pipeline **CI/CD** avec **Jenkins** et **Docker**.

## 🚀 Fonctionnalités

* Visualisation de données via une application **Streamlit**.
* Déploiement automatisé via **Jenkins Pipeline**.
* Construction et envoi des images sur **Docker Hub**.
* Exposition de l'application via **Ngrok** (accès externe).
* Notifications par e-mail en cas de succès ou d'échec du déploiement.

---

## 📂 Arborescence du projet

```
My_Data_App/
├── .streamlit/               # Configuration Streamlit
├── data/                     # Datasets de l'application
├── jenkins-docker/           # Fichiers Docker liés au Jenkinsfile
├── docker_compose.yaml       # Fichier docker-compose
├── Dockerfile                # Image Docker pour l'application
├── Jenkinsfile               # Pipeline Jenkins
├── my_data_app.py            # Script principal de l'application
├── requirements.txt          # Dépendances Python
├── README.md                 # Ce fichier
```

---

## ⚙️ Prérequis

* Docker installé
* Jenkins installé (ou conteneur Jenkins fonctionnel)
* Compte Docker Hub
* Ngrok (pour exposer l'application si besoin)

---

## 🛠️ Exécution locale

```bash
# Construire l'image Docker
docker build -t attidiany/my_data_app .

# Lancer le conteneur
docker run -d --name my_data_app -p 8501:8501 attidiany/my_data_app
```

Accédez à l'application : [http://localhost:8501](http://localhost:8501)

---

## 🚀 Exécution via Jenkins

1️⃣ Créez un job **Pipeline** dans Jenkins (type : *Pipeline from SCM*).

2️⃣ Configurez le repo GitHub dans le job :
`https://github.com/AliatTidiany/My_Data_App.git`

3️⃣ Assurez-vous que Jenkins a accès aux **credentials Docker Hub** :
ID : `dockerhub-projetGroup4`

4️⃣ Le pipeline s'exécute automatiquement lors d'un `push` grâce au **webhook**.

---

## 🌐 Exposer avec Ngrok (optionnel)

```bash
ngrok http 8501
```

Un lien public sera généré (ex : `https://xxxx.ngrok-free.app`)

---

## 📬 Notifications

Le pipeline Jenkins envoie un e-mail :
✅ En cas de succès : `Déploiement réussi`
❌ En cas d'échec : `Échec du déploiement`

---

## 📌 Auteur

Alioune  MBODJI – *Projet DevOps*
