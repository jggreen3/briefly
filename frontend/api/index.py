from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from api.slack import Slack
from api.gmail import get_all_messages
from api.canvas import get_all_assignments

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
    slack_client = Slack()
    slack_messages = slack_client.get_all_recent_messages()
    gmail_messages = get_all_messages()
    assigments = get_all_assignments()


    return {"response": f'{assigments}'}
    # return {"response": f"Bot response to: {user_message}"}


