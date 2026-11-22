# Centre d'assistance Netheret, étape 03 : base de données

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un exemple pour enseigner. En seize étapes, nous construisons une application web de centre d'assistance pour Netheret, une entreprise imaginaire qui s'occupe de l'informatique de petites entreprises. Cette étape ajoute la base de données : les tables du MCD sous forme de classes Python, et un script qui les remplit avec des données d'exemple.

## Ce que cette étape ajoute

- `helpdesk/extensions.py` : l'objet `db` de Flask-SQLAlchemy.
- `helpdesk/models.py` : six tables, `Company`, `User`, `Ticket`,
  `TicketUpdate`, `Job` et `Article`, avec en tête les listes de valeurs autorisées
  (rôles, catégories, priorités, statuts, etc.).
- `seed.py` : efface tout et charge des entreprises, des utilisateurs, des demandes
  d'assistance, des mises à jour de fil chronologique, des interventions et des articles de base de connaissances d'exemple.
- La page d'accueil compte désormais les lignes de chaque table, pour montrer que tout fonctionne.

## Lancer l'application

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`python seed.py` crée `instance/helpdesk.db`. Relancez-le chaque fois que vous voulez
repartir de données d'exemple neuves. Il affiche les comptes de démonstration ; tous
utilisent le mot de passe de démonstration `password123`, réservé à cet exemple.
Personne ne peut encore se connecter : c'est l'étape suivante.

## À regarder

- `models.py` : comment chaque colonne a un type, lesquelles peuvent être vides
  (`| None`), et les clés étrangères qui relient les tables.
- `User.set_password` : le mot de passe est haché avec Werkzeug avant d'être
  enregistré, si bien que la base ne contient jamais le mot de passe lui-même.
- `Ticket.set_reference` : les références comme `NTH-0001` viennent de l'id, qui
  n'existe qu'une fois la ligne enregistrée, d'où l'appel à `db.session.flush()` dans `seed.py`.
- Vous pouvez ouvrir la base avec n'importe quel visualiseur SQLite et voir les lignes.

## Apprendre cette étape

Voici l'étape 3 sur 16 de **Task 2. Developing the solution**, une série gratuite de leçons de T Level Digital Software Development, en anglais, qui construit le centre d'assistance Netheret en sprints agiles avec Python et Flask. Lisez la leçon de cette étape :
[La base de données avec Flask-SQLAlchemy](https://mitsurutech.co.uk/resources/t-level/dsd-t2-03-database).

- Étape précédente : [étape 02, mise en page avec les gabarits Jinja et le CSS](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- Étape suivante : [étape 04, connexion, rôles et sessions](https://github.com/mitsurutech/netheret-helpdesk-04-sign-in)
- [Toutes les leçons gratuites de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseigner ces leçons à votre classe sur MitsuruTech](https://mitsurutech.co.uk/fr/learning), [voir les tarifs](https://mitsurutech.co.uk/fr/pricing) ou
  [commencer une année gratuite pour votre établissement](https://mitsurutech.co.uk/fr/signup)

## À propos

Écrit par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) (MitsuruTech) comme exemple pédagogique pour le T Level Digital
Software Development. Le cahier des charges Netheret IT Support Solutions provient du matériel d'évaluation type de Pearson ; ce code
et ses notes sont les nôtres, et ne sont ni publiés, ni soutenus, ni approuvés par Pearson ou le Department for Education.
« T Level » est une marque déposée du Department for Education.
