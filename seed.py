"""Fill the database with sample data, so there is something to look at.

Run it with:  python seed.py

WARNING: it deletes everything in the database first, then adds the samples.
Every date is worked out from today, so the data always looks recent.
"""
from datetime import datetime, timedelta

from helpdesk import create_app
from helpdesk.extensions import db
from helpdesk.models import Article, Company, Job, Ticket, TicketUpdate, User

# DEMO ONLY: every sample account signs in with this same easy password.
# Never use a password like this on a real system.
EVERYONE_SIGNS_IN_WITH = "password123"

# The phone numbers are from Ofcom's range kept for drama, so none is real.
COMPANIES = {
    "brightwell": ("Brightwell Bakery", "12 Mill Lane, Bristol BS1 4AA", "0117 496 0101"),
    "harbour": ("Harbour Dental Practice", "3 Quay Street, Bristol BS1 5BB", "0117 496 0202"),
    "kestrel": ("Kestrel Accountants", "Unit 7, Temple Court, Bristol BS2 6CC", "0117 496 0303"),
    "moorside": ("Moorside Garage", "88 Moor Road, Bristol BS4 7DD", "0117 496 0404"),
}

# key: (name, email, role, company key or None)
USERS = {
    "maya": ("Maya Patel", "manager@netheret.example", "manager", None),
    "tom": ("Tom Reid", "tier1@netheret.example", "tier1", None),
    "aisha": ("Aisha Khan", "aisha@netheret.example", "tier1", None),
    "sam": ("Sam Okafor", "tier2@netheret.example", "tier2", None),
    "ben": ("Ben Clarke", "ben@netheret.example", "tier2", None),
    "priya": ("Priya Shah", "tier3@netheret.example", "tier3", None),
    "lucy": ("Lucy Hart", "customer@brightwell.example", "customer", "brightwell"),
    "david": ("David Moss", "customer@harbour.example", "customer", "harbour"),
    "nadia": ("Nadia Ali", "nadia@kestrel.example", "customer", "kestrel"),
    "gary": ("Gary Webb", "gary@moorside.example", "customer", "moorside"),
}

# (company, raised by, title, description, category, priority, status, tier,
#  assigned to, days ago, hours taken to resolve or None)
TICKETS = [
    ("brightwell", "lucy", "Till printer will not print receipts",
     "The receipt printer on the main till beeps but prints nothing.",
     "hardware", "high", "resolved", 1, "tom", 20, 3),
    ("harbour", "david", "Cannot sign in to email",
     "Our receptionist gets 'wrong password' even after typing it carefully.",
     "account", "medium", "closed", 1, "aisha", 18, 1),
    ("kestrel", "nadia", "Wi-Fi drops every afternoon",
     "From about 2pm the Wi-Fi keeps disconnecting in the back office.",
     "network", "high", "resolved", 2, "sam", 15, 30),
    ("moorside", "gary", "New laptop needs setting up",
     "We bought a laptop for the workshop and need it set up with our software.",
     "hardware", "low", "closed", 2, "ben", 14, 50),
    ("brightwell", "lucy", "Accounts software shows an update error",
     "The accounts program says an update failed every time it starts.",
     "software", "medium", "resolved", 1, "tom", 12, 5),
    ("harbour", "david", "Patient booking system very slow",
     "Booking an appointment takes over a minute. Patients are waiting at the desk.",
     "software", "critical", "resolved", 3, "priya", 9, 20),
    ("kestrel", "nadia", "Printer offline for the whole office",
     "Nobody can print. The printer says it is ready but the PCs say offline.",
     "hardware", "medium", "resolved", 1, "aisha", 8, 2),
    ("moorside", "gary", "Password reset for the parts system",
     "I have forgotten my password for the parts ordering system.",
     "account", "low", "resolved", 1, "tom", 7, 0.5),
    ("brightwell", "lucy", "Card reader keeps losing its connection",
     "The card reader drops its connection a few times a day, so payments fail.",
     "network", "high", "open", 2, "sam", 5, None),
    ("harbour", "david", "Backup failed overnight",
     "The backup report email says last night's backup failed.",
     "software", "critical", "open", 3, "priya", 4, None),
    ("kestrel", "nadia", "Second monitor flickers",
     "The second screen on my desk flickers on and off.",
     "hardware", "low", "waiting", 1, "aisha", 3, None),
    ("moorside", "gary", "Router lights flashing red",
     "The internet router has a red flashing light and the internet is very slow.",
     "network", "high", "open", 2, None, 2, None),
    ("brightwell", "lucy", "New user account for a new starter",
     "A new member of staff starts on Monday and needs an email account.",
     "account", "medium", "new", 1, None, 1, None),
    ("harbour", "david", "Reception PC makes a grinding noise",
     "The PC under the reception desk has started making a grinding noise.",
     "hardware", "medium", "new", 1, None, 0.2, None),
    ("kestrel", "nadia", "Spreadsheet macro stopped working",
     "Our month-end spreadsheet macro now stops with an error.",
     "software", "low", "open", 1, "tom", 6, None),
    ("moorside", "gary", "Email attachments blocked",
     "Customers say the invoices we email arrive without the attachment.",
     "other", "medium", "waiting", 1, "tom", 3, None),
]

# (ticket number in the list above, author, body, visible to customer,
#  new status or None, hours after the ticket was raised)
UPDATES = [
    (1, "tom", "Talked Lucy through clearing a paper jam. Printing again.", True, "resolved", 3),
    (2, "aisha", "Reset the password and checked she could sign in.", True, "resolved", 1),
    (3, "tom", "Not a quick fix. Escalated to Tier 2.", False, "open", 1),
    (3, "sam", "Visited and added a second access point. Signal is strong now.", True, "resolved", 30),
    (6, "aisha", "Database server is overloaded. Escalated to Tier 3.", False, "open", 0.5),
    (6, "priya", "Moved the database to faster storage. Booking takes 2 seconds now.", True, "resolved", 20),
    (9, "tom", "Escalated to Tier 2. Looks like the base station.", False, "open", 2),
    (9, "sam", "Booked a visit to replace the base station this week.", True, None, 26),
    (10, "priya", "Looking at the backup logs now.", True, "open", 1),
    (11, "aisha", "Could you send a photo of the cable at the back of the monitor?", True, "waiting", 4),
    (12, "tom", "Escalated to Tier 2 for an on-site visit.", False, "open", 1),
    (16, "tom", "Asked Gary which email program sends the invoices.", True, "waiting", 2),
]

# (company, ticket number or None, engineer, title, kind, days from this
#  Monday, start hour, minutes, cancelled?)
JOBS = [
    ("kestrel", 3, "sam", "Fit a second Wi-Fi access point", "installation", -5, 10, 120, False),
    ("moorside", 4, "ben", "Set up new laptop on site", "installation", -4, 14, 90, False),
    ("harbour", None, "priya", "Quarterly server maintenance", "maintenance", 0, 9, 180, False),
    ("brightwell", 9, "sam", "Replace card reader base station", "repair", 1, 13, 90, False),
    ("moorside", 12, "ben", "Replace faulty router", "repair", 2, 10, 120, False),
    ("kestrel", None, "priya", "Firewall firmware update", "maintenance", 2, 16, 60, True),
    ("kestrel", None, "ben", "Install new office printer", "installation", 3, 14, 60, False),
    ("harbour", 10, "priya", "Check backup drive and storage box", "repair", 4, 9, 120, False),
    ("brightwell", None, "sam", "Annual PC health check", "maintenance", 8, 10, 240, False),
]

BRIEF = ("Report to reception and sign in. Ask the customer which machines are affected "
         "before you start. Take spare cables. Before you leave, check that everything "
         "works with the customer and write what you did in the notes.")

# (title, symptoms, solution, category, author, views, helpful)
ARTICLES = [
    ("Printer shows as offline",
     "PCs say the printer is offline, but the printer's screen says it is ready.",
     "1. Turn the printer off and on again.\n2. Check it has the same network name as before.\n"
     "3. On the PC, remove the printer and add it again.", "hardware", "aisha", 41, 17),
    ("Resetting an email password",
     "A user cannot sign in to email, or has forgotten their password.",
     "1. Check who they are: ask for their date of birth or staff number.\n"
     "2. Reset the password in the admin centre.\n3. Ask them to choose a new one on first sign in.",
     "account", "tom", 63, 25),
    ("Wi-Fi keeps dropping",
     "Laptops lose the Wi-Fi connection now and then, often in one part of the building.",
     "1. Check the signal strength where it happens.\n2. Move the access point or add another one.\n"
     "3. If many devices are affected, escalate to Tier 2 for a site survey.", "network", "sam", 22, 8),
    ("Receipt printer not printing",
     "The till receipt printer beeps or shows a light but prints nothing.",
     "1. Open the cover and clear any paper jam.\n2. Check the paper roll is the right way round.\n"
     "3. Turn the printer off and on.", "hardware", "tom", 18, 9),
    ("Computer running slowly",
     "A PC takes a long time to start or to open programs.",
     "1. Restart it: many problems clear after a restart.\n2. Check free disk space.\n"
     "3. Check for updates that are waiting to install.", "software", "aisha", 35, 11),
    ("Email attachments go missing",
     "People receive our emails but the attached file is not there.",
     "1. Check the size of the file: most mail systems refuse files over 20 MB.\n"
     "2. Check the file type is not blocked (for example .exe).\n3. Send a link to the file instead.",
     "other", "tom", 9, 2),
]


def main():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        now = datetime.now().replace(second=0, microsecond=0)

        companies = {}
        for key, (name, address, phone) in COMPANIES.items():
            companies[key] = Company(name=name, address=address, phone=phone)
            db.session.add(companies[key])

        users = {}
        for key, (name, email, role, company_key) in USERS.items():
            user = User(name=name, email=email, role=role,
                        company=companies.get(company_key), created_at=now - timedelta(days=60))
            user.set_password(EVERYONE_SIGNS_IN_WITH)
            users[key] = user
            db.session.add(user)

        tickets = []
        for (company, raiser, title, description, category, priority, status, tier,
             assigned, days_ago, hours_to_resolve) in TICKETS:
            created = now - timedelta(days=days_ago)
            ticket = Ticket(
                title=title, description=description, category=category,
                priority=priority, status=status, tier=tier,
                company=companies[company], raised_by=users[raiser],
                assigned_to=users.get(assigned), created_at=created,
            )
            if hours_to_resolve is not None:
                ticket.resolved_at = created + timedelta(hours=hours_to_resolve)
            db.session.add(ticket)
            tickets.append(ticket)

        # flush() sends the new rows to the database so they get their ids,
        # which the references are made from.
        db.session.flush()
        for ticket in tickets:
            ticket.set_reference()
            # Set updated_at here, after the reference: otherwise saving the
            # reference would stamp updated_at with the time right now.
            ticket.updated_at = ticket.resolved_at or ticket.created_at

        for number, author, body, visible, status_change, hours in UPDATES:
            ticket = tickets[number - 1]
            db.session.add(TicketUpdate(
                ticket=ticket, author=users[author], body=body,
                visible_to_customer=visible, status_change=status_change,
                created_at=ticket.created_at + timedelta(hours=hours),
            ))

        monday = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0)
        for (company, ticket_number, engineer, title, kind, day, hour, minutes,
             cancelled) in JOBS:
            start = monday + timedelta(days=day, hours=hour)
            end = start + timedelta(minutes=minutes)
            if cancelled:
                status = "cancelled"
            elif end < now:
                status = "done"
            else:
                status = "scheduled"
            db.session.add(Job(
                company=companies[company], engineer=users[engineer],
                ticket=tickets[ticket_number - 1] if ticket_number else None,
                title=title, brief=BRIEF, kind=kind, scheduled_start=start,
                duration_minutes=minutes, status=status,
            ))

        for title, symptoms, solution, category, author, views, helpful in ARTICLES:
            db.session.add(Article(
                title=title, symptoms=symptoms, solution=solution, category=category,
                author=users[author], views=views, helpful_count=helpful,
                updated_at=now - timedelta(days=30),
            ))

        db.session.commit()
        print("Sample data loaded.")
        print("Demo accounts (all use the demo password from seed.py):")
        for name, email, role, _ in USERS.values():
            print(f"  {role:9} {email}")


if __name__ == "__main__":
    main()
