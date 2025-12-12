from google.adk.agents import Agent
from ..config import config

resources_agent = Agent(
    name="ResourcesAgent",
    model=config.worker_model,
    instruction="""
Provide a list of 5 campus or online resources the student can use:
- tutoring centers
- notes libraries
- office hours
- study communities
- mental health support
Save to resources_output.
""",
    output_key="resources_output",
)
