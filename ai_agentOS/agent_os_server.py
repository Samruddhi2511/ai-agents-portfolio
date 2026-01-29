from agno.agent import Agent
from agno.os import AgentOS
from agno.models.anthropic import Claude
from tools import db_tool
from agent import run_agent_logic

my_agent = Agent(
    name="PostgreSQL Agent",
    model=Claude(
        id="claude-3-haiku-20240307",
        max_tokens=1000,
    ),

    tools=[db_tool],
    instructions="Answer database queries using SQL.",
)

agent_os = AgentOS(
    id="postgres-agent-os",            # unique identifier
    description="My PostgreSQL AI Agent",
    agents=[my_agent],                  # list of agents
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agent_os_server:app", reload=True)
