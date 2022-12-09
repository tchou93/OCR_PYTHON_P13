# Site web d'Orange County Lettings

---
## Sommaire
#### 1. [Développement local](#dev_local)
#### 2. [Déploiement](#deploiement)
#### 3. [Journalisation](#journalisation)
---

<a name="dev_local"></a>
## Développement local

### Prérequis
```
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).
```

### macOS / Linux

#### Cloner le repository
```
- `git clone https://github.com/tchou93/OPENCLASSROOMS_PYTHON_P13.git`
```

Pour toutes les prochaines étapes, il faut se placer à la racine du projet.

#### Créer l'environnement virtuel
```
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`
```

#### Exécuter le site
```
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
```

#### Linting
```
- `source venv/bin/activate`
- `flake8`
```

#### Tests unitaires
```
- `source venv/bin/activate`
- `pytest`
```

#### Base de données
```
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter
```

#### Panel d'administration
```
- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`
```

### Windows
```
Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
```

### Conteneurisation du site sous Docker
```
TBD
```

### La mise en production sous Heroku
```
TBD
```

<a name="deploiement"></a>
## Déploiement
```
Le déploiement se fait via circleCI en trois étapes successives: 
1) L exécution du linting et la suite de tests
2) La conteneurisation du site sous Docker
3) La mise en production sous Heroku

La tâche de conteneurisation ne doit être exécutée que si la compilation et de test sont réussies.
Le travail de déploiement et de production ne doit s'exécuter que si le travail de conteneurisation est réussi.

!!!!!A compléter : un récapitulatif haut niveau du fonctionnement du déploiement
la configuration requise pour que le déploiement fonctionne correctement
les étapes nécessaires pour effectuer le déploiement (votre successeur doit être capable de suivre vos instructions 
et de faire le travail sans problème, sans avoir à passer du temps à rechercher le problème/la solution lui-même).
!!!!!
```

<a name="journalisation"></a>
## Journalisation
```
!!!!! A définir: Veuillez mettre à jour la documentation sur le déploiement en conséquence (là encore, votre successeur devrait pouvoir mettre en place facilement la journalisation de Sentry décrite ici)!!!!!
```


