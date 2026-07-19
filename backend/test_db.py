from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("Preethi@0908")

DATABASE_URL = f"postgresql://postgres:{password}@localhost:5432/service_desk"

engine = create_engine(DATABASE_URL)