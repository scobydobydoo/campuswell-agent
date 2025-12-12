from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from ..tools import make_email_template
from ..config import config
from ..utils import suppress_output_callback

email_tool = FunctionTool(make_email_template)

message_agent = Agent(
    name="MessageWriterAgent",
    model=config.worker_model,
    instruction="""
Using planner_output and academic_output from session state,
draft a polite email a student can send to a professor requesting help.
Use the make_email_template tool to structure the message.
Save final email to email_draft.
""",
    tools=[email_tool],
    output_key="email_draft",
    after_agent_callback=suppress_output_callback,
)
