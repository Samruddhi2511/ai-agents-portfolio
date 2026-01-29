from sqlalchemy import text
from db import engine


def db_tool(query: str) -> str:
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                return "No data found."

            data = [dict(row._mapping) for row in rows]
            return "\n".join(str(d) for d in data)

    except Exception as e:
        return f"Database error: {str(e)}"


print("DB TOOL CALLED")
