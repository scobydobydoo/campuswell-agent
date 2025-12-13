from google.adk.agents import Agent
from ..config import config

academic_agent = Agent(
    name="AcademicSupportAgent",
    model=config.worker_model,
    instruction="""
Use planner_output and raw_profile from session state.
Provide subject-specific strategies and 3 practice activities per subject.
Save output to academic_output.
""",
    output_key="academic_output",
)
