import json
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5544/oncalldb"
)

TABLES = [
    "Tour",
    "TourGuest",
    "TourExpense",
    "TourRoute",
    "TourTracking",
]

all_data = {}

with engine.connect() as conn:
    for table in TABLES:
        rows = conn.execute(text(f'SELECT * FROM "{table}" LIMIT 5')).fetchall()
        formatted_rows = []
        for r in rows:
            formatted_rows.append(dict(r._mapping))
        all_data[table] = formatted_rows

with open("schema_data.json", "w") as f:
    json.dump(all_data, f, indent=2, default=str)

print("schema_data.json created!")
