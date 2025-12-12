from google.adk.agents import Agent, LoopAgent
from google.adk.tools import FunctionTool, google_search
from ..config import config
from ..utils import suppress_output_callback
from ..validation_checkers import PlanValidationChecker
from ..tools import parse_student_profile

plan_tool = FunctionTool(parse_student_profile)

planner_agent = Agent(
    name="AcademicPlannerAgent",
    model=config.worker_model,
    instruction="""
You are AcademicPlannerAgent.
Using the student's raw_profile (from parse_student_profile tool),
create a detailed 7-day structured study plan with time blocks,
subject priorities, and goals. Save output to planner_output.
""",
    tools=[plan_tool, google_search],
    output_key="planner_output",
    after_agent_callback=suppress_output_callback,
)

robust_planner = LoopAgent(
    name="robust_planner",
    sub_agents=[
        planner_agent,
        PlanValidationChecker(name="plan_validation_checker")
    ],
    max_iterations=3,
    after_agent_callback=suppress_output_callback,
)
