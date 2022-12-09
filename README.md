# Site web d'Orange County Lettings

---
## Sommaire
#### 1. [Développement local](#dev_local)
#### 2. [Déploiement](#deploiement)
#### 3. [Journalisation](#journalisation)
---

<a name="dev_local"></a>
## 1. Développement local

### 1.1 Prérequis
```
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande $python de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).
```

### 1.2 macOS / Linux

#### 1.2.1 Cloner le repository
```
- $git clone https://github.com/tchou93/OPENCLASSROOMS_PYTHON_P13.git
```

Pour toutes les prochaines étapes, il faut se placer à la racine du projet.

#### 1.2.2 Créer l'environnement virtuel
```
- $python -m venv venv
- $apt-get install python3-venv (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement $source venv/bin/activate
- Confirmer que la commande $python exécute l'interpréteur Python dans l'environnement virtuel
$which python
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure $python --version
- Confirmer que la commande $pip exécute l'exécutable pip dans l'environnement virtuel, $which pip
- Pour désactiver l'environnement, $deactivate
```

#### 1.2.3 Exécuter le site
```
- $source venv/bin/activate
- $pip install --requirement requirements.txt
- $python manage.py runserver
- Aller sur http://localhost:8000 dans un navigateur
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
```

#### 1.2.4 Linting
```
- $source venv/bin/activate
- $flake8
```

#### 1.2.5 Tests unitaires
```
- $source venv/bin/activate
- $pytest
```

#### 1.2.6 Base de données
```
- Ouvrir une session shell $sqlite3
- Se connecter à la base de données $.open oc-lettings-site.sqlite3
- Afficher les tables dans la base de données $.tables
- Afficher les colonnes dans le tableau des profils, $pragma table_info(profiles_profile);
- Lancer une requête sur la table des profils, $select user_id, favorite_city from profiles_profile where favorite_city like 'B%';
- $.quit pour quitter
```

#### 1.2.7 Panel d'administration
```
- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`
```

### 1.3 Windows
```
Utilisation de PowerShell, comme ci-dessus sauf :
- Pour activer l'environnement virtuel, $source env/Scripts/activate
```

### 1.4 Conteneurisation du site sous Docker
```
- Créer un fichier d'environnement .env à la racine du projet
- Ajouter les variables d'environnement (ne pas mettre d'espace et de guillemets):
 PORT=8000
 DEBUG=TRUE
 SECRET_KEY => à définir
 SENTRY_DSN => à définir (voir la partie 3)
- Installer Docker desktop sur https://hub.docker.com/
- S'inscrire et s'identifier

Pour contruire l'image: 
- $docker build -t lettings .

Pour lancer le site localement en utilisant l'image: 
- $docker run -p 8000:8000 --env-file .env lettings
- Ouvrir le navigateur à la page localhost:8000

Pour pousser l'image vers le registre des conteneurs du Docker Hub:
- $docker tag lettings:latest <DOCKER_ACCOUNT_NAME>/lettings:latest
- $docker push <DOCKER_ACCOUNT_NAME>/lettings:latest

Pour récupérer la dernière image via le Docker Hub:
- $docker pull <DOCKER_ACCOUNT_NAME>/lettings:latest
```

<a name="deploiement"></a>
## 2. Déploiement
```
Le déploiement se fait via circleCI en trois étapes successives: 
1) L exécution du linting et la suite de tests
2) La conteneurisation du site sous Docker
3) La mise en production sous Heroku

La tâche de conteneurisation ne doit être exécutée que si la compilation et de test sont réussies.
Le travail de déploiement et de production ne doit s'exécuter que si le travail de conteneurisation est réussi.
```
### 2.1 Configuration de Docker
```
- Installer Docker desktop sur https://hub.docker.com/
- S'inscrire et se connecter
```

### 2.2 Configuration de Heroku
```
- S'incrire sur Heroku: https://signup.heroku.com/
- Se connecter
- Au niveau du tableau de bord cliquer sur "New" puis "Create new app"
- Donner un nom à l'application puis "Create app"
- Ajouter les variables d'environnement au projet:
SECRET_KEY => Clé secrète de l'application Django
SENTRY_DNS => DSN Sentry d'application (voir la partie 3)

```
### 2.3 Configuration de circleCI
```
- Lié le compte github à circleCI à partir du lien: https://circleci.com/signup/
- Aller sur "Projects"/"Project Setting"/"Environment variables"
- Ajouter les variables:
DOCKER_USERNAME => le nom d'utilisateur du compte Docker
DOCKER_PASS => le mot de passe du compte Docker
HEROKU_API_KEY => tableau de bord d'Heroku/"account setting"/"API KEY"
HEROKU_APP_NAME => nom de l'application sur Heroku
SECRET_KEY => Clé secrète de l'application Django
SENTRY_DNS => DSN Sentry d'application (voir la partie 3)
```

<a name="journalisation"></a>
## 3. Journalisation
```
- Lié le compte github à Sentry à partir du lien: https://sentry.io/signup/
- Créer un projet 
- Récupérer le DSN du projet: ouvrir le projet et partir sur "Project Setting"/"Client Keys (DSN)"/DSN
```


