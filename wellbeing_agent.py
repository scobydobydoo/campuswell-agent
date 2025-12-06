from google.adk.agents import Agent
from ..config import config

wellbeing_agent = Agent(
    name='WellbeingAgent',
    model=config.worker_model,
    instruction="""You are a wellbeing coach. Based on {planner_output} provide short morning/evening routines and 3 stress techniques. Save to 'wellbeing_output'.""" ,
    output_key='wellbeing_output',
)
