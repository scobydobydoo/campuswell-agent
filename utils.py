from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content, TextPart

def suppress_output_callback(callback_context: CallbackContext) -> Content:
    return Content(role="assistant", parts=[TextPart(text="")])
