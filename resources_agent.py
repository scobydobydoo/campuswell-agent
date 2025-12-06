from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from ..tools import parse_student_profile
from ..config import config

resources_agent = Agent(
    name='ResourcesAgent',
    model=config.worker_model,
    instruction="""You are ResourceNavigatorAgent. Recommend campus resources and how/when to use them. Save to 'resources_output'.""" ,
    tools=[FunctionTool(parse_student_profile)],
    output_key='resources_output',
)
