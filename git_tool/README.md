# Git Tool

**Git Tool** est un utilitaire en ligne de commande (CLI) permettant d'interagir avec l'API GitHub. Il offre des fonctionnalités pour se connecter à un compte GitHub, consulter les informations du compte, et créer des dépôts directement depuis le terminal.

---

## Fonctionnalités

* Connexion sécurisée à GitHub via un token personnel.
* Affichage des informations du compte (nom d'utilisateur, nombre de dépôts publics, followers, following).
* Création de dépôts publics ou privés.

---

## Prérequis

Avant d'installer et d'utiliser Git Tool, assurez-vous d'avoir installé les éléments suivants sur votre machine :

* **Python 3.8 ou supérieur**
* **[Poetry](https://python-poetry.org/)** (gestionnaire de dépendances et packaging)
* **Un token GitHub personnel** (pour l'authentification)

---

## Installation

1. **Cloner le dépôt** (si vous avez déjà le code, passez à l'étape suivante) :
   ```bash
   git clone https://github.com/votre-utilisateur/git_tool.git
   cd git_tool
   ```

2. **Installer les dépendances avec Poetry** :
   ```bash
   poetry install
   ```

3. **Activer l'environnement virtuel de Poetry** :
   ```bash
   poetry shell
   ```

4. **Lancer l'application** :
   ```bash
   python src/git_tool/main.py
   ```

---

## Génération d'un token GitHub

Pour utiliser Git Tool, vous devez générer un token GitHub personnel :

1. Allez dans **Paramètres** > **Developer settings** > **Personal access tokens**.
2. Cliquez sur **Generate new token**.
3. Donnez un nom à votre token et cochez les permissions suivantes :
   * `repo` (pour accéder aux dépôts)
   * `user` (pour accéder aux informations du compte)
4. Copiez le token généré et conservez-le en lieu sûr.

---

## Utilisation

### Se connecter à GitHub
* Lancez l'application et choisissez l'option `Connect GitHub`.
* Entrez votre token GitHub lorsque vous y êtes invité.

### Consulter les informations du compte
* Une fois connecté, sélectionnez l'option `Infos compte` pour afficher vos informations GitHub.

### Créer un dépôt
* Sélectionnez l'option `Create repo`.
* Entrez le nom et la description du dépôt.
* Choisissez si le dépôt doit être public ou privé.

---

## Structure du projet

```
git_tool/
├── src/
│   └── git_tool/
│       ├── __init__.py
│       ├── main.py
│       └── tests/
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commit vos modifications (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Poussez la branche (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une Pull Request.

---

## Licence

