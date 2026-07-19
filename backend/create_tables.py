from database.db import engine, Base
from models.ticket import Ticket

Base.metadata.create_all(bind=engine)

print("Tickets table created successfully!")