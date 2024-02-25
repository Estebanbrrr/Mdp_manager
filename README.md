
# Gestionnaire de Mots de Passe

Le Gestionnaire de Mots de Passe est une application web conçue pour stocker de manière sécurisée vos mots de passe. Facile à utiliser, elle offre une interface utilisateur intuitive pour ajouter, supprimer et visualiser vos mots de passe.

## Fonctionnalités

- **Ajout sécurisé** de nouveaux mots de passe.
- **Visualisation** rapide de vos mots de passe enregistrés.
- **Suppression** facile des mots de passe.
- Interface utilisateur **simple et épurée**.
- Sécurité renforcée avec **cryptage** des mots de passe.

## Technologies Utilisées

- Backend : Flask (Python)
- Frontend : HTML, CSS, JavaScript
- Base de données : MySQL

## Installation

Pour mettre en place et exécuter le Gestionnaire de Mots de Passe localement, suivez ces étapes :

1. Clonez ce dépôt :

```bash
git clone https://github.com/Estebanbrrr/Mdp_manager.git
cd Mdp_manager
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

3. Initialisez la base de données (si nécessaire) :

```bash
flask db upgrade
```

4. Lancez l'application :

```bash
flask run
```

Votre application devrait maintenant être accessible à l'adresse [http://localhost:5000](http://localhost:5000).

## Usage

Après avoir lancé l'application, naviguez vers [http://localhost:5000](http://localhost:5000) pour accéder à l'interface web du Gestionnaire de Mots de Passe.

- Cliquez sur **Ajouter un nouveau mot de passe** pour enregistrer un nouveau mot de passe.
- Visualisez la liste des mots de passe enregistrés sur la page principale.
- Utilisez le bouton **Supprimer** à côté de chaque entrée pour supprimer un mot de passe.

## Contribution

Les contributions sont toujours les bienvenues ! Si vous souhaitez contribuer au projet, n'hésitez pas à forker le dépôt et soumettre une pull request.

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## Contact

Votre Nom – [@votreTwitter](https://twitter.com/votreTwitter) – email@example.com

Lien du projet : [https://github.com/Estebanbrrr/Mdp_manager](https://github.com/Estebanbrrr/Mdp_manager)
