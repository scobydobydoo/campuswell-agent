from google.adk.agents import Agent
from ..config import config

academic_agent = Agent(
    name='AcademicSupportAgent',
    model=config.worker_model,
    instruction="""You are AcademicSupportAgent. Using {planner_output} and profile, provide subject-specific strategies and 3 practice activities per subject. Save to 'academic_output'.""" ,
    output_key='academic_output',
)
