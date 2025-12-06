from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from ..tools import make_email_template
from ..config import config
from ..utils import suppress_output_callback

email_template_tool = FunctionTool(make_email_template)

message_agent = Agent(
    name='MessageWriterAgent',
    model=config.worker_model,
    instruction="""You are MessageWriterAgent. Using planner_output and academic_output draft a polite email to a professor including student's name and course. Save to 'email_draft'.""" ,
    tools=[email_template_tool],
    output_key='email_draft',
    after_agent_callback=suppress_output_callback,
)
