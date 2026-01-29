from agno.tools import tool
from db import engine
from sqlalchemy import text
from tabulate import tabulate


@tool(stop_after_tool_call=True)
def db_tool(query: str) -> str:
    try:
        # Safety: allow only SELECT
        if not query.lower().strip().startswith("select"):
            return "Only SELECT queries are allowed."

        with engine.connect() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                return "This information is not present in my database."
            # Convert to list of dicts
            data = [dict(row._mapping) for row in rows]

            # for neat table
            table = tabulate(data, headers="keys", tablefmt="pretty")

            return table

    except Exception:
        return "This information is not present in my database."
