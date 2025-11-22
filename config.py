import os
from dataclasses import dataclass
os.environ.setdefault('GOOGLE_GENAI_USE_VERTEXAI', 'True')
@dataclass
class CampusConfig:
    worker_model: str = 'gemini-2.5-flash'
    critic_model: str = 'gemini-2.5-pro'
config = CampusConfig()
