import os
from dataclasses import dataclass

os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'False'
os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY_HERE"

class CampusConfig:
    worker_model: str = "gemini-2.5-flash"
    critic_model: str = "gemini-2.5-pro"

config = CampusConfig()
