# Servicio de asistencia de Netheret, paso 03: base de datos

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un ejemplo para enseñar. En dieciséis pasos construimos una aplicación web de servicio de asistencia para Netheret, una empresa inventada que da soporte informático a pequeñas empresas. Este paso añade la base de datos: las tablas del diagrama entidad-relación como clases de Python, y un script que las llena con datos de ejemplo.

## Qué añade este paso

- `helpdesk/extensions.py`: el objeto `db` de Flask-SQLAlchemy.
- `helpdesk/models.py`: seis tablas, `Company`, `User`, `Ticket`,
  `TicketUpdate`, `Job` y `Article`, con las listas de valores permitidos
  (roles, categorías, prioridades, estados, etc.) al principio.
- `seed.py`: borra todo y carga empresas, usuarios, solicitudes de soporte,
  actualizaciones de la línea de tiempo, trabajos y artículos de la base de conocimiento de ejemplo.
- La página de inicio cuenta ahora las filas de cada tabla, para demostrar que todo funciona.

## Ejecútalo

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`python seed.py` crea `instance/helpdesk.db`. Vuelve a ejecutarlo cuando quieras
empezar con datos de ejemplo nuevos. Muestra las cuentas de demostración; todas
usan la contraseña de demostración `password123`, que es solo para este ejemplo.
Todavía nadie puede iniciar sesión: eso llega en el paso siguiente.

## En qué fijarse

- `models.py`: cómo cada columna tiene un tipo, cuáles pueden quedar vacías
  (`| None`) y las claves foráneas que unen las tablas.
- `User.set_password`: la contraseña se convierte en hash con Werkzeug antes de
  guardarse, así que la base de datos nunca guarda la contraseña en sí.
- `Ticket.set_reference`: las referencias como `NTH-0001` salen del id, que
  solo existe cuando la fila se ha guardado, por eso `seed.py` llama a `db.session.flush()`.
- Puedes abrir la base de datos con cualquier visor de SQLite y ver las filas.

## Aprende este paso

Este es el paso 3 de 16 de **Task 2. Developing the solution**, una serie gratuita de lecciones de T Level Digital Software Development, en inglés, que construye el servicio de asistencia de Netheret en sprints ágiles con Python y Flask. Lee la lección de este paso:
[La base de datos con Flask-SQLAlchemy](https://mitsurutech.co.uk/resources/t-level/dsd-t2-03-database).

- Paso anterior: [paso 02, diseño de página con plantillas Jinja y CSS](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- Paso siguiente: [paso 04, iniciar sesión, roles y sesiones](https://github.com/mitsurutech/netheret-helpdesk-04-sign-in)
- [Todas las lecciones gratuitas de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseña estas lecciones a tu clase en MitsuruTech](https://mitsurutech.co.uk/es/learning), [mira los precios](https://mitsurutech.co.uk/es/pricing) o
  [empieza un año gratis para tu centro](https://mitsurutech.co.uk/es/signup)

## Acerca de

Escrito por [Mitsuru Technologies](https://mitsurutech.co.uk/es) (MitsuruTech) como ejemplo para enseñar T Level Digital
Software Development. El encargo de Netheret IT Support Solutions procede del material de evaluación de muestra de Pearson; este código
y sus notas son nuestros, y no los publica, respalda ni aprueba Pearson ni el Department for Education.
"T Level" es una marca registrada del Department for Education.
