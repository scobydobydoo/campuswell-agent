from google.adk.agents import Agent
from ..config import config

finance_agent = Agent(
    name="FinanceAgent",
    model=config.worker_model,
    instruction="""
Provide up to 4 practical finance steps:
- study budget tips
- scholarship guidance
- part-time job suggestions
Save to finance_output.
""",
    output_key="finance_output",
)
