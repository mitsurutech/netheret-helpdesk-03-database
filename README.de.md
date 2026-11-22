# Netheret-Helpdesk, Schritt 03: Datenbank

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Ein Beispiel für den Unterricht. In sechzehn Schritten bauen wir eine Helpdesk-Webanwendung für Netheret, ein erfundenes Unternehmen, das die IT kleiner Firmen betreut. Dieser Schritt fügt die Datenbank hinzu: die Tabellen aus dem ER-Diagramm als Python-Klassen und ein Skript, das sie mit Beispieldaten füllt.

## Was dieser Schritt hinzufügt

- `helpdesk/extensions.py`: das Objekt `db` aus Flask-SQLAlchemy.
- `helpdesk/models.py`: sechs Tabellen, `Company`, `User`, `Ticket`,
  `TicketUpdate`, `Job` und `Article`, mit den Listen der erlaubten Werte
  (Rollen, Kategorien, Prioritäten, Status und so weiter) am Anfang.
- `seed.py`: löscht alles und lädt Beispielfirmen, -benutzer, -supportanfragen,
  Einträge im Verlauf, Einsätze und Artikel der Wissensdatenbank.
- Die Startseite zählt jetzt die Zeilen jeder Tabelle, um zu zeigen, dass alles funktioniert.

## Starten

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`python seed.py` erstellt `instance/helpdesk.db`. Führen Sie es erneut aus, wann immer Sie
mit frischen Beispieldaten beginnen möchten. Es gibt die Demo-Konten aus; alle
verwenden das Demo-Passwort `password123`, das nur für dieses Beispiel gedacht ist.
Anmelden kann sich noch niemand: Das kommt im nächsten Schritt.

## Worauf Sie achten sollten

- `models.py`: wie jede Spalte einen Typ hat, welche leer sein dürfen
  (`| None`) und die Fremdschlüssel, die die Tabellen verbinden.
- `User.set_password`: Das Passwort wird mit Werkzeug gehasht, bevor es
  gespeichert wird, sodass die Datenbank nie das Passwort selbst enthält.
- `Ticket.set_reference`: Referenzen wie `NTH-0001` entstehen aus der ID, die
  es erst gibt, wenn die Zeile gespeichert ist; deshalb ruft `seed.py` `db.session.flush()` auf.
- Sie können die Datenbank mit jedem SQLite-Betrachter öffnen und die Zeilen ansehen.

## Diesen Schritt lernen

Dies ist Schritt 3 von 16 aus **Task 2. Developing the solution**, einer kostenlosen Reihe von Lektionen zu T Level Digital Software Development auf Englisch, die den Helpdesk von Netheret in agilen Sprints mit Python und Flask baut. Lesen Sie die Lektion zu diesem Schritt:
[Die Datenbank mit Flask-SQLAlchemy](https://mitsurutech.co.uk/resources/t-level/dsd-t2-03-database).

- Vorheriger Schritt: [Schritt 02, Seitenlayout mit Jinja-Vorlagen und CSS](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- Nächster Schritt: [Schritt 04, Anmeldung, Rollen und Sitzungen](https://github.com/mitsurutech/netheret-helpdesk-04-sign-in)
- [Alle kostenlosen Lektionen zu T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Diese Lektionen mit Ihrer Klasse auf MitsuruTech unterrichten](https://mitsurutech.co.uk/de/learning), [die Preise ansehen](https://mitsurutech.co.uk/de/pricing) oder
  [ein kostenloses Jahr für Ihre Schule beginnen](https://mitsurutech.co.uk/de/signup)

## Über dieses Beispiel

Geschrieben von [Mitsuru Technologies](https://mitsurutech.co.uk/de) (MitsuruTech) als Unterrichtsbeispiel für T Level Digital
Software Development. Die Aufgabenstellung Netheret IT Support Solutions stammt aus dem Muster-Prüfungsmaterial von Pearson; dieser Code
und seine Erläuterungen sind unsere eigenen und werden weder von Pearson noch vom Department for Education veröffentlicht, unterstützt oder genehmigt.
„T Level“ ist eine eingetragene Marke des Department for Education.
