from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from api.slack import Slack
from api.gmail import get_all_messages
from api.canvas import get_all_assignments
from api.aixplainintegration import get_llm_response
from api.sambanova import get_response

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust based on your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    user_message = message.message
    # slack_client = Slack()
    # slack_messages = slack_client.get_all_recent_messages()
    # gmail_messages = get_all_messages()
    # assigments = get_all_assignments()

    agent1_response = get_llm_response()
    agent2_response = get_response(agent1_response)



    return {"response": f'{agent2_response}'}
    # return {"response": f"Bot response to: {user_message}"}