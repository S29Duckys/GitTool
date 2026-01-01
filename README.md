# Git Tool

**Git Tool** est un utilitaire en ligne de commande (CLI) permettant d'interagir avec l'API GitHub.  
Il offre des fonctionnalités pour se connecter à un compte GitHub, consulter les informations du compte et créer des dépôts directement depuis le terminal.

---

## Fonctionnalités

- Connexion sécurisée à GitHub via un token personnel  
- Affichage des informations du compte :
  - nom d'utilisateur
  - nombre de dépôts publics
  - followers
  - following
- Création de dépôts publics ou privés  
- Recherche d'utilisateurs GitHub et affichage de leurs informations  
- Liste et suppression de dépôts  

---

## Prérequis

Avant d'installer et d'utiliser **Git Tool**, assurez-vous d'avoir :

- **Python 3.8 ou supérieur**
- **[Poetry](https://python-poetry.org/)** (gestionnaire de dépendances)
- **Un token GitHub personnel**

---

## Installation

1. Installer les dépendances avec Poetry
```
poetry install
```

2. Activer l'environnement virtuel
```
poetry shell
```

3. Lancer l'application
```
poetry run python src/git_tool/main.py
```

## Dépendances

- rich
- requests
- python-dotenv
- PyGithub
- prompt_toolkit
- readchar

## Génération d'un token GitHub

1. Allez dans **Settings** > **Developer settings** > **Personal access tokens**

2. Cliquez sur **Generate new token**

3. Cochez les permissions suivantes :

- **repo** (accès aux dépôts)
- **user** (informations du compte)


## Utilisation
**Se connecter à GitHub**

- Lancez l'application

- Choisissez l'option Connect GitHub

- Entrez votre token GitHub

**Consulter les informations du compte**

- Sélectionnez l'option Infos compte

- Affichage des informations GitHub

**Créer un dépôt**

- Sélectionnez Create repo

- Entrez le nom et la description

- Choisissez public ou privé

**Rechercher un utilisateur**

- Sélectionnez Search user

- Entrez le nom d'utilisateur GitHub

**Lister et supprimer des dépôts**

- Depuis Infos compte, affichez vos dépôts

- Supprimez un dépôt en entrant son nom

## Structure du projet

```bash
git_tool/
├── src/
│   └── git_tool/
│       ├── __init__.py
│       ├── main.py
│       └── tests/
├── poetry.lock
├── pyproject.toml
├── .example.env
├── .gitignore
└── README.md
```

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commit vos modifications (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Poussez la branche (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une Pull Request.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.