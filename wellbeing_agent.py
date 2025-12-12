from google.adk.agents import Agent
from ..config import config

wellbeing_agent = Agent(
    name="WellbeingAgent",
    model=config.worker_model,
    instruction="""
Using planner_output, create:
- a morning routine
- an evening routine
- 3 stress-management techniques
Save to wellbeing_output.
""",
    output_key="wellbeing_output",
)
