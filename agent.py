from google.adk.agents import SequentialAgent
from google.adk.tools import AgentTool, FunctionTool
from sub_agents.planner_agent import robust_planner
from sub_agents.academic_agent import academic_agent
from sub_agents.wellbeing_agent import wellbeing_agent
from sub_agents.finance_agent import finance_agent
from sub_agents.resources_agent import resources_agent
from sub_agents.message_agent import message_agent

orchestrator = SequentialAgent(
    name='CampusWellOrchestrator',
    sub_agents=[
        robust_planner,
        academic_agent,
        wellbeing_agent,
        finance_agent,
        resources_agent,
        message_agent,
    ],
)
