import json
from agno.knowledge import Knowledge

with open("schema_data.json") as schemadata:
    data = json.load(schemadata)

texts = []                       #here Convert rows into readable sentences
for table, rows in data.items():
    for row in rows:
        line = f"TABLE: {table}\n"
        for k, v in row.items():
            line += f"{k}: {v}\n"
        texts.append(line)

# Create Knowledge from list of text  i.e gives searchable memory
knowledge = Knowledge(texts)
