from agentos import Agent
from agent import run_agent_logic


def my_brain(message: str) -> str:
    return run_agent_logic(message)


personal_ai = Agent(
    name="PersonalAI",
    brain=my_brain
)
