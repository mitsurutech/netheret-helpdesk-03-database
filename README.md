# Netheret help desk, step 03: database

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step adds the database: the tables from the ERD as Python classes, and a
script that fills them with sample data.

## What this step adds

- `helpdesk/extensions.py`: the `db` object from Flask-SQLAlchemy.
- `helpdesk/models.py`: six tables, `Company`, `User`, `Ticket`,
  `TicketUpdate`, `Job` and `Article`, with the lists of allowed values
  (roles, categories, priorities, statuses and so on) at the top.
- `seed.py`: deletes everything and loads sample companies, users, support
  requests, timeline updates, jobs and knowledge base articles.
- The home page now counts the rows in each table, to show it all works.

## Run it

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`python seed.py` makes `instance/helpdesk.db`. Run it again whenever you want
to start from fresh sample data. It prints the demo accounts; every one of
them uses the demo password `password123`, which is for this example only.
Nobody can sign in yet: that is the next step.

## What to look at

- `models.py`: how each column has a type, which ones may be empty
  (`| None`), and the foreign keys that join the tables.
- `User.set_password`: the password is hashed with Werkzeug before it is
  stored, so the database never holds the password itself.
- `Ticket.set_reference`: references like `NTH-0001` come from the id, which
  only exists once the row is saved, so `seed.py` calls `db.session.flush()`.
- You can open the database with any SQLite viewer and see the rows.

## Learn this step

This is step 3 of 16 of **Task 2. Developing the solution**, a free series of T Level Digital Software Development
lessons that builds the Netheret help desk in agile sprints with Python and Flask. Read the lesson for this step:
[The database with Flask-SQLAlchemy](https://mitsurutech.co.uk/resources/t-level/dsd-t2-03-database).

- Previous step: [step 02, page layout with jinja templates and css](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- Next step: [step 04, signing in, roles and sessions](https://github.com/mitsurutech/netheret-helpdesk-04-sign-in)
- [Every free T Level Digital lesson](https://mitsurutech.co.uk/resources/t-level)
- [Teach these lessons to your class on MitsuruTech](https://mitsurutech.co.uk/learning), [see the pricing](https://mitsurutech.co.uk/pricing) or
  [start a free year for your college](https://mitsurutech.co.uk/signup)

## About

Written by [Mitsuru Technologies](https://mitsurutech.co.uk) (MitsuruTech) as a teaching example for T Level Digital
Software Development. The Netheret IT Support Solutions brief is from Pearson's sample assessment material; this code
and its notes are our own, and are not published, endorsed or approved by Pearson or the Department for Education.
'T Level' is a registered trade mark of the Department for Education.

