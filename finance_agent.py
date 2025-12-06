from google.adk.agents import Agent
from ..config import config

finance_agent = Agent(
    name='FinanceAgent',
    model=config.worker_model,
    instruction="""You are FinanceAgent. Provide up to 4 practical finance steps (scholarships, budgeting, jobs). Save to 'finance_output'.""" ,
    output_key='finance_output',
)
